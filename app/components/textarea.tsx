'use client'
import {Textarea} from "@heroui/react";

function TextArea(){
    return (
    <Textarea
      isClearable
      className="max-w-xs"
      defaultValue="Enter the bullet points you want the resume tailored to"
      label="Description"
      placeholder="Description"
      variant="bordered"
    />
  );
}

export default TextArea;