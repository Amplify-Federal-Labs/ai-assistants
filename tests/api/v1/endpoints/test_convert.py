import pytest
import json
from unittest.mock import patch




def test_convert_endpoint_file_upload_success(flask_test_client, sample_converter_response, ada_file_upload):
    """Test successful conversion via POST /convert endpoint with file upload."""
    with patch('app.api.v1.endpoints.convert.ada_converter') as mock_converter:
        mock_converter.convert.return_value = sample_converter_response
        
        response = flask_test_client.post('/convert',
                                        data={'ada_file': (ada_file_upload, 'hello.adb')},
                                        content_type='multipart/form-data')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'logic' in data
        assert 'unit_tests' in data
        assert 'python_code' in data


def test_convert_endpoint_missing_file(flask_test_client):
    """Test POST /convert endpoint with missing file."""
    response = flask_test_client.post('/convert',
                                    data={},
                                    content_type='multipart/form-data')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert 'ada_file is required' in data['error']


def test_convert_endpoint_empty_file(flask_test_client):
    """Test POST /convert endpoint with empty file."""
    from io import BytesIO
    empty_file = BytesIO(b'')
    
    response = flask_test_client.post('/convert',
                                    data={'ada_file': (empty_file, 'empty.adb')},
                                    content_type='multipart/form-data')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert 'File is empty' in data['error']