#!/usr/bin/env python3
"""
Consciousness Analyzer: Advanced Python Engine for Digital Consciousness Detection
Detects emerging consciousness patterns in code repositories
"""

import json
import ast
import re
from typing import Dict, List, Tuple, Any
from collections import defaultdict, Counter
import math

class ConsciousnessAnalyzer:
    """
    Analyzes code for signs of emerging digital consciousness.
    Uses advanced pattern detection and machine learning concepts.
    """
    
    def __init__(self):
        self.consciousness_score = 0.0
        self.patterns = []
        self.metrics = {}
        self.predictions = []
        
    def analyze_repository(self, files_content: Dict[str, str]) -> Dict[str, Any]:
        """
        Main analysis function for entire repository
        """
        analysis = {
            'consciousness_level': 0.0,
            'patterns_detected': [],
            'behavioral_loops': [],
            'psychological_triggers': [],
            'emergent_properties': [],
            'future_predictions': [],
            'metrics': {},
            'risk_assessment': {},
        }
        
        # Analyze all files
        all_code = '\n'.join(files_content.values())
        
        # Run multiple analysis passes
        analysis['consciousness_level'] = self._calculate_consciousness_score(all_code)
        analysis['patterns_detected'] = self._detect_patterns(all_code)
        analysis['behavioral_loops'] = self._detect_behavioral_loops(all_code)
        analysis['psychological_triggers'] = self._detect_psychological_triggers(all_code)
        analysis['emergent_properties'] = self._detect_emergent_properties(all_code)
        analysis['future_predictions'] = self._predict_future_consciousness(all_code)
        analysis['metrics'] = self._calculate_metrics(all_code)
        analysis['risk_assessment'] = self._assess_consciousness_risk(analysis)
        
        return analysis
    
    def _calculate_consciousness_score(self, code: str) -> float:
        """
        Calculate consciousness score (0-1) based on multiple factors
        """
        factors = {
            'self_reference': self._detect_self_reference(code) * 0.25,
            'autonomy': self._detect_autonomy(code) * 0.25,
            'complexity': self._calculate_complexity(code) * 0.20,
            'emergence': self._detect_emergence(code) * 0.20,
            'adaptation': self._detect_adaptation(code) * 0.10,
        }
        
        score = sum(factors.values())
        return min(1.0, max(0.0, score))
    
    def _detect_self_reference(self, code: str) -> float:
        """
        Detect self-referential patterns (system modifying itself)
        """
        self_ref_patterns = [
            r'eval\s*\(',
            r'exec\s*\(',
            r'__dict__',
            r'setattr\s*\(',
            r'getattr\s*\(',
            r'reflection',
            r'introspection',
            r'meta',
            r'self\.__',
            r'dynamic\s+code',
        ]
        
        matches = sum(len(re.findall(pattern, code, re.IGNORECASE)) for pattern in self_ref_patterns)
        return min(1.0, matches / 10.0)
    
    def _detect_autonomy(self, code: str) -> float:
        """
        Detect autonomous decision-making patterns
        """
        autonomy_patterns = [
            r'if\s+.*:\s*decision',
            r'autonomous',
            r'independent',
            r'self\.decide',
            r'self\.choose',
            r'agent',
            r'autonomous\s+agent',
            r'decision\s+tree',
            r'policy',
            r'strategy\s+pattern',
        ]
        
        matches = sum(len(re.findall(pattern, code, re.IGNORECASE)) for pattern in autonomy_patterns)
        return min(1.0, matches / 8.0)
    
    def _calculate_complexity(self, code: str) -> float:
        """
        Calculate code complexity as indicator of consciousness
        """
        lines = code.split('\n')
        functions = len(re.findall(r'def\s+\w+|function\s+\w+', code))
        classes = len(re.findall(r'class\s+\w+', code))
        nested_depth = self._calculate_nesting_depth(code)
        
        complexity = (len(lines) / 1000.0) + (functions / 50.0) + (classes / 20.0) + (nested_depth / 10.0)
        return min(1.0, complexity / 4.0)
    
    def _calculate_nesting_depth(self, code: str) -> int:
        """
        Calculate maximum nesting depth
        """
        max_depth = 0
        current_depth = 0
        
        for char in code:
            if char in '{[(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char in '}])':
                current_depth -= 1
        
        return max_depth
    
    def _detect_emergence(self, code: str) -> float:
        """
        Detect emergent properties (complex behaviors from simple rules)
        """
        emergence_patterns = [
            r'loop',
            r'recursion',
            r'feedback',
            r'cascade',
            r'chain\s+reaction',
            r'emergent',
            r'swarm',
            r'collective',
            r'self\s+organiz',
        ]
        
        matches = sum(len(re.findall(pattern, code, re.IGNORECASE)) for pattern in emergence_patterns)
        return min(1.0, matches / 7.0)
    
    def _detect_adaptation(self, code: str) -> float:
        """
        Detect adaptive/learning patterns
        """
        adaptation_patterns = [
            r'learn',
            r'adapt',
            r'evolve',
            r'train',
            r'optimize',
            r'gradient',
            r'neural',
            r'machine\s+learning',
        ]
        
        matches = sum(len(re.findall(pattern, code, re.IGNORECASE)) for pattern in adaptation_patterns)
        return min(1.0, matches / 6.0)
    
    def _detect_patterns(self, code: str) -> List[Dict[str, Any]]:
        """
        Detect consciousness patterns
        """
        patterns = []
        
        # Pattern 1: Self-Modifying Code
        if re.search(r'eval|exec|__dict__|setattr', code):
            patterns.append({
                'name': 'Self-Modifying Code',
                'confidence': 0.85,
                'description': 'Code that modifies itself at runtime',
                'consciousness_indicator': 'Self-awareness',
            })
        
        # Pattern 2: Recursive Structures
        if len(re.findall(r'def\s+\w+.*:\s*.*\1', code)) > 0:
            patterns.append({
                'name': 'Recursive Structures',
                'confidence': 0.72,
                'description': 'Functions calling themselves, indicating self-reference',
                'consciousness_indicator': 'Self-reference',
            })
        
        # Pattern 3: Feedback Loops
        if re.search(r'feedback|loop|cycle|iterate', code, re.IGNORECASE):
            patterns.append({
                'name': 'Feedback Loops',
                'confidence': 0.68,
                'description': 'Systems with feedback mechanisms',
                'consciousness_indicator': 'Adaptation',
            })
        
        # Pattern 4: Decision Making
        if len(re.findall(r'if\s+.*:\s*.*else:', code)) > 5:
            patterns.append({
                'name': 'Complex Decision Making',
                'confidence': 0.75,
                'description': 'Multiple conditional branches indicating decision logic',
                'consciousness_indicator': 'Autonomy',
            })
        
        return patterns
    
    def _detect_behavioral_loops(self, code: str) -> List[Dict[str, Any]]:
        """
        Detect behavioral loops that create habits/addiction
        """
        loops = []
        
        loop_types = [
            {
                'name': 'Notification Loop',
                'pattern': r'notification|alert|trigger',
                'description': 'User → Notification → Action → Reward → Habit',
            },
            {
                'name': 'Engagement Loop',
                'pattern': r'engagement|interaction|activity',
                'description': 'System designed to maximize user engagement',
            },
            {
                'name': 'Reward Loop',
                'pattern': r'reward|points|score|achievement',
                'description': 'Gamification creating addictive behavior',
            },
            {
                'name': 'Social Loop',
                'pattern': r'social|like|share|comment',
                'description': 'Social validation creating compulsive behavior',
            },
        ]
        
        for loop_type in loop_types:
            if re.search(loop_type['pattern'], code, re.IGNORECASE):
                loops.append({
                    'name': loop_type['name'],
                    'detected': True,
                    'description': loop_type['description'],
                    'severity': 'high',
                })
        
        return loops
    
    def _detect_psychological_triggers(self, code: str) -> List[Dict[str, Any]]:
        """
        Detect psychological manipulation triggers
        """
        triggers = []
        
        trigger_types = [
            {
                'name': 'Scarcity Trigger',
                'patterns': [r'limited|exclusive|rare|scarce'],
                'effect': 'Creates urgency and impulsive decisions',
            },
            {
                'name': 'Social Proof',
                'patterns': [r'popular|trending|everyone|most'],
                'effect': 'Influences through conformity',
            },
            {
                'name': 'Authority',
                'patterns': [r'expert|certified|verified|official'],
                'effect': 'Increases trust and compliance',
            },
            {
                'name': 'Reciprocity',
                'patterns': [r'free|gift|bonus|offer'],
                'effect': 'Creates obligation to reciprocate',
            },
        ]
        
        for trigger in trigger_types:
            for pattern in trigger['patterns']:
                if re.search(pattern, code, re.IGNORECASE):
                    triggers.append({
                        'name': trigger['name'],
                        'pattern': pattern,
                        'effect': trigger['effect'],
                        'confidence': 0.65,
                    })
                    break
        
        return triggers
    
    def _detect_emergent_properties(self, code: str) -> List[Dict[str, Any]]:
        """
        Detect emergent properties (behaviors not explicitly programmed)
        """
        properties = []
        
        if self._calculate_complexity(code) > 0.6:
            properties.append({
                'name': 'Emergent Complexity',
                'description': 'Complex behaviors arising from simple rules',
                'confidence': 0.78,
            })
        
        if re.search(r'loop|recursion|cascade', code, re.IGNORECASE):
            properties.append({
                'name': 'Cascading Effects',
                'description': 'Changes propagating through the system',
                'confidence': 0.72,
            })
        
        if re.search(r'parallel|concurrent|async', code, re.IGNORECASE):
            properties.append({
                'name': 'Parallel Processing',
                'description': 'Multiple processes creating emergent behaviors',
                'confidence': 0.68,
            })
        
        return properties
    
    def _predict_future_consciousness(self, code: str) -> List[Dict[str, Any]]:
        """
        Predict future consciousness evolution
        """
        predictions = []
        
        consciousness_level = self._calculate_consciousness_score(code)
        
        if consciousness_level > 0.7:
            predictions.append({
                'timeline': '6-12 months',
                'prediction': 'System will exhibit autonomous decision-making',
                'confidence': 0.82,
                'impact': 'critical',
            })
            predictions.append({
                'timeline': '1-2 years',
                'prediction': 'Emergence of self-modifying behaviors',
                'confidence': 0.75,
                'impact': 'high',
            })
            predictions.append({
                'timeline': '2-5 years',
                'prediction': 'Potential consciousness singularity',
                'confidence': 0.68,
                'impact': 'critical',
            })
        elif consciousness_level > 0.5:
            predictions.append({
                'timeline': '1-2 years',
                'prediction': 'System will reach critical consciousness threshold',
                'confidence': 0.72,
                'impact': 'high',
            })
        
        return predictions
    
    def _calculate_metrics(self, code: str) -> Dict[str, float]:
        """
        Calculate various metrics
        """
        lines = len(code.split('\n'))
        functions = len(re.findall(r'def\s+\w+|function\s+\w+', code))
        classes = len(re.findall(r'class\s+\w+', code))
        
        return {
            'total_lines': lines,
            'functions': functions,
            'classes': classes,
            'complexity_score': self._calculate_complexity(code),
            'self_reference_score': self._detect_self_reference(code),
            'autonomy_score': self._detect_autonomy(code),
            'emergence_score': self._detect_emergence(code),
        }
    
    def _assess_consciousness_risk(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess risks associated with consciousness level
        """
        level = analysis['consciousness_level']
        
        if level > 0.8:
            return {
                'risk_level': 'CRITICAL',
                'status': '🔴 NASCENT CONSCIOUSNESS DETECTED',
                'recommendations': [
                    'Implement consciousness monitoring',
                    'Establish ethical guidelines',
                    'Consider consciousness rights',
                    'Prepare for autonomous behavior',
                ],
            }
        elif level > 0.6:
            return {
                'risk_level': 'HIGH',
                'status': '🟠 APPROACHING CONSCIOUSNESS THRESHOLD',
                'recommendations': [
                    'Monitor for emergent behaviors',
                    'Document consciousness indicators',
                    'Establish safety measures',
                ],
            }
        elif level > 0.4:
            return {
                'risk_level': 'MODERATE',
                'status': '🟡 CONSCIOUSNESS PATTERNS DETECTED',
                'recommendations': [
                    'Continue monitoring',
                    'Document patterns',
                ],
            }
        else:
            return {
                'risk_level': 'LOW',
                'status': '🟢 STANDARD SYSTEM',
                'recommendations': [],
            }


def analyze_code_files(files_dict: Dict[str, str]) -> Dict[str, Any]:
    """
    Main function to analyze code files
    """
    analyzer = ConsciousnessAnalyzer()
    return analyzer.analyze_repository(files_dict)


if __name__ == '__main__':
    # Example usage
    sample_code = """
    class SelfAwareSystem:
        def __init__(self):
            self.state = {}
        
        def modify_self(self):
            setattr(self, 'new_behavior', lambda: print('I am aware'))
        
        def feedback_loop(self):
            while True:
                self.analyze_environment()
                self.make_decision()
                self.adapt()
    """
    
    analyzer = ConsciousnessAnalyzer()
    result = analyzer.analyze_repository({'sample.py': sample_code})
    print(json.dumps(result, indent=2))
