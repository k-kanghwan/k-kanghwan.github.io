from PIL import Image
import os


# fmt: on
# 1. 이미지 크기 확인 함수
def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"이미지 처리 중 오류 발생: {e}")
        return None, None

# 2. 이미지 리사이즈 함수
def resize_image(image_path, output_path, new_width, new_height):
    try:
        with Image.open(image_path) as img:
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)
            print(f"이미지가 성공적으로 {new_width}x{new_height} 크기로 저장되었습니다.")
    except Exception as e:
        print(f"이미지 처리 중 오류 발생: {e}")

# resize image width = 1.91 : height = 1
def resize_image_191(image_path, output_path, new_width):
    try:
        with Image.open(image_path) as img:
            new_height = int(new_width / 1.91)
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)
            print(f"이미지가 성공적으로 {new_width}x{new_height} 크기로 저장되었습니다.")
    except Exception as e:
        print(f"이미지 처리 중 오류 발생: {e}")

# 3. 이미지 확장자 체크 함수
def check_image_extension(image_path):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    _, ext = os.path.splitext(image_path)
    if ext.lower() in allowed_extensions:
        return True
    else:
        return False

if __name__ == "__main__":
    from pathlib import Path
    
    # 사용 예시
    target_image_path = Path("assets/img/Git-Blog/prompts.png")
    image_name = target_image_path.stem

    # 1. 이미지 크기 확인
    width, height = get_image_size(target_image_path)
    if width and height:
        print(f"이미지 크기: {width}x{height}")
    else:
        print("이미지 크기를 가져오는 데 실패했습니다.")

    # 2. 이미지 리사이즈 (원하는 크기로 리사이즈)
    output_path = target_image_path.parent / f"{image_name}_resized.png"
    resize_image_191(target_image_path, output_path, 800)

    width, height = get_image_size(output_path)
    if width and height:
        print(f"리사이즈된 이미지 크기: {width}x{height}")
    else:
        print("리사이즈된 이미지 크기를 가져오는 데 실패")

    # # 3. 이미지 확장자 체크
    # if check_image_extension(image_filename):
    #     print("유효한 이미지 파일입니다.")
    # else:
    #     print("유효하지 않은 이미지 파일 형식입니다.")
