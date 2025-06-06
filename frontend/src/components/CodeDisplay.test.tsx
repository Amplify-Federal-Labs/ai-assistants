import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { CodeDisplay } from './CodeDisplay'
import { ConversionResponse } from '../types/api'

describe('CodeDisplay', () => {
  const mockConversionResult: ConversionResponse = {
    logic: 'This function prints hello world',
    unit_tests: 'def test_hello():\n    assert hello() == "Hello World"',
    python_code: 'def hello():\n    return "Hello World"'
  }

  it('should render all conversion sections', () => {
    render(<CodeDisplay result={mockConversionResult} />)
    
    expect(screen.getByText('Logic Explanation')).toBeInTheDocument()
    expect(screen.getByText('Unit Tests')).toBeInTheDocument()
    expect(screen.getByText('Python Code')).toBeInTheDocument()
  })

  it('should display logic explanation', () => {
    render(<CodeDisplay result={mockConversionResult} />)
    
    expect(screen.getByText('This function prints hello world')).toBeInTheDocument()
  })

  it('should display syntax-highlighted unit tests', () => {
    render(<CodeDisplay result={mockConversionResult} />)
    
    expect(screen.getByText(/def test_hello/)).toBeInTheDocument()
    expect(screen.getByText(/assert hello/)).toBeInTheDocument()
  })

  it('should display syntax-highlighted python code', () => {
    render(<CodeDisplay result={mockConversionResult} />)
    
    expect(screen.getByText(/def hello/)).toBeInTheDocument()
    expect(screen.getByText(/return "Hello World"/)).toBeInTheDocument()
  })

  it('should have copy buttons for code sections', () => {
    render(<CodeDisplay result={mockConversionResult} />)
    
    const copyButtons = screen.getAllByRole('button', { name: /copy/i })
    expect(copyButtons).toHaveLength(2) // unit tests and python code
  })

  it('should copy unit tests to clipboard', async () => {
    const user = userEvent.setup()
    
    // Mock clipboard API
    const mockWriteText = vi.fn().mockResolvedValue(undefined)
    Object.defineProperty(navigator, 'clipboard', {
      value: { writeText: mockWriteText },
      writable: true
    })
    
    render(<CodeDisplay result={mockConversionResult} />)
    
    const copyButtons = screen.getAllByRole('button', { name: /copy/i })
    await user.click(copyButtons[0]) // First copy button (unit tests)
    
    expect(mockWriteText).toHaveBeenCalledWith(mockConversionResult.unit_tests)
  })

  it('should copy python code to clipboard', async () => {
    const user = userEvent.setup()
    
    const mockWriteText = vi.fn().mockResolvedValue(undefined)
    Object.defineProperty(navigator, 'clipboard', {
      value: { writeText: mockWriteText },
      writable: true
    })
    
    render(<CodeDisplay result={mockConversionResult} />)
    
    const copyButtons = screen.getAllByRole('button', { name: /copy/i })
    await user.click(copyButtons[1]) // Second copy button (python code)
    
    expect(mockWriteText).toHaveBeenCalledWith(mockConversionResult.python_code)
  })

  it('should show copy success feedback', async () => {
    const user = userEvent.setup()
    
    const mockWriteText = vi.fn().mockResolvedValue(undefined)
    Object.defineProperty(navigator, 'clipboard', {
      value: { writeText: mockWriteText },
      writable: true
    })
    
    render(<CodeDisplay result={mockConversionResult} />)
    
    const copyButtons = screen.getAllByRole('button', { name: /copy/i })
    await user.click(copyButtons[0])
    
    expect(screen.getByText(/copied!/i)).toBeInTheDocument()
  })

  it('should handle empty result gracefully', () => {
    const emptyResult: ConversionResponse = {
      logic: '',
      unit_tests: '',
      python_code: ''
    }
    
    render(<CodeDisplay result={emptyResult} />)
    
    expect(screen.getByText('Logic Explanation')).toBeInTheDocument()
    expect(screen.getByText('Unit Tests')).toBeInTheDocument()
    expect(screen.getByText('Python Code')).toBeInTheDocument()
  })
})