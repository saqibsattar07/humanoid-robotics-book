import React from 'react';
import Layout from '@theme/Layout';
import Chatbot from '../Chatbot/Chatbot';

interface LayoutWrapperProps {
  children: React.ReactNode;
  title?: string;
  description?: string;
}

const LayoutWrapper: React.FC<LayoutWrapperProps> = ({ children, title, description }) => {
  return (
    <Layout title={title} description={description}>
      {children}
      <Chatbot />
    </Layout>
  );
};

export default LayoutWrapper;