'use client'
import {Textarea} from "@heroui/react";

function readOnlyTextArea({promptResult}) {
    return (
    <Textarea
      isReadOnly
      className="max-w-3xl"
      label="Wait for tailored bullet points here"
      variant="bordered"
      size="lg"
      value={promptResult}
    />
  );
}

export default readOnlyTextArea;
