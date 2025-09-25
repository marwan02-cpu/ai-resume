'use client'
import { useState } from 'react';
import { SendPrompt } from '../../actions/prompt/sendPrompt'; 

export function usePrompt(prompt: string){

  const [promptData, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const callSendPrompt = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await SendPrompt(prompt);
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { promptData, loading, error, callSendPrompt };
}

export function useInput(){

  const [inputData, setTextareaValue] = useState('');

  function handleChange(value: string){
    setTextareaValue(value);
    console.log(value)
  }

  return { inputData, handleChange };
}