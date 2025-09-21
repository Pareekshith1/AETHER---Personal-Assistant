# AETHER - Personal Assistant Version 1.0
## Project Overview

AETHER v1.0 is a modular personal assistant application written in Python. It responds to text or voice commands, automates routine tasks and integrates with external services via a plugin architecture.

### What is AETHER?  
AETHER acts as a conversational agent:
- Listens for user input (text or speech)  
- Parses intents and entities  
- Executes tasks or queries external APIs  
- Returns responses via text or speech  

### Main Capabilities  
- Scheduling & reminders  
- Information retrieval (weather, news, facts)  
- Task automation (timers, to-do lists)  
- Service integration (calendar, email, smart home)  
- Plugin support for custom extensions  

### Typical Use-Cases  
- “Set a meeting tomorrow at 3 PM and remind me 15 minutes before.”  
- “What’s the weather in New York today?”  
- “Add ‘write report’ to my to-do list.”  
- “Turn off the living room lights at 10 PM.”  

### Getting Started

Clone the repo and install dependencies:

```bash
git clone https://github.com/Pareekshith1/AETHER---Personal-Assistant-.git
cd AETHER---Personal-Assistant-
pip install -r requirements.txt
```

Launch AETHER:

```bash
python main.py
```

Once running, type or speak a command:

```text
User: What’s on my calendar today?
AETHER: You have a team meeting at 2 PM and a dentist appointment at 5 PM.
## Getting Started

This guide walks you through setting up AETHER on a fresh machine—from cloning the repo and installing dependencies to launching the assistant and testing your first voice command.

### Prerequisites  
- Python 3.10 or newer  
- libsndfile (for `soundfile`)  
  - Ubuntu/Debian: `sudo apt-get install libsndfile1`  
  - macOS (Homebrew): `brew install libsndfile`  
- A working microphone and speakers

### 1. Clone the Repository  
```bash
git clone https://github.com/Pareekshith1/AETHER---Personal-Assistant.git
cd AETHER---Personal-Assistant
```

### 2. Create and Activate a Virtual Environment  
```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate.bat     # Windows (PowerShell)
```

### 3. Install Python Dependencies  
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables  
AETHER uses ElevenLabs for text-to-speech. Obtain your API key from https://elevenlabs.io and export it:  
```bash
export ELEVENLABS_API_KEY="your_api_key_here"    # Linux/macOS
set ELEVENLABS_API_KEY="your_api_key_here"       # Windows
```

### 5. Launch AETHER  
Run the main script to start continuous listening:  
```bash
python Aether.py
```
On startup you’ll see:
```
[INFO] Boot mode: normal
[INFO] Listening for commands...
```

### 6. First Voice Interaction  
Speak a simple wake phrase or command, for example:  
- “change mode to casual”  
- “open calculator”  
- “what time is it?”  
AETHER will process your speech, switch modes or execute actions, and reply via TTS.

### 7. Verify Everything Works  
- If you say “change mode to professional,” you should hear “Mode set to professional.”  
- If you ask “shutdown computer,” AETHER will confirm and proceed.

### Troubleshooting  
- Microphone not detected:  
  - Linux: `arecord -l` to list devices  
  - macOS: check System Preferences → Sound → Input  
- `libsndfile` errors: ensure system library is installed (see Prerequisites)  
- `ModuleNotFoundError`: confirm you’re in the virtualenv and rerun `pip install -r requirements.txt`  
- TTS failures: verify `ELEVENLABS_API_KEY` is set and has valid permissions  

Proceed to configuring custom commands and boot modes in the following sections.
## Using AETHER

AETHER runs a continuous voice-activated loop. After startup it waits for a wake word, processes your spoken command, and routes it to the appropriate handler (application launch, mode switch, system control).

### Activation Phrase (Wake Word)

- Default wake word: **“Aether”**  
- Defined in Aether.py as `WAKE_WORD = "aether"`  
- To customize, set `WAKE_WORD` before calling `Start_Aether()`.

Example: change wake word to “hey assistant”  
```python
# Aether.py (top of file)
WAKE_WORD = "hey assistant"

if __name__ == "__main__":
    Start_Aether()
```

### Starting the Assistant

```python
from Aether import Start_Aether

# Begins listening for WAKE_WORD and subsequent commands
if __name__ == "__main__":
    Start_Aether()
