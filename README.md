# Performance Evaluation of Deep Learning-Based Brain Tumor Segmentation Using Magnetic Resonance Imaging 
### 개요
뇌종양은 두개골 내의 뇌 및 뇌 주변 구조물에서 발생하는 종양을 의미한다. 뇌종양의 경우 초기에 얼마나 정확하게 진단하는지에 따라 질병의 완치 가능성이 좌우된다. 그러나 자기공명영상(Magnetic Resonance Imaging, MRI)을 이용하여 뇌종양 영역을 검출하는 것은 상당한 시간이 소모되고 뇌종양의 위치를 부정확하게 진단할 가능성이 있다. 따라서 MRI 영상 데이터를 이용한 뇌종양 분할 및 진단 작업량을 최소한으로 줄이기 위해 다양한 딥러닝 기반 뇌종양 분할 모델 개발 연구가 활발히 진행되고 있다

정상적인 뇌와 서로 다른 종류의 뇌종양 MRI 영상 데이터 셋을 가지고 객체 검출 모델을 통해 뇌종양의 이미지 데이터 셋을 세분화하여 분류의 정확도를 높일 예정이며, 딥러닝 기반 모델을 통해 뇌종양 분류에 가장 적합한 모델을 선정하고 평가한다.

# Getting Started

## Dataset
- glioma(1426개), meningioma(708개), pituitary(930개)로 이루어진 총 3064개 뇌 MRI 이미지 dataset과 각 이미지에 따른 종양 부분이 segmentation 된 tumor mask dataset을 사용한다.
- 의료 데이터 특성 상 데이터 수가 적으므로 Elastic Deformation 기법을 통해 뇌 MRI 이미지 수를 2배로 증강하여 총 6128개의 이미지 dataset을 사용한다. 

![image](https://user-images.githubusercontent.com/83739271/196184545-bdd10bad-b4b4-4213-9f35-4ea8b69220c1.png)


## Model

![image](https://user-images.githubusercontent.com/83739271/196138408-1c985b56-341e-4512-8469-c22aaf95da3e.png)

U-Net은 Biomedical 분야에서 이미지 분할(Image Segmentation)을 목적으로 제안된 모델이다. U-Net을 포함하여 U-Net 파생 모델인 Residual U-Net, Hybrid Res U-Net 모델을 사용하였다.

1) **UNet**: Biomedical 분야에서 Image Segmentation을 목적으로 제안된 End-to-End 방식의 Fully-Convolutional Network 기반 모델이다. 입력 이미지의 Context 포착이 목적인 Contracting Path와 세밀한 Localization을 위해 위치정보를 결합(skip connection)하여 up-sampling을 진행하는 Expanding Path로 구성되어있다.

![image](https://user-images.githubusercontent.com/83739271/196184966-5d3bf7fd-6f81-4512-a646-8e4c9566856c.png)

2) **Residual U-Net(ResUnet)**: ResUnet은 기존 U-Net 모델에서 resnet 블록을 활용한 모델이다. Resnet 블록은 위 그람과 같이 동작한다. 네트워크의 출력값 H(x)가 입력값 x가 되도록, 잔차 H(x)-x 를 최소화하는 방향으로 학습을 진행한다. 

![image](https://user-images.githubusercontent.com/83739271/196185049-5b51bc71-4eac-4eff-b1d9-7e55d8983ea6.png)

3) **Deep-Residual U-Net(DeepResUnet)**: DeepResUnet은 ResUnet 모델에서 resnet 블록 대신 preactivate resnet 블록을 사용하는 모델이다. Preactivate resnet 블록은 2D batch normal, ReLU 활성함수, 2D convolution 연산 순으로 통과하고 F(x)+x가 ReLU 활성화 함수를 거치지 않는다.

![image](https://user-images.githubusercontent.com/83739271/196185113-07f2c243-75be-4756-bbce-ded43831f9ae.png)

4) **Hybrid-Residual U-Net(HybridResUnet)**: HybridResUnet은 기존 U-Net 모델에서 contracting path 부분을 ResUnet의 contracting path로 바꾼 모델이다. 





## result
#### 1) 성능 평가 지표

![image](https://user-images.githubusercontent.com/83739271/196137980-8dfc8e37-1f99-49cd-9580-1378f8d3fa9e.png)


모델의 성능을 평가하기 위해 Intersection over Union(IoU)와 F1-score 두 가지 평가지표를 사용하였다.


#### 2) 성능 비교

![image](https://ifh.cc/g/y60ZqL.png)



## conclusion
 본 프로젝트에서는 뇌종양 MRI 데이터를 이용하여 U-Net 모델 아키텍처를 가지고 있는 딥러닝 기반 뇌종양 분할 모델들의 성능을 정량적으로 비교하고 평가하였다. 
 
 기본적인 U-Net 모델과 U-Net의 파생 모델들인 ResUnet, DeepResUnet, HybridResUnet 총 네 가지 모델의 성능을 IoU와 F1-score를 사용하여 평가하였다. 테스트한 모델 중에서 U-Net 모델이 0.7833(IoU), 0.8585(F1-score)로 가장 좋은 성능을 보였다. 이처럼 데이터셋에 따라 기본적인 딥러닝 아키텍처를 가지는 모델이 더 좋은 성능을 보일 수 있음을 확인하였다.
 
 향후 다양한 조합으로 데이터셋을 분할하여 모델에 적용해 볼 것이고, 다양한 딥러닝 기반의 이미지 분할 모델에 대해서 성능 평가를 진행할 계획이다. 이를 통해 딥러닝을 기반으로 한 이미지 분할 기법이 뇌종양뿐 아니라 여러 질병에 대한 진단을 보조하는 기법으로 널리 활용될 수 있을 것이라 기대한다.

## Reference 

* https://github.com/4uiiurz1/pytorch-nested-unet
