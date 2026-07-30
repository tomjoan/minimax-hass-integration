<!-- markdownlint-disable first-line-heading -->
<!-- markdownlint-disable no-inline-html -->

<img src="https://play-lh.googleusercontent.com/hsPVehKUDPBS1LiaAkitNSmZtVNjb5-zbnlhHuNid42l5RMWWVEEiHqF5vSawdNK6ro"
     alt="MiniMax icon"
     width="35%"
     align="right"
     style="float: right; margin: 10px 0px 20px 20px;" />


# MiniMax Home Assistant Integration

Provides conversation, text-to-speech (TTS), and speech-to-text (STT) capabilities powered by MiniMax AI.

## Features

- **Conversation Agent**: Natural language conversations with MiniMax AI
- **Text-to-Speech**: High-quality voice synthesis with customizable voices
- **Speech-to-Text**: Audio transcription for voice commands

## Installation

Easiest install is via [HACS](https://hacs.xyz/):

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=tomjoan&repository=minimax-hass-integration&category=integration)

`HACS -> Integrations -> Explore & Add Repositories -> MiniMax`

For manual installation for advanced users, copy `custom_components/minimax` to
your `custom_components` folder in Home Assistant.

## Configuration

After installation:

1. Go to **Configuration > Integrations**
2. Click **Add Integration**
3. Search for **MiniMax**
4. Enter your MiniMax API key

### Subentries

The integration creates three subentries for independent configuration:

- **Conversation**: Configure the AI model and system prompt
- **TTS**: Select voice, speed, pitch, and volume
- **STT**: Configure transcription prompt

## Requirements

- Home Assistant 2025.4.1 or later
- MiniMax API key from [MiniMax Platform](https://platform.minimaxi.com)

## License

MIT License
