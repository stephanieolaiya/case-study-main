from bs4 import BeautifulSoup
import requests
import time
import json

headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    "cookie":
"_vwo_uuid_v2=DF673CDB3DE6A1CDE6BA1A8A0FB10250B|2f6eae4007dea3d2fac3bf01308506d5; clearRVDataOnLoad=Efmfufe; ai_user=IYcfIc7/3zgPxXUxV8eYRz|2025-04-27T04:23:08.307Z; _gcl_au=1.1.758008982.1745727788; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DF673CDB3DE6A1CDE6BA1A8A0FB10250B; _vwo_ds=3%241745727788%3A91.79196549%3A%3A; InternalSearch=usvf; _vis_opt_exp_62_combi=2; _vis_opt_exp_65_combi=2; _vis_opt_exp_70_combi=2; GA_MrAppliance=wbsjbujpo; _hjSessionUser_1213522=eyJpZCI6IjRhNjdkMDRhLWY5NDUtNTUxMi1hMjc2LTdkMmRlMmVjZTU5MyIsImNyZWF0ZWQiOjE3NDU3Mjc3ODg4NDIsImV4aXN0aW5nIjp0cnVlfQ==; CountryCode=VT; _gid=GA1.2.154190232.1745727790; IR_gbd=partselect.com; _fbp=fb.1.1745727789787.790147743907374724; _pin_unauth=dWlkPU9UQTBZMlEyWXpFdFpXTTBPQzAwWkRNNExUbGxOak10TURaaVkyWTNNR1psTVRoaw; __idcontext=eyJjb29raWVJRCI6IjJ3SVNxekxjbmNlek81N0ZQWkdZRUJIT3BjNiIsImRldmljZUlEIjoiMndJU3F6UUdiQ1M2N05jb2M1ZVhJU1Z3MzZUIiwiaXYiOiIiLCJ2IjoiIn0%3D; phr_rule=organic; _abck=1F94291BF0DCACF632BC1E5445E8768A~0~YAAQhvNuaG/kp0iWAQAAlGyNdQ20pKLKv+6gQBLcwOCeMJi66WPm0FG0PTPnmQdNf4z9jd32KCAiqcQQ9JNtzsSjekDXxgxJLvhPu7E08pE9GALPA+lLV+im4y2aSEJat1teJGKxUdlVBvbRBegIGQhhFIh4QwWCj9SfEcYF5nTcdcr3VN3turV3v3EzVLjTIbXC9R3+b3KpLFXu3lFm068mXzHYyZYJCkvs1hycNbW1HF1MHWpHu7o7ZCGZhgR8w5Yq4zP+loji/SfoHsDz9bXgp2gCPW7ovLqh+SddM6ssYO0c8oQdRZnCW6nlCdGvLgzkx+P+kzmxVuJMJIGc3FbaHzikA4gplg3XLC0MWcotoloFwQZRGVmWdgSxyl3OASRe4zbfoP/6m192bSddwPhEdE7puu0gXs4+7/HlhPlbwvG964HgIM5IsgWbbd/2PGj6p0Eflw6rkNaQdjxsss4sh+ZedEstBq0xuFY4o4mUf3+5HjTD+1kPCxNYTWoMvWC4LIk0EUDlRzLFjRDj3dKQRYoDWseRuZtDNeYhf8Mv8x4vLuv7W+FtSh2IUw6bOLDPm0twtw==~-1~-1~-1; FirstVisit=usvf; _vis_opt_exp_65_goal_202=1; _vis_opt_exp_65_goal_204=1; _vis_opt_exp_72_combi=2; _vis_opt_exp_77_combi=2; _vis_opt_exp_77_goal_1=1; .AspNetCore.Antiforgery.Xh2vXOVYRfQ=CfDJ8MxFXhWWlKdLsXYEntchT1uRcHMF2rZ2nccclBmAF9ESjI-K-CAhK-xPAEBg0RXKXT77dXud8tQJsimcANYE2y496hw0-UJZ_YuplpjuG55aq3ZNT8R73ynl8eyhqFqG4mlAp8aMu66QVz6cCB1ux6M; bm_ss=ab8e18ef4e; _hjSession_1213522=eyJpZCI6IjJlYzU3MzRkLWM2M2ItNGM3Mi05Y2FhLWYyYmM0NjIxMzc2NSIsImMiOjE3NDU3NDA4NzkyMzQsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; GABRAND=Admiral; bm_s=YAAQhvNuaBbnqEiWAQAA+oREdgP6Adpcbqix2W7MCtaC5l9tFam+J0jRHzNyu8e4TTXYGvXiTHBAcNpEfbd6D591Bd0JgKMjfDCiU2J3Z6fzGgrfWjBdPcwmqYYcsO5gNYMGpym9NEg0vtMO/iaHQkqBu8mvtDl6V1C9ZevLtAzfXWHVj5Le0PZr2LA7nb+udVziZltiaNp1X5j4PUZp4a1G1zoXDyOUbtwpY1V9rfOQNJqPAHpunOeYEzLOMl+7v5u4yYkY72/PWRDa5BOXsXXupRgfiFBdCVvPRCaOl+EbqZrM9rQ1zXJ2RG/uy7nOBTY/lmVHFElzoauJWrfZzhM+yRDAyuYB0W/c4L/VAkk8ZBelWUij6ejifPtZbDu0SUuMgj3FwLdTMcUIWjvVUJTysZiAwwP2brc1W7kleFplIJUNm3/9lnUonRk2E/j0YWHkmE37sncmqKi3xA==; bm_so=FF17A8BC8245BE4D62B55EF442828FB9A1036F6EFFE4779F8C4A57A1B5DC5787~YAAQhvNuaBfnqEiWAQAA+oREdgPXGNshADip7JcHFATbWq9cDGv5zB1Cl4U2rLy7MXfV/zVOuSrABfi+y/94czbNZVHXou6zxe+mcCVrQwEo44lJrFH0fPATFtAzH/CeUcM3/4tyL3wTkLWb6yrv4LEhZfES+mkm2bBI8uv+31AeNlMXpkH0Bo9O413alth7lzRScl2sUZVdDb2CRlcIN8aoNu1LWziwtWpwxgHHFaqyX25V/4Uxlf/AOZYskomHsRjRifsmF7ISJCmX/ADDS8cQqz4y0yVraiGnI1e249bFBmtrS74b66ZM1p2Gt2oQVK2XJS8U1usMx9X9SMni/rW/O64bf+BToU4OcHwKYBzSrLKdUB5u6qifSYpqD00uHl+bV0hkn4PuetU3/ib6lf/hnTFrYo0A7Us9QycLhoceIVyxdnSFgMfHMkC2UgWGkZ0QWY4jE7cFaQp1VFKd7Uc=; bm_sz=1A41D6AE01AEB5ECC1433706BDFBB266~YAAQhvNuaBjnqEiWAQAA+oREdhuv9GEmntt/demWTHtKTvtqugfXH5MMHA0rg5dwFK8QfSAk0VUhovH4RHpEnJu518o4aTcXOfoGV8o4YJmqIFbZRkj9cVaeiFL81uhp0q/mscCojqj6HD1uRptiw96uhnInkgJ/ptFEB3TQdfyuLP8aVu7o+V0gQkpj9jS5ceqZ6oT7qxavEL5ikiR88ydZRsoM/ZNfN3c3omw9Hkw0yMv4wVTkZaldsT2XoRAQDHPwrJ+xvVbz1q0kqQzB7xYyudICyAtIEMN6yeFP2JQGWbBqgZuWfLFBpaBIPVM5ZteuN1ObPwwUT9AFAly/FETMvTZUVOmbZjg5DlMJOiO/0BcXKQglIDa9gZxidZZ09V2uIgKV19CWZ/sjVwCw6zRUiZ/oIUiFmtz3/ydaPNPEAS4ETAskgzpL7YXBzoL/AwYsth8AFQe7a2HbMByNTewJ77C556GG3D3LY0tOz5ziiECA3fhvPo6zkEsKI0htAHd0tGTYSyjzouDxrTUBSnFJ/Cz7orj0N48iEe7UtPprkxxU4g5pgHib6/9LDJjRaan33cvF1W5t~4473913~4342342; chref=/Admiral-Refrigerator-Trays-and-Shelves.htm; _vwo_sn=9556%3A4; bm_lso=FF17A8BC8245BE4D62B55EF442828FB9A1036F6EFFE4779F8C4A57A1B5DC5787~YAAQhvNuaBfnqEiWAQAA+oREdgPXGNshADip7JcHFATbWq9cDGv5zB1Cl4U2rLy7MXfV/zVOuSrABfi+y/94czbNZVHXou6zxe+mcCVrQwEo44lJrFH0fPATFtAzH/CeUcM3/4tyL3wTkLWb6yrv4LEhZfES+mkm2bBI8uv+31AeNlMXpkH0Bo9O413alth7lzRScl2sUZVdDb2CRlcIN8aoNu1LWziwtWpwxgHHFaqyX25V/4Uxlf/AOZYskomHsRjRifsmF7ISJCmX/ADDS8cQqz4y0yVraiGnI1e249bFBmtrS74b66ZM1p2Gt2oQVK2XJS8U1usMx9X9SMni/rW/O64bf+BToU4OcHwKYBzSrLKdUB5u6qifSYpqD00uHl+bV0hkn4PuetU3/ib6lf/hnTFrYo0A7Us9QycLhoceIVyxdnSFgMfHMkC2UgWGkZ0QWY4jE7cFaQp1VFKd7Uc=^1745740951606; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+27+2025+04%3A02%3A39+GMT-0400+(Eastern+Daylight+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CBG24%3A1%2CC0004%3A1%2CC0007%3A0&AwaitingReconsent=false; _ga=GA1.1.197047067.1745727790; IR_22088=1745740961594%7C0%7C1745740961594%7C%7C; _uetsid=535e55a0231f11f08157d11c34cea430; _uetvid=535e7a60231f11f0bac36920d5417841; __kla_id=eyJjaWQiOiJaVFZoTjJabE16Y3RZbVF4WWkwME5qUmhMV0kyTTJJdE1ETXlPVE14WVRVd01qTTEiLCIkcmVmZXJyZXIiOnsidHMiOjE3NDU3Mjc3OTAsInZhbHVlIjoiaHR0cHM6Ly9wb3J0YWwuaW5zdGFsaWx5LmFpLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5wYXJ0c2VsZWN0LmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3NDU3NDA5NjQsInZhbHVlIjoiaHR0cHM6Ly93d3cucGFydHNlbGVjdC5jb20vUmVmcmlnZXJhdG9yLVBhcnRzLmh0bSIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5wYXJ0c2VsZWN0LmNvbS9SZWZyaWdlcmF0b3ItVHJheXMtYW5kLVNoZWx2ZXMuaHRtIn19; ai_session=ricI15ezHUl1+6/TPjBMow|1745737344979|1745741286070; _ga_4NJ2YKSQY4=GS1.1.1745740059.3.1.1745741321.60.0.0",
"host": "www.partselect.com",
"referer": "https://www.partselect.com/Products/",
"sec-ch-ua":
'"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
"sec-ch-ua-mobile":
"?0",
"sec-ch-ua-platform":"macOS",
"sec-fetch-dest": "document,",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests":"1",
"User-Agent":
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

