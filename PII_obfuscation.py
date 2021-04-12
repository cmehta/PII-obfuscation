from presidio_analyzer import AnalyzerEngine, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import AnonymizerConfig


def analyze(text):
    analyzer = AnalyzerEngine()
    analyzer_results = analyzer.analyze(text=text, language='en')
    return analyzer_results

def obfuscate(text):
    analyzer_results = analyze(text)
    anonymizer = AnonymizerEngine()
    anonymized_results = anonymizer.anonymize(
        text=text,
        analyzer_results=analyzer_results,
        anonymizers_config={"DEFAULT": AnonymizerConfig("replace", {"new_value": "<ANONYMIZED>"}),
                            "PHONE_NUMBER": AnonymizerConfig("mask",
                                                             {"type": "mask", "masking_char": "*", "chars_to_mask": 12,
                                                              "from_end": True}),
                            }
    )
    output = anonymized_results
    return output


if __name__== '__main__':
    text_to_anonymize = "please cancel my credit card effective September 19th. My name is Kurt and my credit card \
    number is 4095-2609-9393-4932. My email is kurt.h3@brillio.com and I live in Seattle. Please call me on 2179795382."
    analysis = analyze(text_to_anonymize)
    print(analysis)
    output = obfuscate(text_to_anonymize)
    print(output.text)