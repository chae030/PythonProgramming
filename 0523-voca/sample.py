# begin sample.py
# This file is to show how we can use the functions defined in exercise.py
# 이 파일은 exercise.py에 정의된 함수를 어떻게 사용할 수 있는지 보여주기 위한 것입니다.
# This file is not to be evaluated.
# 이 파일은 평가되지 않습니다.

import pathlib
import random
import sys

from typing import List


def this_file():
    """
    Returns the path of this script file.
    이 스크립트 파일의 경로를 반환합니다.
    """
    return pathlib.Path(__file__)


def project_folder():
    """
    Returns the path of the folder containing this script file.
    이 스크립트파일을 담고 있는 폴더의 경로를 반환합니다.
    """
    return this_file().parent.resolve()


# Add the project folder to the system path to import the exercise module
# 같은 폴더에 위치하고 있는 exercise.py 을 import하기 위해 sys.path에 추가합니다.
sys.path.insert(
    0,
    str(project_folder())
)


# Import the module containing the functions
# 학생이 작성한 exercise.py 모듈을 import
import exercise


# Initialize the random number generator
# (유사) 난수 발생기를 초기화
random.seed()


def main(argv:List[str]):
    if len(argv) > 1:
        # If the script is run with a command line argument, use it as the word file
        # 스크립트가 실행될 때 명령행 인수가 있으면 단어 파일로 사용합니다.
        word_file = pathlib.Path(argv[1])
    else:
        # Otherwise, use a default word file
        # 그렇지 않으면 기본 단어 파일을 사용합니다.
        word_file = project_folder() / "words.txt"
    # end if

    # Read the word file
    # 단어 파일을 읽어들입니다.
    word_dict = exercise.file_to_dict(word_file, separator='\t')

    # Practice the worlds
    # 단어를 연습합니다.
    n = 5

    word_list = list(word_dict.keys())
    random.shuffle(word_list)

    for attempt, word in enumerate(word_list[:n]):
        print(f"Attempt {attempt + 1}/{n}:")
        print(f"Word: {word}")
        input('Press Enter to continue...')
        print(f"Meaning: {word_dict[word]}")
    # end for
# end main()


if __name__ == "__main__":
    # Lines below are executed only when this file is run directly
    # 이 파일이 직접 실행될 때만 아래의 코드가 실행됩니다.
    # When this file is imported, the lines below are not executed.
    # 이 파일이 import될 때는 아래의 코드가 실행되지 않습니다.
    main(sys.argv)

# end sample.py
