from flask import request, jsonify
from app.services.ada_converter import AdaConverter
from app.core.exceptions import FileUploadError, AdaConverterError
import re

# Initialize converter
ada_converter = AdaConverter()


def parse_converter_response(response: str) -> dict:
    """Parse the structured response from AdaConverter into components."""
    # Initialize default values
    logic = ""
    unit_tests = ""
    python_code = ""
    
    # Split by sections using regex
    sections = re.split(r'# (Logic|Unit Test|Python Code)', response)
    
    for i in range(1, len(sections), 2):
        section_name = sections[i]
        section_content = sections[i + 1].strip() if i + 1 < len(sections) else ""
        
        if section_name == "Logic":
            logic = section_content
        elif section_name == "Unit Test":
            unit_tests = section_content
        elif section_name == "Python Code":
            python_code = section_content
    
    return {
        "logic": logic,
        "unit_tests": unit_tests,
        "python_code": python_code
    }


def convert_ada_file():
    """Convert Ada code to Python via REST API using file upload."""
    if 'ada_file' not in request.files:
        return jsonify({"error": "ada_file is required"}), 400
    
    file = request.files['ada_file']
    
    if file.filename == '':
        return jsonify({"error": "ada_file is required"}), 400
    
    try:
        # Read the file content
        ada_code = file.read().decode('utf-8')
        
        if not ada_code.strip():
            return jsonify({"error": "File is empty"}), 400
        
        # Convert using AdaConverter
        converter_response = ada_converter.convert(ada_code)
        
        # Parse the structured response
        parsed_response = parse_converter_response(converter_response)
        
        return jsonify(parsed_response), 200
        
    except UnicodeDecodeError:
        return jsonify({"error": "File must be valid UTF-8 text"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500