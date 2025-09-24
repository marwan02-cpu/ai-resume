'use server'
import '../prompt/prompt'


export async function SendPrompt() {
  var dataToSend : Prompt = {content: "Testing"}

  const data = await fetch('http://127.0.0.1:8000/prompt' , {
    method: "POST",
     headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToSend)
  });
  
  const promptResult = await data.json();
  await GetPromptResult(promptResult);
}

export async function GetPromptResult(promptResult){
    return promptResult
}