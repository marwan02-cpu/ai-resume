'use server'
import '../../prompt/prompt'

export async function SendPrompt(prompt: string) {
  var dataToSend : Prompt = {content: prompt}

  const data = await fetch('http://127.0.0.1:8000/prompt' , {
    method: "POST",
     headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToSend)
  });

  const promptResult = await data.json();
  console.log(promptResult);

  return promptResult
}