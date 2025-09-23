'use client'
import {Textarea} from "@heroui/react";

function readOnlyTextArea() {
    return (
    <Textarea
      isReadOnly
      className="max-w-3xl"
      label="Wait for tailored bullet points here"
      variant="bordered"
      size="lg"
    />
  );
}

export default readOnlyTextArea;
