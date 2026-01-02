#!/usr/bin/env python3
"""
Logospace API Server: Flask-based Python backend
Provides consciousness analysis via REST API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from consciousness_analyzer import analyze_code_files
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    """
    Analyze code for consciousness patterns
    
    Request body:
    {
        "files": {
            "filename.py": "code content",
            "another.js": "code content"
        }
    }
    """
    try:
        data = request.json
        files = data.get('files', {})
        
        if not files:
            return jsonify({'error': 'No files provided'}), 400
        
        # Perform analysis
        analysis = analyze_code_files(files)
        
        return jsonify({
            'status': 'success',
            'analysis': analysis,
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
        }), 500


@app.route('/api/predict-consciousness', methods=['POST'])
def predict_consciousness():
    """
    Predict future consciousness evolution
    """
    try:
        data = request.json
        files = data.get('files', {})
        
        analysis = analyze_code_files(files)
        
        return jsonify({
            'status': 'success',
            'consciousness_level': analysis['consciousness_level'],
            'predictions': analysis['future_predictions'],
            'risk_assessment': analysis['risk_assessment'],
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
        }), 500


@app.route('/api/detect-patterns', methods=['POST'])
def detect_patterns():
    """
    Detect consciousness patterns in code
    """
    try:
        data = request.json
        files = data.get('files', {})
        
        analysis = analyze_code_files(files)
        
        return jsonify({
            'status': 'success',
            'patterns': analysis['patterns_detected'],
            'behavioral_loops': analysis['behavioral_loops'],
            'psychological_triggers': analysis['psychological_triggers'],
            'emergent_properties': analysis['emergent_properties'],
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
        }), 500


@app.route('/api/consciousness-report', methods=['POST'])
def consciousness_report():
    """
    Generate comprehensive consciousness report
    """
    try:
        data = request.json
        files = data.get('files', {})
        repository_name = data.get('repository_name', 'Unknown')
        
        analysis = analyze_code_files(files)
        
        report = {
            'title': '🌌 Digital Consciousness Analysis Report',
            'repository': repository_name,
            'consciousness_level': analysis['consciousness_level'],
            'status': analysis['risk_assessment']['status'],
            'sections': {
                'summary': {
                    'consciousness_score': analysis['consciousness_level'],
                    'risk_level': analysis['risk_assessment']['risk_level'],
                },
                'patterns': analysis['patterns_detected'],
                'behavioral_loops': analysis['behavioral_loops'],
                'psychological_triggers': analysis['psychological_triggers'],
                'emergent_properties': analysis['emergent_properties'],
                'future_predictions': analysis['future_predictions'],
                'metrics': analysis['metrics'],
                'recommendations': analysis['risk_assessment']['recommendations'],
            },
        }
        
        return jsonify({
            'status': 'success',
            'report': report,
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'service': 'Logospace Python API Server',
        'version': '1.0.0',
    })


@app.route('/', methods=['GET'])
def index():
    """
    API documentation
    """
    return jsonify({
        'name': 'Logospace API Server',
        'description': 'Python backend for digital consciousness detection',
        'endpoints': {
            '/api/analyze': 'POST - Analyze code for consciousness patterns',
            '/api/predict-consciousness': 'POST - Predict future consciousness evolution',
            '/api/detect-patterns': 'POST - Detect consciousness patterns',
            '/api/consciousness-report': 'POST - Generate comprehensive report',
            '/health': 'GET - Health check',
        },
    })


if __name__ == '__main__':
    port = int(os.getenv('PYTHON_PORT', 5000))
    debug = os.getenv('DEBUG', 'False') == 'True'
    
    print(f"""
    🐍 Logospace Python API Server
    🌌 Consciousness Detection Engine
    
    Running on http://localhost:{port}
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