```

### Available Command Categories

1. Application Launch  
2. Mode Switching  
3. System Control (shutdown, exit)

#### 1. Application Launch

- Triggers live in `TextFileCollection/OpenApplicationTriggerCommands` (one keyword or phrase per line).  
- Handler: `bot_functionality.open_applications.LaunchApp(app_name: str, boot_mode: str)`  
- Pattern: speak “Aether, open calculator” → AETHER strips wake word, lowercases input, and matches “calculator”.

Example: launch Notepad  
```python
from bot_functionality.open_applications import LaunchApp
from bot_functionality.boot_mode import BootMode

# Suppose current mode is normal
mode = BootMode("start normal mode")
LaunchApp("open notepad", mode)
```

Common triggers:
- calculator → `os.system("calc")`
- notepad → `os.system("notepad")`
- file explorer → `subprocess.Popen("explorer")`
- chrome → `subprocess.Popen("chrome")`

#### 2. Mode Switching

Speak a mode keyword after wake word to update AETHER’s persona.  
Handler: `bot_functionality.boot_mode.BootMode(content: str) → mode_id`

Keywords (case-insensitive):
- Undercover / Anonymous → `"Kill_Switch"`
- Professional / Private → `"Boss"`
- Normal / Casual → `"Pareekshith"` (default)

Example:
```python
from bot_functionality.boot_mode import BootMode

mode = BootMode("activate undercover mode please")
# ElevenLabs TTS plays the undercover greeting
print(mode)  # → "Kill_Switch"
```

#### 3. System Control

AETHER recognizes:
- “shutdown” or “exit” → calls internal shutdown routine and terminates
- “restart” → if implemented, you can add a branch in Aether.py

Example snippet in Aether.py:
```python
if "shutdown" in command_text:
    tts = elevenlabs.text_to_speech.convert(text="Shutting down", ...)
    play(tts)
    sys.exit(0)
```

### Example Voice Session

User: “Aether”  
AETHER: *beep* (listening)  
User: “Open calculator”  
AETHER: *“Opening Calculator for you now”*  
(System launches Windows Calculator)  
User: “Switch to professional mode”  
AETHER: *“Entering professional mode”*  
User: “Open file explorer”  
AETHER: *“Opening File Explorer for you now”*

### Extending and Customizing

- To add a new app trigger, append its keyword to `OpenApplicationTriggerCommands` and add a branch in `LaunchApp`.  
- To change TTS voice/model, edit `voice_id`, `model_id`, and `output_format` parameters in both `LaunchApp` and `BootMode`.  
- Always lowercase and trim user input before routing. For multi-word triggers, use `SpaceRemover` from `text_processing_functions.whitespace_cleaner`.  

This guide covers all interactions after AETHER starts. Use these patterns to automate tasks, personalize responses, and extend AETHER’s command set.
## Extending & Customizing AETHER

AETHER’s modular design lets you add new voice commands, tweak text-processing, or contribute new integrations. This section shows how to:

- Manage and extend “boot modes” in Aether.py  
- Add or modify application-launch commands in `bot_functionality/open_applications.py`  
- Customize the whitespace-cleaning utility in `text_processing_functions/whitespace_cleaner.py`  

### Boot Mode Management

AETHER maintains a set of personality “boot modes” and listens for direct mode keywords or generic swap commands. You can add modes or customize swap triggers in `Aether.py`.

#### Key Code Excerpt

```python
# Inside Start_Aether() when is_awake == True

# 1. Predefined mode names
modes = ["undercover", "anonymous", "professional", "private", "normal", "casual"]

# 2. Normalized swap trigger phrases
change_mode = [
    "change mode", "revise boot mode", "swap mode",
    "boot swap", "mode change", "boot change", "personality swap"
]

# Detect direct mode selection
for mode_name in modes:
    if mode_name in content.lower():
        boot_mode = BootMode(mode_name)  # switch personality

# Detect swap intent without explicit mode
normalized = SpaceRemover(content).lower()
if any(SpaceRemover(cmd) in normalized for cmd in change_mode) \
   and not any(mode in content.lower() for mode in modes):
    prompt = f"Ok {boot_mode}, select boot mode for swap please."
    response = elevenlabs.text_to_speech.convert(
        text=prompt,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )
    play(response)
