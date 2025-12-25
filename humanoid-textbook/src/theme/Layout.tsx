import React from 'react';
import OriginalLayout from '@theme-original/Layout';
import Chatbot from '../components/Chatbot/Chatbot';
import type { Props } from '@theme/Layout';

export default function Layout(props: Props) {
  return (
    <>
      <OriginalLayout {...props} />
      <Chatbot />
    </>
  );
}