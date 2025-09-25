'use client'
import {Textarea} from "@heroui/react";

function TextArea({value, onValueChange}){
    return (
    <Textarea
      isClearable
      className="max-w-3xl"
      label="Enter the bullet points you want tailored here"
      placeholder="Description"
      variant="bordered"
      size="lg"
      value={value}
      onValueChange={onValueChange}
    />
  );
}

export default TextArea;