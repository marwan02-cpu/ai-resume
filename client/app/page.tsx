"use client";
import "./main.css";
import PrimaryButton from "./components/button";
import Textarea from "./components/textarea";
import ReadOnlyTextArea from "./components/readOnlyTextArea";
import { useInput, usePrompt } from "./hooks/prompt/prompt";
import LoadingIndicator from "./components/loadingIndicator";

export default function Home() {
  const { inputData, handleChange } = useInput();
  const { promptData, loading, error, callSendPrompt } = usePrompt(inputData);

  return (
    <div className="flex flex-col gap-24 h-screen justify-center">
      <h1 className="self-center text-4xl font-extrabold">
        Extract resume keywords with
        <span
          className="ml-2 bg-gradient-to-r from-teal-400 via-sky-500 to-purple-600 
               bg-clip-text text-transparent"
        >
          AI
        </span>
      </h1>

      <div className="flex justify-around gap-8">
        <Textarea onValueChange={handleChange} value={inputData}></Textarea>
        <ReadOnlyTextArea promptResult={promptData}></ReadOnlyTextArea>
      </div>
      {loading ? <LoadingIndicator></LoadingIndicator> : <PrimaryButton action={callSendPrompt}></PrimaryButton>}
      
    </div>
  );
}
