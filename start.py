import threading

import app
import test_bot

if __name__ == '__main__':
    threading.Thread(target=test_bot).start()
    threading.Thread(target=app).start()
