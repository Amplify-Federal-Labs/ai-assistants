import React, { useState } from 'react';
import { useForm } from 'react-hook-form';

interface FileUploadProps {
  onUpload: (file: File) => void;
  isLoading?: boolean;
}

interface FormData {
  ada_file: FileList;
}

export const FileUpload: React.FC<FileUploadProps> = ({ onUpload, isLoading = false }) => {
  const { register, handleSubmit, formState: { errors }, setValue, watch } = useForm<FormData>();
  const [fileError, setFileError] = useState<string>('');
  
  const validateFile = (file: File) => {
    const validExtensions = ['.ada', '.adb'];
    const fileExtension = file.name.toLowerCase().slice(file.name.lastIndexOf('.'));
    
    if (!validExtensions.includes(fileExtension)) {
      setFileError('Please select a valid Ada file (.ada or .adb)');
      return false;
    }
    
    setFileError('');
    return true;
  };

  const onSubmit = (data: FormData) => {
    const file = data.ada_file?.[0];
    
    if (!file) {
      setFileError('Please select a file');
      return;
    }
    
    if (!validateFile(file)) {
      return;
    }
    
    onUpload(file);
    setValue('ada_file', undefined as any);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && !validateFile(file)) {
      e.target.value = '';
      setValue('ada_file', undefined as any);
    } else if (file) {
      setFileError('');
    }
  };

  return (
    <div>
      <h2>Upload Ada File</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label htmlFor="ada_file">Select Ada File:</label>
          <input
            id="ada_file"
            type="file"
            accept=".ada,.adb"
            {...register('ada_file', { required: 'Please select a file' })}
            onChange={handleFileChange}
            disabled={isLoading}
          />
        </div>
        
        {(errors.ada_file || fileError) && (
          <div style={{ color: 'red' }}>
            {errors.ada_file?.message || fileError}
          </div>
        )}
        
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Converting...' : 'Convert'}
        </button>
      </form>
    </div>
  );
};