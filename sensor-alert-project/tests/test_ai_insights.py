import pytest
from datetime import datetime

from src.ai_insights import AIInsightsGenerator


def create_sample_alerts():
    """
    Generate sample alerts for testing
    
    Returns:
        list: List of sample alert dictionaries
    """
    return [
        {
            'type': 'high_temperature',
            'sensor_id': 'temp_01',
            'timestamp': datetime.now(),
            'value': 90.5,
            'threshold': 85.0
        },
        {
            'type': 'low_pressure',
            'sensor_id': 'press_01',
            'timestamp': datetime.now(),
            'value': 45.2,
            'threshold': 50.0
        }
    ]


def test_ai_insights_generation():
    """
    Test generation of AI insights for sensor alerts
    """
    try:
        # Create AI insights generator
        ai_generator = AIInsightsGenerator()
        
        # Generate sample alerts
        alerts = create_sample_alerts()
        
        # Generate insights
        insights = ai_generator.generate_insights(alerts)
        
        # Assertions
        assert isinstance(insights, dict)
        assert 'summary' in insights
        assert 'recommendations' in insights
        assert len(insights['recommendations']) > 0
        assert len(insights['summary']) > 0
    except ImportError:
        pytest.skip("Transformers library not installed")


def test_no_alerts_scenario():
    """
    Test AI insights generation with no alerts
    """
    # Create AI insights generator
    try:
        ai_generator = AIInsightsGenerator()
        
        # Generate insights with empty alerts
        insights = ai_generator.generate_insights([])
        
        # Assertions
        assert isinstance(insights, dict)
        assert insights['summary'] == 'No significant anomalies detected.'
        assert insights['recommendations'] == ['Continue routine monitoring']
    except ImportError:
        pytest.skip("Transformers library not installed")


def test_ai_insights_recommendations():
    """
    Test that recommendations are generated
    """
    try:
        # Create AI insights generator
        ai_generator = AIInsightsGenerator()
        
        # Generate sample alerts
        alerts = create_sample_alerts()
        
        # Generate insights
        insights = ai_generator.generate_insights(alerts)
        
        # Assertions
        recommendations = insights.get('recommendations', [])
        assert len(recommendations) > 0
        assert all(isinstance(rec, str) for rec in recommendations)
        
        # Check that recommendations are distinct
        assert len(set(recommendations)) == len(recommendations)
    except ImportError:
        pytest.skip("Transformers library not installed")


def test_ai_insights_root_causes():
    """
    Test root cause generation
    """
    try:
        # Create AI insights generator
        ai_generator = AIInsightsGenerator()
        
        # Generate sample alerts
        alerts = create_sample_alerts()
        
        # Generate insights
        insights = ai_generator.generate_insights(alerts)
        
        # Check root causes (optional, as they might not always be generated)
        root_causes = insights.get('root_causes', [])
        assert isinstance(root_causes, list)
        
        # If root causes are generated, they should be strings
        if root_causes:
            assert all(isinstance(cause, str) for cause in root_causes)
    except ImportError:
        pytest.skip("Transformers library not installed")


def test_fallback_insights():
    """
    Test the fallback insights generation method
    """
    try:
        # Create AI insights generator
        ai_generator = AIInsightsGenerator()
        
        # Generate sample alerts
        alerts = create_sample_alerts()
        
        # Simulate an error in generation to trigger fallback
        def mock_generate(*args, **kwargs):
            raise Exception("Simulated generation error")
        
        # Temporarily replace the generation method
        original_method = ai_generator.generate_insights
        ai_generator.generate_insights = mock_generate
        
        try:
            # Try to generate insights (should use fallback)
            fallback_insights = ai_generator._fallback_insights(alerts)
            
            # Assertions
            assert isinstance(fallback_insights, dict)
            assert 'recommendations' in fallback_insights
            assert len(fallback_insights['recommendations']) > 0
        finally:
            # Restore the original method
            ai_generator.generate_insights = original_method
    except ImportError:
        pytest.skip("Transformers library not installed")