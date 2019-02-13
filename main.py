from bots import *


if __name__ == '__main__':
    folder_bot = FolderBot('.')
    dl_bot = DownloadBot()
    dl_bot.start(folder_bot.get_video_file_name())
    folder_bot.start(dl_bot.file_name)
    input('...')
