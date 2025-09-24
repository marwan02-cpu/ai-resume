'use client'
import { useState } from 'react';
import { SendPrompt } from '../../actions/prompt/sendPrompt'; 

export function UsePrompt(){

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const callSendPrompt = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await SendPrompt();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, callSendPrompt };
}