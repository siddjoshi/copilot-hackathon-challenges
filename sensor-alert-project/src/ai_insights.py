import random
from typing import List, Dict, Any

try:
    import transformers
    import torch
except ImportError:
    print("Please install transformers and torch: pip install transformers torch")
    transformers = None


class AIInsightsGenerator:
    """
    Generates AI-powered insights for sensor anomalies using a local generative model.
    
    Utilizes a lightweight generative AI model to provide context-aware recommendations.
    """

    def __init__(self, model_name: str = "distilgpt2"):
        """
        Initialize the generative AI model.
        
        Args:
            model_name (str): Name of the pre-trained model to use
        """
        if transformers is None:
            raise ImportError("Transformers library is not installed")
        
        try:
            # Load tokenizer and model
            self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
            self.model = transformers.AutoModelForCausalLM.from_pretrained(model_name)
            
            # Ensure pad token is set
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
        
        except Exception as e:
            print(f"Error initializing AI model: {e}")
            raise

    def generate_insights(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate AI insights for detected sensor alerts.
        
        Args:
            alerts (List[Dict[str, Any]]): List of detected sensor alerts
        
        Returns:
            Dict[str, Any]: AI-generated insights and recommendations
        """
        if not alerts:
            return {
                'summary': 'No significant anomalies detected.',
                'recommendations': ['Continue routine monitoring']
            }
        
        # Create a structured prompt for the AI with customized instructions
        prompt = self._create_prompt(alerts)
        
        try:
            # Prepare input for generation
            input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
            
            # Configure generation parameters
            generation_config = {
                'max_new_tokens': 150,  # More flexible token generation
                'do_sample': True,      # Enable sampling for more creative output
                'temperature': 0.7,     # Moderate creativity
                'top_k': 50,            # Sample from top 50 tokens
                'top_p': 0.95,          # Nucleus sampling
            }
            
            # Generate response
            outputs = self.model.generate(
                input_ids, 
                **generation_config
            )
            
            # Decode the generated text
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Parse insights from generated text
            return self._parse_insights(generated_text, alerts)
        
        except Exception as e:
            print(f"AI insight generation error: {e}")
            return self._fallback_insights(alerts)

    def _determine_report_type(self, alerts: List[Dict[str, Any]]) -> str:
        """
        Determine the report type based on the severity of the alerts.
        
        Returns:
            str: 'extreme', 'moderate', or 'sample'
        """
        severity_scores = []
        max_severity = 0
        for alert in alerts:
             for alert in alerts:
                if 'value' in alert and 'threshold' in alert and isinstance(alert['threshold'], (int, float)) and alert['threshold'] != 0:
                    ratio = abs(alert['value'] - alert['threshold']) / abs(alert['threshold'])
                    severity_scores.append(ratio)
                    max_severity = max(max_severity, ratio)
        if max_severity >= 0.8:
            return 'extreme'            
        if severity_scores:
            avg_severity = sum(severity_scores) / len(severity_scores)
            if avg_severity >= 0.5:
                return 'extreme'
            elif avg_severity >= 0.2:
                return 'moderate'
            else:
                return 'sample'
        else:
            # If no threshold alerts exist, but there are rapid change alerts, consider them moderate.
            if any('value_change' in alert for alert in alerts):
                return 'moderate'
            return 'sample'

    def _create_prompt(self, alerts: List[Dict[str, Any]]) -> str:
        """
        Create a structured prompt for the generative model.
        
        Args:
            alerts (List[Dict[str, Any]]): List of detected sensor alerts
        
        Returns:
            str: Formatted prompt for AI generation
        """
        report_type = self._determine_report_type(alerts)
        
        # Summarize alerts with detailed information for threshold alerts
        threshold_alerts = [alert for alert in alerts if 'value' in alert]
        alert_summary = "\n".join([
            f"Sensor {alert.get('sensor_id', 'Unknown')} ({alert.get('type', 'Unknown type')}) reported value {alert.get('value', 'N/A')} at {alert.get('timestamp', 'Unknown time')}. This exceeds the threshold of {alert.get('threshold', 'N/A')}."
            for alert in threshold_alerts
        ])
        
        # Summarize rapid change alerts
        rapid_alerts = [alert for alert in alerts if 'value_change' in alert]
        rapid_summary = "\n".join([
            f"Sensor {alert.get('sensor_id', 'Unknown')} experienced a rapid change of {alert.get('value_change', 'N/A')} over {alert.get('time_span', 'N/A')} minutes."
            for alert in rapid_alerts
        ])
        
        combined_summary = alert_summary
        if rapid_summary:
            combined_summary += "\n" + rapid_summary
        
        # Customize analysis instructions based on report type
        if report_type == 'extreme':
            analysis_instruction = (
                "This is an extreme anomaly scenario. Urgent emergency measures are required. "
                "Provide a comprehensive analysis focusing on potential catastrophic failures, immediate system shutdown recommendations, "
                "and strategies to prevent cascading risks."
            )
        elif report_type == 'moderate':
            analysis_instruction = (
                "This scenario shows moderate deviations from normal sensor readings. Provide a detailed analysis with recommendations for immediate maintenance, "
                "calibration suggestions, and monitoring strategies to prevent escalation."
            )
        elif report_type == 'sample':
            analysis_instruction = (
                "This sample indicates minor deviations that do not appear critical. Provide an analysis with suggestions for ongoing monitoring, "
                "sensor calibration, and gradual improvement measures."
            )
        else:
            analysis_instruction = (
                "Provide a detailed analysis of the sensor alerts, including potential root causes, immediate actions, and long-term recommendations."
            )
        
        prompt = f"""Analyze the following industrial sensor alerts and provide comprehensive insights:

Detected Anomalies:
{combined_summary}

{analysis_instruction}

Detailed technical analysis:"""
        return prompt

    def _parse_insights(self, generated_text: str, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Parse the AI-generated text into structured insights.
        
        Args:
            generated_text (str): Text generated by the AI model
            alerts (List[Dict[str, Any]]): Original list of alerts
        
        Returns:
            Dict[str, Any]: Structured insights
        """
        insights = {
            'summary': generated_text[:500],  # First 500 characters as summary
            'recommendations': [],
            'root_causes': [],
            'full_text': generated_text
        }
        
        # Extract recommendations and root causes from text
        sections = generated_text.split('\n\n')
        
        for section in sections:
            if 'recommended action' in section.lower():
                recommendations = [
                    line.strip() for line in section.split('\n') 
                    if line.strip() and any(keyword in line.lower() for keyword in ['should', 'must', 'recommended', 'advise'])
                ]
                insights['recommendations'] = recommendations[:5]
            
            if 'root cause' in section.lower():
                root_causes = [
                    line.strip() for line in section.split('\n') 
                    if line.strip() and any(keyword in line.lower() for keyword in ['may be', 'could be', 'likely'])
                ]
                insights['root_causes'] = root_causes[:3]
        
        # Fallback if no specific insights found
        if not insights['recommendations']:
            insights['recommendations'] = self._generate_generic_recommendations(alerts)
        
        return insights

    @staticmethod
    def _generate_generic_recommendations(alerts: List[Dict[str, Any]]) -> List[str]:
        """
        Generate generic recommendations based on alert types.
        
        Args:
            alerts (List[Dict[str, Any]]): List of detected alerts
        
        Returns:
            List[str]: Generic recommendations
        """
        alert_types = {alert.get('type', '').split('_')[1] for alert in alerts if '_' in alert.get('type', '')}
        
        base_recommendations = [
            "Conduct comprehensive system diagnostics",
            "Review recent maintenance logs",
            "Inspect sensor calibration and positioning"
        ]
        
        type_specific_recommendations = {
            'temperature': [
                "Check cooling system and thermal management",
                "Verify environmental temperature controls"
            ],
            'pressure': [
                "Inspect pressure regulation mechanisms",
                "Check for potential leaks or blockages"
            ],
            'vibration': [
                "Check mechanical alignment and bearing conditions",
                "Perform vibration analysis and balance equipment"
            ]
        }
        
        for sensor_type in alert_types:
            base_recommendations.extend(
                type_specific_recommendations.get(sensor_type, [])
            )
        
        return list(dict.fromkeys(base_recommendations))[:5]

    def _fallback_insights(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Provide fallback insights when AI generation fails.
        
        Args:
            alerts (List[Dict[str, Any]]): List of detected alerts
        
        Returns:
            Dict[str, Any]: Fallback insights dictionary
        """
        return {
            'summary': 'Unable to generate detailed AI insights. Providing generic analysis.',
            'recommendations': self._generate_generic_recommendations(alerts),
            'root_causes': [],
            'full_text': 'Fallback insights generated due to AI generation limitations.'
        }
