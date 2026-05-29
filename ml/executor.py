import os
import webbrowser
import urllib.parse
import psutil

#  App aliases
APP_ALIASES = {

    "browser": "chrome",

    "editor": "notepad",

    "calc": "calc",

    "calculator": "calc",

    "files": "explorer",

    "explorer": "explorer",

    "code": "code",

    "vscode": "code",

    "youtube": "youtube"
}

def execute_command(data: dict):

    intent = data.get("intent")

    entities = data.get("entities", {})

    text = data.get("clean_text", "")


    if intent == "web_search":

        platform = entities.get("platform")

        query = entities.get("query", "")

        encoded_query = urllib.parse.quote(query)

        # 🔹 YouTube Search
        if platform == "youtube":

            url = f"https://www.youtube.com/results?search_query={encoded_query}"

            webbrowser.open(url)

            return {
                "status": f"Searching '{query}' on YouTube"
            }

        # 🔹 Google Search
        elif platform == "google":

            url = f"https://www.google.com/search?q={encoded_query}"

            webbrowser.open(url)

            return {
                "status": f"Searching '{query}' on Google"
            }


    elif intent == "automation":

        raw_app = entities.get("app")

        app = None

        if raw_app:

            # 🔹 Use alias if available
            app = APP_ALIASES.get(
                raw_app.lower(),
                raw_app.lower()
            )

            try:

                # 🔹 Open YouTube
                if app == "youtube":

                    webbrowser.open(
                        "https://www.youtube.com"
                    )

                    return {
                        "status": "Opened YouTube"
                    }

                # 🔹 VS Code
                elif app == "code":

                    os.system("code")

                    return {
                        "status": "Opened VS Code"
                    }

                # 🔹 Paint
                elif app == "paint":

                    os.system("start mspaint")

                    return {
                        "status": "Opened Paint"
                    }

                # 🔹 Dynamic App Opening
                else:

                    os.system(f"start {app}")

                    return {
                        "status": f"Opened {raw_app}"
                    }

            except Exception:

                return {
                    "status": f"Could not open {raw_app}"
                }

        #  Screenshot
        elif "screenshot" in text:

            os.system("start ms-screenclip:")

            return {
                "status": "Taking Screenshot"
            }

        #  Show Desktop
        elif "desktop" in text:

            os.system(
                'powershell -command "(New-Object -ComObject Shell.Application).MinimizeAll()"'
            )

            return {
                "status": "Showing Desktop"
            }

        #  Battery
        elif "battery" in text:

            battery = psutil.sensors_battery()

            percent = battery.percent

            return {
                "status": f"Battery is at {percent}%"
            }

        return {
            "status": "Unknown automation command"
        }


    elif intent == "query":

        query = entities.get("query")

        if query:

            webbrowser.open(
                f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            )

            return {
                "status": f"Searching '{query}' on Google"
            }

        return {
            "status": "No query found"
        }

    return {
        "status": "Unknown command"
    }


# TEST
if __name__ == "__main__":

    test_data = {
        "intent": "web_search",
        "entities": {
            "platform": "youtube",
            "query": "Coldplay music"
        },
        "clean_text": "search Coldplay music on youtube"
    }

    print(execute_command(test_data))