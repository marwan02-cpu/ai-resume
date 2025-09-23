'use client'
import {Textarea} from "@heroui/react";

function TextArea(){
    return (
    <Textarea
      isClearable
      className="max-w-3xl"
      label="Enter the bullet points you want tailored here"
      placeholder="Description"
      variant="bordered"
      size="lg"
    />
  );
}

export default TextArea;