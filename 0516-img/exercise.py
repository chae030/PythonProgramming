import os
import pathlib
import tkinter as tk

import PIL
import PIL.ImageTk

# please work on this file
# 이 파일을 수정하여 제출하시오

def get_image_path(project_folder: pathlib.Path) -> pathlib.Path:
    """
    Get the path to the image file.
    Assume `project_folder` is the location of this script.
    이미지 파일의 경로를 생성합니다.
    `project_folder` 는 이 스크립트가 포함된 폴더로 가정하세요.

    For example, if the image file is "sample.png", replace `pass` below with following code.
    예를 들어, 이미지 파일이 "sample.png"인 경우, 아래의 `pass`를 다음 코드로 변경하세요.

    ```python
    return project_folder / "sample.png"
    ```
    """
    jpg_path = project_folder / "sample.jpg"
    if jpg_path.exists():
        return jpg_path

    # sample.jpg가 없으면 sample.png 로 계속 진행
    return project_folder / "sample.png"


def show_image(label: tk.Label, image_path: pathlib.Path) -> None:
    """
    Show the image in a Tkinter window.
    Tkinter 창에 이미지를 보여줍니다.

    Show the image in the label.
    If the image file does not exist, show an error message in the label.
    이미지 파일을 레이블에 표시합니다.
    이미지 파일이 존재하지 않으면 레이블에 오류 메시지를 표시합니다.

    Following method of `image_path` will return `True` if the file exists.
    `image_path`의 다음 메서드는 파일이 존재하면 `True`를 반환합니다.

    ```python
    image_path.exists()
    ```
    """
    if not image_path.exists():
        label.config(text=f"Error: {image_path.name} not found", image='')
        return

    # PIL.Image.open 대신, PIL.ImageTk.PhotoImage에 바로 파일을 넘겨서 처리
    photo = PIL.ImageTk.PhotoImage(file=image_path)
    label.config(image=photo, text='')
    # 가비지 컬렉션 방지를 위해 참조 저장
    label.image = photo