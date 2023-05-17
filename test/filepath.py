import os


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    image_path = os.path.join(os.path.dirname(__file__), "media")
    print(image_path)