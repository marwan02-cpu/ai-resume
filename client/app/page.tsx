import "./main.css";
import PrimaryButton from './components/button';
import Textarea from './components/textarea';
import ReadOnlyTextArea from "./components/readOnlyTextArea";
import SendPrompt from "./actions/sendPrompt";

export default function Home() {

  return (
    <div className="flex flex-col gap-24">
      <h1 className="text-3xl font-bold self-center">
        Tailor your Resume with AI
      </h1>
      <div className="flex justify-around gap-8">
          <Textarea></Textarea>
          <ReadOnlyTextArea promptResult={}></ReadOnlyTextArea>
      </div>
      <PrimaryButton getData={SendPrompt}></PrimaryButton>
    </div>
  )
}