import pathlib

# 폴더 안 파일 수 확인
def file_count(root):
    count = 0
    for path in pathlib.Path(root).iterdir():
        if path.is_file():
            count += 1
    return count

if __name__ == "__main__":
    # 데이터 몇개인지 확인
    print("meningioma_mask :", file_count("/root/data/meningioma/mask"))
    print("glioma_mask :", file_count("/root/data/glioma/mask"))
    print("pituitary_mask :", file_count("/root/data/pituitary/mask"))
    print("meningioma :", file_count("/root/data/meningioma/image"))
    print("glioma :", file_count("/root/data/glioma/image"))
    print("pituitary :", file_count("/root/data/pituitary/image"))