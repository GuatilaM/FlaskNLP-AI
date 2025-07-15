from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask('Emotion Detector')

@app.route('/')
def render_index():
    """Renders index template"""

    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotions():
    """Uses emotion detector to process a text and output an emotion analysis"""
    
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_detected = emotion_detection(text_to_analyze)
    
    # catch no input error
    if emotions_detected['dominant_emotion'] is None: 
        return 'Invalid text! Please try again!'

    response = f"""
        For the given statement, the system response is 'anger':
        {emotions_detected['anger']}, 'disgust': {emotions_detected['disgust']},
        'fear': {emotions_detected['fear']}, 'joy': {emotions_detected['joy']}
        and 'sadness': {emotions_detected['sadness']}. The dominant emotion is
        <b>{emotions_detected['dominant_emotion']}</b>.
    """
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
