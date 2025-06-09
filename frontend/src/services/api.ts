import { ConversionResponse, ApiError } from '../types/api';
import { apiConfig } from '../config/client';

const API_BASE_URL = `${apiConfig.baseUrl}/api/v1`;

export class ApiClient {
  static async convertAdaFile(file: File): Promise<ConversionResponse> {
    const formData = new FormData();
    formData.append('ada_file', file);

    const response = await fetch(`${API_BASE_URL}/convert`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const errorData: ApiError = await response.json();
      throw new Error(errorData.error || 'Conversion failed');
    }

    return response.json();
  }
}