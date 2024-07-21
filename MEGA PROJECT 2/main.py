import pyautogui
import time
import pyperclip
import openai
import os

# Function to click at given coordinates
def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Function to select text by dragging from start to end coordinates
def select_text(start_x, start_y, end_x, end_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=1)  # duration can be adjusted
    pyautogui.mouseUp()

# Main execution
def main():
    # Give a little time to switch to the correct window
    time.sleep(3)

    # Step 1: Click on (1243, 1055)
    click_at(1243, 1055)
    time.sleep(0.5)  # Wait a bit for any UI response

    # Step 2: Select text from (673, 131) to (1859, 943)
    select_text(673, 131, 1859, 943)
    time.sleep(0.5)  # Ensure the selection is done

    # Step 3: Copy the selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for the text to be copied to clipboard

    click_at(1450,802)
    # Step 4: Get the copied text from clipboard
    chat_history = pyperclip.paste()

    # Step 5: Store the copied text in a variable and print it
    print(f"Copied Text: {chat_history}")

    client = openai.OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
        )

    response= client.chat.completions.create(
        messages=[
            {
                "role": "You are Mature Balak who talks in hindi and english.You are a coder.You are a very lovely and helpful person.you have to analyze the chat history and genrate a response as from mature balak(message only)",
                "content": f"{chat_history}",
            }
        ],
        model="gpt-3.5-turbo",
        )
    response_text =  response.choices[0].message['content'].strip()
    # Copy the response text to clipboard
    pyperclip.copy(response_text)

    # Step 6: Click on (813, 995)
    click_at(813, 995)
    time.sleep(0.5)  # Wait a bit for any UI response

    # Step 7: Paste the copied text (Ctrl+V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)  # Wait for the text to be pasted

    # Step 8: Click on (1877, 996)
    click_at(1877, 996)
if __name__ == "__main__":
    main()
