import "./main.css";
import {Button} from '@heroui/button';

export default function Home() {
  return (
    <div>
      <h1 className="text-3xl font-bold">
        Tailor your Resume with AI
      </h1>
      <div className="flex">
        <Textarea></Textarea>
        <ReadOnlyTextArea></ReadOnlyTextArea>
      </div>
      <PrimaryButton></PrimaryButton>
    </div>
  )
}