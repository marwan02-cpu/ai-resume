'use client'
import "./main.css";
import PrimaryButton from './components/button';
import Textarea from './components/textarea';
import ReadOnlyTextArea from "./components/readOnlyTextArea";
import { useInput, usePrompt } from "./hooks/prompt/prompt";

export default function Home() {
  const { inputData, handleChange } = useInput();
  const { promptData, loading, error, callSendPrompt } = usePrompt(inputData);

  return (
    <div className="flex flex-col gap-24">
      <h1 className="text-3xl font-bold self-center">
        Tailor your Resume with AI
      </h1>
      <div className="flex justify-around gap-8">
          <Textarea onValueChange={handleChange} value={inputData}></Textarea>
          <ReadOnlyTextArea promptResult={promptData}></ReadOnlyTextArea>
      </div>
      <PrimaryButton action={callSendPrompt}></PrimaryButton>
    </div>
  )
}