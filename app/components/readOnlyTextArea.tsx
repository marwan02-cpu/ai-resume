'use client'
import {Textarea} from "@heroui/react";

function readOnlyTextArea() {
    return (
    <Textarea
      isReadOnly
      className="max-w-xs"
      defaultValue="Wait for bullet points here"
      label="Description"
      placeholder="Description"
      variant="bordered"
    />
  );
}

export default readOnlyTextArea;
