# Data_Capstone

#### 0. 실행 전 수정해야하는 사항
- train.py, val.py 파일마다 ctrl+F로 'root' 검색하여 directory에 본인 Volumes 이름으로 설정해주세요.
- train.py의 98번째 줄에 원하는 worker 수를 지정해주세요.
#
#### 1. Unet 실행 방법
- train.py 수정사항
> - 41번째 줄(arch)의 defualt값을 'UNet'으로 설정해주세요.
> - 46번째 줄(deep_supervision)의 defualt값을 False로 설정해주세요.
> - 219~227번째 줄(model)에서 UNet model을 사용해주세요.

- val.py 수정사항
> - 24번째 줄(model name)의 default값을 사용할 모델 파일 이름으로 설정해주세요.

#
#### 2. Unet++ 실행 방법
- train.py 수정사항
> - 41번째 줄(arch)의 defualt값을 'NestedUNet'으로 설정해주세요.
> - 46번째 줄(deep_supervision)의 defualt값을 설정해주세요.(deep_supervision을 사용할거면 True)
> - 219~227번째 줄(model)에서 NestedUNet model을 사용해주세요.

- val.py 수정사항
> - 24번째 줄(model name)의 default값을 사용할 모델 파일 이름으로 설정해주세요.
