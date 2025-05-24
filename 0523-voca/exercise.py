import pathlib

# please work on this file
# 이 파일을 수정하여 제출하시오

def file_to_dict(word_file_path:pathlib.Path, separator:str):
    """
    Read the word file and return a `dict` of words vs meanings.
    단어 파일을 읽어들여 단어와 뜻을 담은 `dict`를 반환합니다.

    + `word_file_path` is `pathlib.Path` to the word file
    `word_file_path` 은 단어 파일을 가리키는 `pathlib.Path` 입니다.

    Please use `.read_text()` method to read the content.
    `.read_text()` 로 내용을 읽을 수 있습니다.

    + First line is the header. So we will skip it.
    첫 행은 머릿글입니다. 그러니까 건너뜁시다.

    + `.splitlines()` method will return a list of `str`s.
    `.splitlines()` method 는 `str`의 list 를 반환할 것입니다.

    + separator separates word vs meaning.
    separator 는 단어와 뜻을 구분하는 문자입니다.

    Please use with `.split()` method to split the line.
    `.split()` 메소드와 사용 바랍니다.

    """
    


# All executable code in this file must be inside functions.
# 이 파일의 모든 실행 가능한 코드는 함수 안에 있어야 합니다.
