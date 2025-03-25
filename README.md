


# Project Bella: Real-Time Holographic Fish Companion

## Overview

**Project Bella** is an innovative initiative to create an interactive holographic fish companion for children in sterile hospital environments. Developed in collaboration with IMAGE et CONCEPT, this project leverages speech recognition, text-to-speech, and video generation to deliver emotionally adaptive interactions via a volumetric holographic device called 'VID'. The system, named Bella, aims to humanize hospital experiences, facilitate communication, and provide emotional support to children.

## Features

- **Speech Interaction**: Converts French speech input to text using Google Speech Recognition.
- **Text-to-Speech**: Provides audio responses with adjustable rate and volume using `pyttsx3`.
- **Video Prompt Generation**: Creates video prompts for Bella, with a fallback to a neutral underwater scene.
- **Conversation Logging**: Saves interactions with timestamps for analysis.
- **Emotion Integration**: Placeholder for future emotion detection to tailor responses (currently unimplemented).

## Installation

### Prerequisites

- Python 3.8+
- Git
- Microphone (for speech input)
- Dependencies listed in `requirements.txt`

### Dependencies

```
speechrecognition>=3.10.0
pyttsx3>=2.90
```

*Note*: Additional dependencies (e.g., for `mainpy.py`) are not specified here; update `requirements.txt` accordingly.

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/[YourUsername]/Project-Bella.git
   cd Project-Bella
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure the following files are present:
   - `mainpy.py`: Custom module for generating responses (not provided here; must be implemented).
   - Microphone setup for speech input.

## Usage

### Running the Application

1. Execute the main script:
   ```
   python bella.py
   ```
   *Note*: Replace `bella.py` with the actual filename of the provided Python script.

2. Speak in French when prompted ("Parlez maintenant..."). Say "au revoir" to exit.
3. The system will:
   - Recognize your speech and convert it to text.
   - Generate a response via `mainpy.py`.
   - Convert the response to speech.
   - Log the conversation to a timestamped file (e.g., `conversation_2025-03-25_12-00-00.txt`).
   - Generate a video prompt (currently a placeholder function).

### Example Interaction

- **Input**: "Bonjour, comment vas-tu?"
- **Output**: (Response from `mainpy.py`, spoken aloud, logged with a video prompt like "Generate a video of a fish saying: 'Je vais bien, merci!' with neutral emotion").

If no speech is recognized, it defaults to: "Generate a video of a neutral fish character in an underwater scene with ambient movement".

## Project Structure

```
Project-Bella/
├── bella.py             # Main script for speech and video interaction
├── mainpy.py            # Custom response generation module (placeholder)
├── requirements.txt     # List of dependencies
├── LICENSE              # MIT License file
└── README.md            # Project documentation
```

## Technical Details

### Code Functionality

- **Speech-to-Text**: Uses `speech_recognition` with Google’s API (French: "fr-FR").
- **Text-to-Speech**: Configured with `pyttsx3` at 170 words/minute and 90% volume.
- **Video Generation**: Placeholder function (`generate_video`) for future integration with models like Cog Video.
- **Emotion Detection**: Placeholder (`detect_child_emotion`) for future development.
- **Fallback Prompt**: "Generate a video of a neutral fish character in an underwater scene with ambient movement" when input fails.

### Research Insights

Based on the technical report:
- **Objective**: Real-time video generation for Bella using open-source (e.g., Cog Video, Pyramid Flow) and commercial APIs (e.g., Synthesia, Runway).
- **Findings**:
  - Commercial APIs: High quality but costly and inflexible.
  - Open-Source Models: Cog Video offers efficiency but lacks real-time speed; Pyramid Flow is resource-heavy.
- **Solution**: A clip-based system with pre-rendered animations, supplemented by Cog Video and Wave2Lip for lip sync.
- **Challenges**: Real-time processing, smooth transitions, adapting human-centric models for a fish character.

## Future Development

### Short-Term Goals
- Implement `detect_child_emotion` for emotional adaptation.
- Integrate real-time video generation with Cog Video or similar.
- Enhance lip synchronization with Wave2Lip.

### Long-Term Vision
- Optimize for hospital communication workflows.
- Expand to educational and therapeutic settings.
- Achieve full real-time video generation with improved infrastructure.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details:

```
MIT License

Copyright (c) 2025 [Likhita Yerra]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

```

