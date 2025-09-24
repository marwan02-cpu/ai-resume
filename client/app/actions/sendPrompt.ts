'use server'
export default async function SendPrompt() {
  const data = await fetch('http://127.0.0.1:8000');
  const posts = await data.json();
  console.log("test")
  console.log(posts);
}