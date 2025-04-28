import OpenAI from "openai";

const apiKey = process.env.REACT_APP_DEEPSEEK_API_KEY;

const openai = new OpenAI({
  baseURL: 'https://api.deepseek.com',
  apiKey: apiKey,
  dangerouslyAllowBrowser: true
});


export const getAIMessage = async (userQuery, oldMessages) => {
  const inscope = await checkInScope(userQuery);
  if (inscope == "None") {
    return  {
      role: "assistant",
      content: `Sorry that's outside of what I can assist with, but I'm happy to help with other questions related to PartSelect products!`
    }
  }
  const retrievedContext = await getContext(userQuery);
  let newMessages;
  if (oldMessages.length == 1) {
    newMessages = [
      {"role": "system", "content": `Use the retrieved context to answer as a chatbot to a user. Do not add "Based on the retrieved context," in your response. If a part is not in list of compatible parts for a model then they are not compatible. If retrieved context does not provide adequate information to answer user question then respond saying I currently do not have information regarding this product. Please try again later`},
      {"role": "user", "content": `Context: ${retrievedContext}\n\nQuestion: ${userQuery}`}
  ]
  } else {
    newMessages = [...oldMessages, {
      "role": "user",
      "content": `Context: ${retrievedContext}\n\nQuestion: ${userQuery}`
    }]
  }
  const response = await openai.chat.completions.create({
    model:"deepseek-chat",
    messages: newMessages
  });
  const textResponse = response.choices[0].message.content
  const message = 
    {
      role: "assistant",
      content: textResponse
    }
  return message;
};


export const checkInScope = async (userQuery) => {
  const response = await openai.chat.completions.create({
    model:"deepseek-chat",
    messages: [
        {"role": "system", "content": `You are an agent that determines if 
          the given query is in or out of scope. 
          If the query is not a question about PartSelect product information or assistance with
          installation or a PartSelect product, return None. If the question is in scope then return Pass. Your
          response is limited to a single string: either "None" or "Pass"`},
        {"role": "user", "content": userQuery}
    ]
  });

  const textResponse = response.choices[0].message.content
  return textResponse;
};

export const getContext = async (userQuery) => {
  const res = await fetch("http://localhost:8001/query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: userQuery })
  });
  const data = await res.json();
  return data.results['documents'][0].toString()
}
