# Performance Evaluation of Deep Learning-Based Brain Tumor Segmentation Using Magnetic Resonance Imaging
### 개요
뇌종양은 두개골 내의 뇌 및 뇌 주변 구조물에서 발생하는 종양을 의미한다. 뇌종양의 경우 초기에 얼마나 정확하게 진단하는지에 따라 질병의 완치 가능성이 좌우된다. 그러나 자기공명영상(Magnetic Resonance Imaging, MRI)을 이용하여 뇌종양 영역을 검출하는 것은 상당한 시간이 소모되고 뇌종양의 위치를 부정확하게 진단할 가능성이 있다. 따라서 MRI 영상 데이터를 이용한 뇌종양 분할 및 진단 작업량을 최소한으로 줄이기 위해 다양한 딥러닝 기반 뇌종양 분할 모델 개발 연구가 활발히 진행되고 있다

정상적인 뇌와 서로 다른 종류의 뇌종양 MRI 영상 데이터 셋을 가지고 객체 검출 모델을 통해 뇌종양의 이미지 데이터 셋을 세분화하여 분류의 정확도를 높일 예정이며, 딥러닝 기반 모델을 통해 뇌종양 분류에 가장 적합한 모델을 선정하고 평가한다.

# Getting Started

## Dataset
- glioma(1426개), meningioma(708개), pituitary(930개)로 이루어진 총 3064개 뇌 MRI 이미지 dataset과 각 이미지에 따른 종양 부분이 segmentation 된 tumor mask dataset을 사용한다.
- 의료 데이터 특성 상 데이터 수가 적으므로 Elastic Deformation 기법을 통해 뇌 MRI 이미지 수를 2배로 증강하여 총 6128개의 이미지 dataset을 사용한다. 

<center>![image](https://user-images.githubusercontent.com/61490878/175048927-ba25f2df-fbfa-4abe-bb51-02f3459b56e2.png)</center>


## Model

!<center>[image](https://user-images.githubusercontent.com/83739271/196138408-1c985b56-341e-4512-8469-c22aaf95da3e.png)</center>

U-Net은 Biomedical 분야에서 이미지 분할(Image Segmentation)을 목적으로 제안된 모델이다. U-Net을 포함하여 U-Net 파생 모델인 Residual U-Net, Hybrid Res U-Net 모델을 사용하였다.

1) **UNet**: Biomedical 분야에서 Image Segmentation을 목적으로 제안된 End-to-End 방식의 Fully-Convolutional Network 기반 모델이다. 입력 이미지의 Context 포착이 목적인 Contracting Path와 세밀한 Localization을 위해 위치정보를 결합(skip connection)하여 up-sampling을 진행하는 Expanding Path로 구성되어있다.
2) **UNet++**: UNet의 기존 skip connection에서 Encoder와 Decoder 사이의 Semantic Gap을 연결하는 부분이 추가된 Re-designed skip pathways을 사용하는 모델이다.
3) **DeepResUNet**: UNet 기반 구조에서 정확도 향상을 위해 residual learning을 활용한 모델이다. 다운 샘플링, 업 샘플링 모두 잔차 학습이 사용된다.
4) **HybridResUNet**: UNet 기반 구조에서 정확도 향상을 위해 residual learning을 활용한 모델이다. 다운샘플링에서만 잔차 학습이 사용된다.




## result
#### 1) 성능 평가 지표

<center>![image](https://user-images.githubusercontent.com/83739271/196137980-8dfc8e37-1f99-49cd-9580-1378f8d3fa9e.png)</center>


모델의 성능을 평가하기 위해 Intersection over Union(IoU)와 F1-score 두 가지 평가지표를 사용하였다.


#### 2) 성능 비교

<center>![image](https://user-images.githubusercontent.com/83739271/196137840-a4f9fd05-7d29-4e7d-86ef-2d1ab319256f.png)</center>



## conclusion
 본 프로젝트에서는 뇌종양 MRI 데이터를 이용하여 U-Net 모델 아키텍처를 가지고 있는 딥러닝 기반 뇌종양 분할 모델들의 성능을 정량적으로 비교하고 평가하였다. 기본적인 U-Net 모델과 U-Net의 파생 모델들인 ResUnet, DeepResUnet, HybridResUnet 총 네 가지 모델의 성능을 IoU와 F1-score를 사용하여 평가하였다. 테스트한 모델 중에서 U-Net 모델이 0.7833(IoU), 0.8585(F1-score)로 가장 좋은 성능을 보였다. 이처럼 데이터셋에 따라 기본적인 딥러닝 아키텍처를 가지는 모델이 더 좋은 성능을 보일 수 있음을 확인하였다. 향후 다양한 조합으로 데이터셋을 분할하여 모델에 적용해 볼 것이고, 다양한 딥러닝 기반의 이미지 분할 모델에 대해서 성능 평가를 진행할 계획이다. 이를 통해 딥러닝을 기반으로 한 이미지 분할 기법이 뇌종양뿐 아니라 여러 질병에 대한 진단을 보조하는 기법으로 널리 활용될 수 있을 것이라 기대한다.
