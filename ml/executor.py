import os
import webbrowser

# 🔹 App aliases (smart understanding)
APP_ALIASES = {
    "browser": "chrome",
    "chrome": "chrome",
    "editor": "notepad",
    "notepad": "notepad",
    "calc": "calculator",
    "calculator": "calculator",
    "files": "explorer",
    "explorer": "explorer"
}

def execute_command(data: dict):

    intent = data.get("intent")
    entities = data.get("entities", {})
    text = data.get("clean_text", "")

    # 🔹 AUTOMATION
    if intent == "automation":

        raw_app = entities.get("app")

        app = None
        if raw_app:
            app = APP_ALIASES.get(raw_app.lower())

        # Open Chrome
        if app == "chrome":
            os.system("start chrome")
            return {"status": "Opened Chrome"}

        # Open Notepad
        elif app == "notepad":
            os.system("start notepad")
            return {"status": "Opened Notepad"}

        # Open Calculator
        elif app == "calculator":
            os.system("start calc")
            return {"status": "Opened Calculator"}

        # Open File Explorer
        elif app == "explorer":
            os.system("start explorer")
            return {"status": "Opened File Explorer"}

        # Screenshot
        elif "screenshot" in text:
            os.system("start ms-screenclip:")
            return {"status": "Taking Screenshot"}

        # Show Desktop
        elif "desktop" in text:
            os.system(
                "powershell -command \"(New-Object -ComObject Shell.Application).MinimizeAll()\""
            )
            return {"status": "Showing Desktop"}

        return {"status": "Unknown automation command"}

    # 🔹 QUERY HANDLING
    elif intent == "query":

        query = entities.get("query")

        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return {"status": f"Searching for '{query}' on Google"}

        return {"status": "No query found"}

    return {"status": "Unknown command"}