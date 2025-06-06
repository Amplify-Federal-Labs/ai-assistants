import React, { useState } from 'react';
import { QueryClient, QueryClientProvider, useMutation } from '@tanstack/react-query';
import { FileUpload } from './components/FileUpload';
import { CodeDisplay } from './components/CodeDisplay';
import { ApiClient } from './services/api';
import { ConversionResponse } from './types/api';

const queryClient = new QueryClient();

function AppContent() {
  const [conversionResult, setConversionResult] = useState<ConversionResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const convertMutation = useMutation({
    mutationFn: ApiClient.convertAdaFile,
    onSuccess: (data) => {
      setConversionResult(data);
      setError(null);
    },
    onError: (error: Error) => {
      setError(error.message);
      setConversionResult(null);
    },
  });

  const handleFileUpload = (file: File) => {
    convertMutation.mutate(file);
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
      <header style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1>Ada to Python Converter</h1>
        <p>Upload your Ada files and get Python code with unit tests and explanations</p>
      </header>

      <main>
        <FileUpload 
          onUpload={handleFileUpload} 
          isLoading={convertMutation.isPending}
        />

        {error && (
          <div style={{ 
            backgroundColor: '#fee', 
            color: '#c00', 
            padding: '1rem', 
            marginTop: '1rem',
            borderRadius: '4px',
            border: '1px solid #fcc'
          }}>
            <strong>Error:</strong> {error}
          </div>
        )}

        {conversionResult && (
          <div style={{ marginTop: '2rem' }}>
            <CodeDisplay result={conversionResult} />
          </div>
        )}
      </main>
    </div>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AppContent />
    </QueryClientProvider>
  );
}

export default App;