'use server'
export default async function SendPrompt() {
  const data = await fetch('http://127.0.0.1:8000/prompt' , {
    method: "POST",
    body: JSON.stringify({})
  });
  const posts = await data.json();
  console.log("test")
  console.log(posts);
}