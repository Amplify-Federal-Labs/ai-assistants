import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { FileUpload } from './FileUpload'

describe('FileUpload', () => {
  const mockOnUpload = vi.fn()

  beforeEach(() => {
    vi.resetAllMocks()
  })

  it('should render file upload form', () => {
    render(<FileUpload onUpload={mockOnUpload} />)
    
    expect(screen.getByText('Upload Ada File')).toBeInTheDocument()
    expect(screen.getByLabelText(/select ada file/i)).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /convert/i })).toBeInTheDocument()
  })

  it('should accept .ada and .adb files', () => {
    render(<FileUpload onUpload={mockOnUpload} />)
    
    const fileInput = screen.getByLabelText(/select ada file/i)
    expect(fileInput).toHaveAttribute('accept', '.ada,.adb')
  })

  it('should call onUpload when valid file is submitted', async () => {
    const user = userEvent.setup()
    render(<FileUpload onUpload={mockOnUpload} />)
    
    const file = new File(['with Ada.Text_IO;'], 'test.adb', { type: 'text/plain' })
    const fileInput = screen.getByLabelText(/select ada file/i)
    const submitButton = screen.getByRole('button', { name: /convert/i })
    
    await user.upload(fileInput, file)
    await user.click(submitButton)
    
    await waitFor(() => {
      expect(mockOnUpload).toHaveBeenCalledWith(file)
    })
  })

  it('should reject non-Ada files', async () => {
    const user = userEvent.setup()
    render(<FileUpload onUpload={mockOnUpload} />)
    
    const file = new File(['console.log("test")'], 'test.js', { type: 'application/javascript' })
    const fileInput = screen.getByLabelText(/select ada file/i) as HTMLInputElement
    
    await user.upload(fileInput, file)
    
    await waitFor(() => {
      expect(fileInput.value).toBe('')
    })
    expect(mockOnUpload).not.toHaveBeenCalled()
  })

  it('should show error when no file is selected', async () => {
    const user = userEvent.setup()
    render(<FileUpload onUpload={mockOnUpload} />)
    
    const submitButton = screen.getByRole('button', { name: /convert/i })
    await user.click(submitButton)
    
    expect(screen.getByText(/please select a file/i)).toBeInTheDocument()
    expect(mockOnUpload).not.toHaveBeenCalled()
  })

  it('should disable submit button while loading', () => {
    render(<FileUpload onUpload={mockOnUpload} isLoading={true} />)
    
    const submitButton = screen.getByRole('button', { name: /converting/i })
    expect(submitButton).toBeDisabled()
  })

  it('should clear file selection after successful upload', async () => {
    const user = userEvent.setup()
    render(<FileUpload onUpload={mockOnUpload} />)
    
    const file = new File(['with Ada.Text_IO;'], 'test.adb', { type: 'text/plain' })
    const fileInput = screen.getByLabelText(/select ada file/i) as HTMLInputElement
    const submitButton = screen.getByRole('button', { name: /convert/i })
    
    await user.upload(fileInput, file)
    await user.click(submitButton)
    
    await waitFor(() => {
      expect(fileInput.value).toBe('')
    })
  })
})