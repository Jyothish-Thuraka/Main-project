# Virtual Desktop Assistant

A voice-controlled desktop assistant that helps you perform various tasks on your computer using natural language commands.

## Features

- **Voice Recognition**: Listens for voice commands and responds accordingly
- **Hotword Detection**: Activates when hearing trigger words like "Siri", "Amazon", or "open"
- **Web Browsing**: Opens websites by name from your saved contacts
- **Application Control**: Opens and closes applications on your computer
- **YouTube Integration**: Plays videos on YouTube based on your request
- **Spotify Control**: Opens and controls Spotify
- **Contact Management**: Stores and retrieves contact information
- **Communication**:
  - Send WhatsApp messages, make calls, and video calls
  - Send emails to contacts
- **Information Retrieval**: Answers questions using AI-powered chat capabilities
- **Entertainment**: Tells jokes on command
- **Time and Date**: Provides current time and date information

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your database:
   - The application uses SQLite database (Main.db) to store contacts, websites, and email information
   - Make sure the database is properly configured with the required tables

4. Configure your credentials:
   - Update the email password in the config.py file
   - Set up your HugChat cookies in engine/cookies.json

## Usage

1. Run the application:

```bash
python run.py
```

2. The application will start in two modes:
   - Main interface (web-based UI using Eel)
   - Hotword detection (listening for trigger words)

3. Speak commands like:
   - "Open YouTube"
   - "Play [song name] on YouTube"
   - "Tell me a joke"
   - "What's the time?"
   - "Send message to [contact name]"
   - "Call [contact name]"
   - "Send email to [contact name]"
   - Ask any general question for AI-powered responses

## Project Structure

- `run.py`: Main entry point that starts the application
- `main.py`: Core functionality and web interface integration
- `engine/`: Contains the main components of the assistant
  - `features.py`: Implements various assistant features
  - `command.py`: Handles voice commands and responses
  - `config.py`: Configuration settings
  - `help.py`: Helper functions
- `web/`: Web interface files (HTML, CSS, JS)
- `model/`: Contains the AI model for local processing

## Requirements

See `requirements.txt` for a complete list of dependencies.



