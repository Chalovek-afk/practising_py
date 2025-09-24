import os
import datetime
import platform
import pyscreenshot
import pyautogui


def show_and_restore_desktop():
    system = platform.system()
    if system == "Windows":
        pyautogui.hotkey('win', 'd')
    elif system == "Darwin":  #
        pyautogui.hotkey('command', 'option', 'd')
    elif system == "Linux":
        pyautogui.hotkey('win', 'd')
    else:
        print("Неизвестная ОС")


def take_desktop_screenshot(restore=True):
    folder = "desktop_screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/desktop_{timestamp}.png"

    if restore:
        show_and_restore_desktop()

    try:
        print("📸 Делаем скриншот...")
        im = pyscreenshot.grab()
        im.save(filename)
        print(f"Скриншот рабочего стола сохранён: {filename}")
    except Exception as e:
        print(f"Ошибка при скриншоте: {e}")
    finally:
        if restore:
            show_and_restore_desktop()

if __name__ == "__main__":
    take_desktop_screenshot()