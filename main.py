from parsers.VkParser import VkParse
import sys


if __name__ == "__main__":
    if len(sys.argv) == 4:
        vk = VkParse()
        vk.parse()
    else:
        if len(sys.argv) < 4:
            print("Ошибка. Слишком мало параметров.")
            sys.exit(1)

        if len(sys.argv) > 4:
            print("Ошибка. Слишком много параметров.")
            sys.exit(1)

"""
Запускается через консоль в виде python main.py login password access_token
"""
 
