from ml.main_pipeline import full_pipeline
from ml.executor import execute_command

print("\n AI Desktop Assistant Started")
print("Type your command below")
print("Press CTRL + C to quit\n")

while True:

    try:
        text = input("Enter command: ")

        #  Run full ML pipeline
        results = full_pipeline(text)

        print("\n==============================")

        for res in results:

            print(f"\n Classified Intent: {res['intent']}")

            print(f"Extracted Entities: {res['entities']}")

            #  Execute command
            action = execute_command(res)

            print(f"Action Result: {action}")

        print("\n==============================\n")

    except KeyboardInterrupt:

        print("\n\nAssistant Closed")

        break

    except Exception as e:

        print(f"\nError: {e}\n")