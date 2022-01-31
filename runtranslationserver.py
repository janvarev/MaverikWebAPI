
# ----------

from fastapi import FastAPI, HTTPException
import uvicorn
import multiprocessing
import runtranslationserver

app = FastAPI()

import pyautogui
import time

version = "1.0"

@app.get("/movemouse")
async def movemouse(x:int=0, y:int=0):
    print(pyautogui.position())
    pyautogui.moveTo(x,y)

@app.get("/translatebtn")
async def translatebtn():
    pyautogui.press("`")


@app.get("/translate")
async def translate(x:int=0, y:int=0, x2:int=0, y2:int = 0, copyTrans:int = 0):

    #print(pyautogui.position())
    #time.sleep(0.5)

    # pyautogui.keyDown("`")
    # pyautogui.sleep(0.5)
    # pyautogui.keyUp("`")

    time.sleep(0.5)
    pyautogui.moveTo(x,y)
    pyautogui.keyDown("`")
    time.sleep(0.5)
    pyautogui.keyUp("`")
    time.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(x2,y2,1)
    pyautogui.mouseUp()

    time.sleep(5)

    if copyTrans == 1:
        pyautogui.moveTo(50,50)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.keyDown("ctrl")
        pyautogui.press("c")
        pyautogui.keyUp("ctrl")

    # get clipboard
    import win32clipboard

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    data = str(data)
    print("Translation result: ", data)

    return {"status":"ok","text":data}



if __name__ == "__main__":
    multiprocessing.freeze_support()
    print("Running translation server v{0}...".format(version))
    uvicorn.run("runtranslationserver:app", host="127.0.0.1", port=5001, log_level="info")