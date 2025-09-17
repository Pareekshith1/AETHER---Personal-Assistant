import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import sounddevice as sd
import soundfile as sf
import io
from dotenv import load_dotenv
from bot_functionality.boot_mode import BootMode
from text_processing_functions.whitespace_cleaner import SpaceRemover
from bot_functionality.open_applications import LaunchApp

load_dotenv()  #

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


def Start_Aether(duration=5, samplerate=16000, is_awake=True,
                 bot_name="Aether"):
    print("Booting Up... ")
    print("Select Boot Mode.")

    boot_mode = ""
    while True:

        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
        sd.wait()

        buffer = io.BytesIO()
        sf.write(buffer, audio, samplerate, format="WAV")
        buffer.seek(0)

        transcript = elevenlabs.speech_to_text.convert(
            file=buffer,
            model_id="scribe_v1",
            language_code="eng",
            diarize=False
        )

        content = transcript.text.strip()
        print(content)

        if "adios" in content.lower() or "adiós" in content.lower():
            bot_command = elevenlabs.text_to_speech.convert(
                text=f"Ok {boot_mode}, Signing off. Bye",
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                model_id="eleven_multilingual_v2",
                output_format="mp3_44100_128",
            )

            play(bot_command)

            break

        if is_awake:

            if "sleep" in content.lower() or "rest" in content.lower():
                is_awake = False
                bot_command = elevenlabs.text_to_speech.convert(
                    text=f"Ok {boot_mode}, Going to sleep, Call me if you need me.",
                    voice_id="JBFqnCBsd6RMkjVDRZzb",
                    model_id="eleven_multilingual_v2",
                    output_format="mp3_44100_128",
                )

                play(bot_command)

            modes = ["undercover", "anonymous", "professional", "private", "normal", "casual"]
            change_mode = ["change mode", "change boot", "revise boot mode", "swap mode", "boot swap", "boot mode "
                                                                                                       "change",
                           "mode change", "boot change", "personality swap", "boot swap", "change"]
            for i in modes:
                if i in content.lower():
                    boot_mode = BootMode(i)

            for j in change_mode:
                if (SpaceRemover(j) in SpaceRemover(content).lower() and
                        not any(mode in content.lower() for mode in modes)):
                    bot_command = elevenlabs.text_to_speech.convert(
                        text=f"Ok {boot_mode}, Select boot mode for swap please.",
                        voice_id="JBFqnCBsd6RMkjVDRZzb",
                        model_id="eleven_multilingual_v2",
                        output_format="mp3_44100_128",
                    )
                    play(bot_command)

            with open("./TextFileCollection/OpenApplicationTriggerCommands") as f:
                triggers = [line.strip() for line in f.readlines()]

                for trigger in triggers:
                    if SpaceRemover(trigger) in SpaceRemover(content).lower():
                        LaunchApp(trigger, boot_mode)

        else:
            if bot_name.lower() in content.lower() or "wake" in content.lower():
                is_awake = True
                bot_command = elevenlabs.text_to_speech.convert(
                    text=f"I'm awake! How can I help you {boot_mode}?",
                    voice_id="JBFqnCBsd6RMkjVDRZzb",
                    model_id="eleven_multilingual_v2",
                    output_format="mp3_44100_128",
                )
                play(bot_command)


if __name__ == "__main__":
    Start_Aether()
