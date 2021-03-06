import os
import shutil


class GenericCCHooks(object):
    """
    通用 CookieCutter Hooks
    file_path_list: 定义待删除的文件路径
    dir_path_list: 定义待删除的文件夹路径
    """

    file_path_list = []
    dir_path_list = []

    def __init__(self, removable):
        self.removable = removable

    def __call__(self, *args, **kwargs):
        if self.removable.lower() == 'n':
            for dir_path in self.dir_path_list:
                if os.path.exists(dir_path):
                    shutil.rmtree(dir_path)

            for file_name in self.file_path_list:
                if os.path.exists(file_name):
                    os.remove(file_name)


class CeleryCCH(GenericCCHooks):
    file_path_list = [
        "{{cookiecutter.project_name}}/celery.py",
    ]


if __name__ == "__main__":
    cch_classes = [
        CeleryCCH('{{cookiecutter.celery}}'),
    ]

    for cch in cch_classes:
        cch()