def scrape_product_page(product_page_url, product): 
    page = requests.get(product_page_url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    popular_parts = []
    for popular_part_div in soup.find_all("div", class_="nf__part__detail"):
        popular_parts.append(popular_part_div.get_text())
    # extract all links 
    uls = soup.find_all('ul', class_='nf__links')
    # List of tuples: (link text, href)
    links = [
        (a.get_text(strip=True), a['href'])
        for ul in uls
        for li in ul.find_all('li')
        for a in li.find_all('a', href=True)
    ]   

    # extract brand links, related parts links, model links 
    brands = []
    brand_links = []
    models = []
    model_links = []
    related_parts_links = []
    # extract related parts links
    for text, link in links:
        if 'Refrigerator Parts' in text:
            brands.append(text)
            brand_links.append(link)
        elif '/Models/' in link:
            models.append(text)
            model_links.append(link)
        else:
            related_parts_links.append(link)

    # extract common problems
    common_problems = soup.find("div", class_="rich-content mb-4")
    if common_problems:
        common_problems = common_problems.get_text()

    return {
        "product": product,
        "popular parts": popular_parts,
        "models": models,
        "brands": brands,
        "common problems fixes": common_problems
    }, brand_links, model_links, related_parts_links


def scrape_model_links(models, model_page_links):
    assert(len(models) == len(model_page_links))
    base_url = 'https://www.partselect.com/'
    for model, model_link in zip(models, model_page_links):
        time.sleep(2)
        page = requests.get(base_url + model_link, headers=headers)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, "html.parser")
            parts = []
            for part_div in soup.find_all("div", class_="mega-m__part"):
                parts.append(part_div.get_text())
            model_info = {
                "model": model,
                "compatible parts": parts
            }
            with open('./data/scraped_data.jsonl', 'a') as f:
                f.write(json.dumps(model_info) + '\n')
        else: 
            print(f"Could not extract model: {model}")


if __name__ == "__main__":
    # res = scrape_product_page("https://www.partselect.com/Refrigerator-Parts.htm", 'Refrigerators')
    # with open('./data/scraped_data.jsonl', 'a') as f:
    #     f.write(json.dumps(res) + '\n')

    # # scrape popular models info
    # scrape_model_links(res[0]['models'], res[2])
    res = scrape_product_page("https://www.partselect.com/Dishwasher-Parts.htm", 'Dishwashers')
    with open('./data/scraped_data.jsonl', 'a') as f:
        f.write(json.dumps(res) + '\n')

    # scrape popular models info
    scrape_model_links(res[0]['models'], res[2])
    
    # scrape 
    

