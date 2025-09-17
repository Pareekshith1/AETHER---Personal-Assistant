from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
from dotenv import load_dotenv


def BootMode(content):

    undercover = "Kill_Switch"
    normal = "Pareekshith"
    professional = "Boss"

    boot_mode = normal

    load_dotenv()

    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY")
    )

    if "undercover" in content.lower() or "anonymous" in content.lower():

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Hello {undercover}, What are we upto today ?",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        boot_mode = undercover

        play(bot_command)

    elif "professional" in content.lower() or "private" in content.lower():

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Hello {professional}, What's our plan for today?",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)

        boot_mode = professional

    elif "normal" in content.lower() or "casual" in content.lower():

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Hello {normal}, what's up how can i help you today ?",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)

    else:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"No Boot Mode Found. Loading default mode. Hello {normal}, How can i help you ?",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)

    return boot_mode
