# begin sample.py

# This file is to show how we can use the functions defined in exercise.py
# 이 파일은 exercise.py에 정의된 함수를 어떻게 사용할 수 있는지 보여주기 위한 것입니다.
# This file is not to be evaluated.
# 이 파일은 평가되지 않습니다.

import pathlib
import tkinter as tk

from typing import Callable


# Import the module containing the functions
# 학생이 작성한 exercise.py 모듈을 import
import exercise


def get_proj_folder() -> pathlib.Path:
    """
    Get the folder containing this script.
    해당 스크립트 파일의 폴더를 반환합니다.
    """
    file_path = pathlib.Path(__file__).resolve()

    # The folder containing this script.
    # 이 스크립트가 포함된 폴더입니다.
    proj_folder = file_path.parent.resolve()

    assert proj_folder.exists(), f"Error: {str(proj_folder)} not found"
    assert proj_folder.is_dir(), f"Error: {str(proj_folder)} is not a directory"

    return proj_folder


def get_label(root:tk.Tk, default_text:str='', pady:int=10) -> tk.Label:
    # Create a label for the image or error message
    # 이미지 또는 오류 메시지를 위한 레이블을 생성합니다.

    # Set as a global variable for testing purposes
    # 테스트 목적으로 전역 변수로 설정합니다.
    # This is not a good practice, but it is done here for simplicity.
    # 이것은 바람직한 방법이 아니지만, 테스트를 단순하게 만들기 위해 이렇게 했습니다.
    global image_label

    image_label = tk.Label(root, text=default_text)
    image_label.pack(pady=pady)
    return image_label


def get_button(root:tk.Tk, text:str, handler:Callable) -> tk.Button:
    # Create a button to show the image
    # 이미지를 보여주는 버튼을 생성합니다.

    # Set as a global variable for testing purposes
    # 테스트 목적으로 전역 변수로 설정합니다.
    # This is not a good practice, but it is done here for simplicity.
    # 이것은 바람직한 방법이 아니지만, 테스트를 단순하게 만들기 위해 이렇게 했습니다.
    global button

    button = tk.Button(
        root,
        text=text,
        command=handler
    )
    button.pack(pady=10)
    return button


def main():
    # Create the Tkinter window
    # Tkinter 창을 생성합니다.
    root = tk.Tk()
    root.title("Show Image App")

    # Get the image path.
    # 이미지 경로를 구합니다.
    image_path = exercise.get_image_path(get_proj_folder())
    assert image_path.exists(), f"Error: {image_path.relative_to(get_proj_folder())} not found"
    assert image_path.is_file(), f"Error: {image_path.relative_to(get_proj_folder())} is not a file"
    assert image_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif'], f"Error: {image_path.relative_to(get_proj_folder())} is not a valid image file"

    # Create a label for the image or error message
    # 이미지 또는 오류 메시지를 위한 레이블을 생성합니다.
    image_label = get_label(
        root,
        default_text="Click the button to show the image"
    )

    def show_image_handler():
        # Show the image in the label
        # 레이블에 이미지를 보여줍니다.
        exercise.show_image(image_label, image_path)

    # Create a button to show the image
    # 이미지를 보여주는 버튼을 생성합니다.
    button = get_button(
        root,
        text="Show Image",
        handler=show_image_handler
    )

    # Run the application
    # 애플리케이션을 실행합니다.
    root.mainloop()


if __name__ == "__main__":
    # Lines below are executed only when this file is run directly
    # 이 파일이 직접 실행될 때만 아래의 코드가 실행됩니다.
    # When this file is imported, the lines below are not executed.
    # 이 파일이 import될 때는 아래의 코드가 실행되지 않습니다.
    main()

# end sample.py
