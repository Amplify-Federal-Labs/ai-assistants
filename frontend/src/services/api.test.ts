import { describe, it, expect, beforeEach, vi } from 'vitest'
import { ApiClient } from './api'

// Mock fetch globally
global.fetch = vi.fn()

describe('ApiClient', () => {
  beforeEach(() => {
    vi.resetAllMocks()
  })

  describe('convertAdaFile', () => {
    it('should successfully convert Ada file', async () => {
      const mockResponse = {
        logic: 'Test logic explanation',
        unit_tests: 'Test unit tests',
        python_code: 'print("Hello World")'
      }

      vi.mocked(fetch).mockResolvedValueOnce({
        ok: true,
        json: async () => mockResponse
      } as Response)

      const file = new File(['with Ada.Text_IO; use Ada.Text_IO;'], 'test.adb', {
        type: 'text/plain'
      })

      const result = await ApiClient.convertAdaFile(file)

      expect(fetch).toHaveBeenCalledWith('http://localhost:8000/api/v1/convert', {
        method: 'POST',
        body: expect.any(FormData)
      })
      expect(result).toEqual(mockResponse)
    })

    it('should throw error when API returns error', async () => {
      const errorResponse = { error: 'File is empty' }

      vi.mocked(fetch).mockResolvedValueOnce({
        ok: false,
        json: async () => errorResponse
      } as Response)

      const file = new File([''], 'empty.adb', { type: 'text/plain' })

      await expect(ApiClient.convertAdaFile(file)).rejects.toThrow('File is empty')
    })

    it('should include file in FormData', async () => {
      vi.mocked(fetch).mockResolvedValueOnce({
        ok: true,
        json: async () => ({})
      } as Response)

      const file = new File(['test content'], 'test.adb', { type: 'text/plain' })
      await ApiClient.convertAdaFile(file)

      const formData = vi.mocked(fetch).mock.calls[0][1]?.body as FormData
      expect(formData.get('ada_file')).toBe(file)
    })
  })
})