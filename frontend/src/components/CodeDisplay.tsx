import React, { useState } from 'react';
import { ConversionResponse } from '../types/api';

interface CodeDisplayProps {
  result: ConversionResponse;
}

export const CodeDisplay: React.FC<CodeDisplayProps> = ({ result }) => {
  const [copiedSection, setCopiedSection] = useState<string | null>(null);

  const copyToClipboard = async (text: string, section: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedSection(section);
      setTimeout(() => setCopiedSection(null), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  return (
    <div>
      <section>
        <h3>Logic Explanation</h3>
        <div>
          {result.logic}
        </div>
      </section>

      <section>
        <h3>Unit Tests</h3>
        <div style={{ position: 'relative' }}>
          <pre style={{ backgroundColor: '#f5f5f5', padding: '1rem', overflow: 'auto' }}>
            <code>{result.unit_tests}</code>
          </pre>
          <button
            onClick={() => copyToClipboard(result.unit_tests, 'unit_tests')}
            style={{ position: 'absolute', top: '10px', right: '10px' }}
          >
            {copiedSection === 'unit_tests' ? 'Copied!' : 'Copy'}
          </button>
        </div>
      </section>

      <section>
        <h3>Python Code</h3>
        <div style={{ position: 'relative' }}>
          <pre style={{ backgroundColor: '#f5f5f5', padding: '1rem', overflow: 'auto' }}>
            <code>{result.python_code}</code>
          </pre>
          <button
            onClick={() => copyToClipboard(result.python_code, 'python_code')}
            style={{ position: 'absolute', top: '10px', right: '10px' }}
          >
            {copiedSection === 'python_code' ? 'Copied!' : 'Copy'}
          </button>
        </div>
      </section>
    </div>
  );
};