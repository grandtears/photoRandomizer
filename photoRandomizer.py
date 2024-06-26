import os
import random
import shutil

# 写真が入っているフォルダのパス
photoFolder = "path/to/your/photo/folder"

# 写真を振り分ける16個のフォルダを作成
for i in range(1, 17):
    os.makedirs(f"{photoFolder}/folder_{i}", exist_ok=True)

# 写真ファイルのリストを取得
photoFiles = [f for f in os.listdir(photoFolder) if f.endswith((".jpg", ".jpeg", ".png"))]

# 写真ファイルをランダムにシャッフル
random.shuffle(photoFiles)

# 写真ファイルを16個のフォルダに均等に振り分ける
folderIndex = 0
for i, photoFile in enumerate(photoFiles):
    folderNumber = (i % 16) + 1
    srcPath = f"{photoFolder}/{photoFile}"
    dstPath = f"{photoFolder}/folder_{folderNumber}/{photoFile}"
    shutil.move(srcPath, dstPath)
