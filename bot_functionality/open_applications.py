import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from dotenv import load_dotenv
from text_processing_functions.whitespace_cleaner import SpaceRemover
import subprocess


def LaunchApp(app_name, boot_mode):
    load_dotenv()

    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    if "notepad" in app_name or "write" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Notepad for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("notepad")

    elif "calculator" in app_name or "calc" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Calculator for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("calc")

    elif SpaceRemover("file explorer") in SpaceRemover(app_name) or "explorer" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"FileExplorer for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("explorer")

    elif "cmd" in app_name or SpaceRemover("command prompt") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening CommandPrompt for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("start cmd")

    elif "powershell" in app_name or "shell" in app_name or "powerhouse" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening PowerShell for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("start powershell")

    elif "settings" in app_name or "setup" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Settings for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("start ms-settings:")

    elif SpaceRemover("control panel") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening ControlPanel for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        os.system("control")

    elif "code" in app_name or SpaceRemover("vscode") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Visual Studio Code for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("code")

    elif "charm" in app_name or SpaceRemover("pycharm") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening PyCharm for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("pycharm")

    elif "idea" in app_name or SpaceRemover("intellij") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening IntelliJ for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("idea")

    elif "post" in app_name or "postman" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening PostMan for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("postman")

    elif "dock" in app_name or "docker" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Docker Desktop for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("docker")

    elif "heidi" in app_name or SpaceRemover("heidisql") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Heidi SQL for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("heidisql")

    elif "chrome" in app_name or SpaceRemover("google chrome") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Google Chrome for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("chrome")

    elif "edge" in app_name or SpaceRemover("microsoft edge") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Microsoft Edge for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("msedge")

    elif "explorer" in app_name or "file explorer" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening File Explorer for you. Happy Exploring {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("explorer")

    elif "c drive" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening C Drive.",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("explorer C:\\")

    elif "d drive" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening D Drive.",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("explorer D:\\")

    elif "downloads" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Downloads for you.",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("explorer %USERPROFILE%\\Downloads")

    elif "desktop" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Desktop for you.",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("explorer %USERPROFILE%\\Desktop")

    elif "env" in app_name or "variable" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Environment variable panel for you.",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("SystemPropertiesAdvanced")

    elif "task manager" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Task Manager for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("taskmgr")

    elif "regedit" in app_name or SpaceRemover("registry edit") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Registry Edit for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("regedit")

    elif "services" in app_name or SpaceRemover("system services") in SpaceRemover(app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Services for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("services.msc")

    elif "device manager" in app_name or "dev manager" in app_name:

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Opening Device Manager for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("devmgmt.msc")

    elif "system info" in app_name or SpaceRemover("sysinfo") in app_name or SpaceRemover("deviceinfo") in SpaceRemover(
            app_name):

        bot_command = elevenlabs.text_to_speech.convert(
            text=f"Displaying System Info for you {boot_mode}",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        play(bot_command)
        subprocess.Popen("msinfo32")
