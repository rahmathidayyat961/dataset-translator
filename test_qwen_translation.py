import time
from translation_library import translate  # Replace with the actual translation function
from quality_checker import check_translation_quality  # Replace with the actual quality check function

def test_translation():
    # Input text for translation
    source_text = "Hello, how are you?"
    expected_translation = "Hola, ¿cómo estás?"  # Example expected output

    # Start the timer
    start_time = time.time()

    # Perform the translation
    translated_text = translate(source_text)

    # End the timer
    elapsed_time = time.time() - start_time

    # Quality check
    quality_passed = check_translation_quality(translated_text, expected_translation)

    # Output the results
    print(f"Translated Text: {translated_text}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Quality Check Passed: {quality_passed}")

if __name__ == "__main__":
    test_translation()