```

#### Practical Guidance

- To add or remove modes: update the `modes` list and ensure `BootMode` supports new identifiers.  
- To adjust swap triggers: edit `change_mode`. Phrases normalize via `SpaceRemover`—extra spaces or punctuation are ignored.  
- Handle invalid mode names in `BootMode.__init__()` by raising or falling back to a default.  
- Tweak TTS voices or formats by passing different `voice_id`, `model_id`, or `output_format` to `elevenlabs.text_to_speech.convert()`.  
- For multilingual support: extend `modes` with localized keywords and pass a `language_code` to your STT client.

---

### Configuring Application Launch Commands

Voice triggers map to OS-level launches using `LaunchApp(app_name, boot_mode)` in `bot_functionality/open_applications.py`.

#### 1. Trigger Phrase List

- File: `TextFileCollection/OpenApplicationTriggerCommands`  
- One lowercase phrase per line (e.g., `notepad`, `calc`, `google chrome`).

Your NLU passes the matched phrase as `app_name` into `LaunchApp()`.

#### 2. Core Launcher Logic

```python
def LaunchApp(app_name: str, boot_mode: str):
    # Load .env, init TTS client...
    if "notepad" in app_name:
        msg = f"Opening Notepad for you, {boot_mode}"
        play_tts(msg)
        subprocess.Popen("notepad")
    elif "chrome" in app_name:
        msg = f"Launching Chrome, {boot_mode}"
        play_tts(msg)
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    # … other branches …
    else:
        play_tts(f"Sorry {boot_mode}, I don't recognize {app_name}")
```

#### 3. Adding a New Application

To support Spotify:

a. Update trigger file  
```
TextFileCollection/OpenApplicationTriggerCommands
→ append:
spotify
play music
```

b. Extend `LaunchApp` before the fallback branch:

```python
elif "spotify" in app_name or "play music" in app_name:
    msg = f"Opening Spotify for you, {boot_mode}"
    play_tts(msg)
    subprocess.Popen("spotify")  # ensure this command works in PATH
```

c. Notes  
- Use `SpaceRemover("play music")` for multi-word triggers if needed.  
- Order branches from most to least specific to avoid premature matches.  
- Prefer `subprocess.Popen` for non-blocking launches.

---

### SpaceRemover: Remove All Spaces from a String

A simple utility in `text_processing_functions/whitespace_cleaner.py`:

```python
def SpaceRemover(word: str) -> str:
    result = ""
    for ch in word:
        if ch != " ":
            result += ch
    return result
```

#### Usage Example

```python
from text_processing_functions.whitespace_cleaner import SpaceRemover

original = "  Hello   world  "
cleaned = SpaceRemover(original)
print(cleaned)  # Helloworld
```

#### Edge Cases

- Input `""` → `""`  
- No spaces → returns original  
- Only spaces → `""`

#### Alternative Patterns

```python
# Using built-in replace
cleaned = original.replace(" ", "")

# Using generator expression
cleaned = "".join(ch for ch in original if ch != " ")
```

Use `SpaceRemover` for a clear, named function in your processing pipeline.
## License

This project is licensed under the MIT License. You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of AETHER, subject to the following conditions.

### MIT License Terms

```text
MIT License

Copyright (c) 2025 Pareekshith1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  
...
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```

### Implications for Users

- Freedom to run AETHER for any purpose, including commercial applications.  
- Permission to study and adapt the code to your needs.  
- Requirement to include the original copyright  
  and license text in all copies or substantial portions.

### Implications for Contributors

- Your contributions become part of AETHER under the same MIT terms.  
- You grant downstream users the same permissions you received.  
- You retain copyright on your contributions.

### Compliance and Distribution

1. Include the full `LICENSE` file at the root of any release or distribution.  
2. Preserve all copyright notices in source files.  
3. If you redistribute packaged artifacts (e.g., Docker images, wheels), add a notice:

   ```text
   This product includes software licensed under the MIT License.  
   See https://github.com/Pareekshith1/AETHER---Personal-Assistant/LICENSE
   ```

### Adding License Headers to Source Files

Include a short SPDX header in new or modified files to streamline tooling:

```python
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Pareekshith1
```

Place this block at the top of each Python, JavaScript, or configuration file to clearly denote its license.
