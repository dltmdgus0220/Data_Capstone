# Performance Evaluation of Deep Learning-Based Brain Tumor Segmentation Using Magnetic Resonance Imaging
### 개요
뇌종양은 두개골 내의 뇌 및 뇌 주변 구조물에서 발생하는 종양을 의미한다. 뇌종양의 경우 초기에 얼마나 정확하게 진단하는지에 따라 질병의 완치 가능성이 좌우된다. 그러나 자기공명영상(Magnetic Resonance Imaging, MRI)을 이용하여 뇌종양 영역을 검출하는 것은 상당한 시간이 소모되고 뇌종양의 위치를 부정확하게 진단할 가능성이 있다. 따라서 MRI 영상 데이터를 이용한 뇌종양 분할 및 진단 작업량을 최소한으로 줄이기 위해 다양한 딥러닝 기반 뇌종양 분할 모델 개발 연구가 활발히 진행되고 있다

정상적인 뇌와 서로 다른 종류의 뇌종양 MRI 영상 데이터 셋을 가지고 객체 검출 모델을 통해 뇌종양의 이미지 데이터 셋을 세분화하여 분류의 정확도를 높일 예정이며, 딥러닝 기반 모델을 통해 뇌종양 분류에 가장 적합한 모델을 선정하고 평가한다.

# Getting Started

## Dataset
- glioma(1426개), meningioma(708개), pituitary(930개)로 이루어진 총 3064개 뇌 MRI 이미지 dataset과 각 이미지에 따른 종양 부분이 segmentation 된 tumor mask dataset을 사용한다.
- 의료 데이터 특성 상 데이터 수가 적으므로 Elastic Deformation 기법을 통해 뇌 MRI 이미지 수를 2배로 증강하여 총 6128개의 이미지 dataset을 사용한다. 

![image](https://user-images.githubusercontent.com/61490878/175048927-ba25f2df-fbfa-4abe-bb51-02f3459b56e2.png)

![image](https://user-images.githubusercontent.com/61490878/175049650-0d57542a-84b3-46fe-ba0a-3f9baf17f381.png)


## Model

![image](https://user-images.githubusercontent.com/61490878/175050012-de253483-dfdb-4d82-8f8b-80f212762206.png)

U-Net은 Biomedical 분야에서 이미지 분할(Image Segmentation)을 목적으로 제안된 모델이다. U-Net을 포함하여 U-Net 기반 모델인 U-Net++(Nested U-Net), Deep Res U-Net, Hybrid Res U-Net 모델을 사용하였다.

1) **UNet**: Biomedical 분야에서 Image Segmentation을 목적으로 제안된 End-to-End 방식의 Fully-Convolutional Network 기반 모델이다. 입력 이미지의 Context 포착이 목적인 Contracting Path와 세밀한 Localization을 위해 위치정보를 결합(skip connection)하여 up-sampling을 진행하는 Expanding Path로 구성되어있다.
2) **UNet++**: UNet의 기존 skip connection에서 Encoder와 Decoder 사이의 Semantic Gap을 연결하는 부분이 추가된 Re-designed skip pathways을 사용하는 모델이다.
3) **DeepResUNet**: UNet 기반 구조에서 정확도 향상을 위해 residual learning을 활용한 모델이다. 다운 샘플링, 업 샘플링 모두 잔차 학습이 사용된다.
4) **HybridResUNet**: UNet 기반 구조에서 정확도 향상을 위해 residual learning을 활용한 모델이다. 다운샘플링에서만 잔차 학습이 사용된다.




## result
#### 1) 데이터 증강 전 후 성능 비교

![image](https://user-images.githubusercontent.com/61490878/175051057-0485bffd-eaf3-4962-94e6-84b782705bad.png)

- 증강 후 overfitting을 방지할 수 있었고 성능 또한 대체적으로 향상되었음을 볼 수 있다.
- UNet의 성능이 IoU 0.6640으로 가장 높게 나왔다.


#### 2) learning rate 별 성능 비교

![image](https://user-images.githubusercontent.com/61490878/175051175-4bcd7dca-9476-49f2-b435-c00dfd715891.png)


> ![image](https://user-images.githubusercontent.com/61490878/175052070-3903451a-60a2-4a83-88cf-36fcd29e1f67.png)  **Test set IoU(lr:0.01)**  

Unet: 0.7255 –> 0.7522  
Deep_ResUnet : 0.6921-> 0.7162  
Hybrid_ResUnet :  0.7152 -> 0.7432
- learning rate을 0.01로 설정하였을 때 성능이 향상됨을 볼 수 있었다.
- UNet의 성능이 IoU 0.7522로 가장 높게 나왔다.


## conclusion
 이번 프로젝트는 segmentation 하는 모델을 새롭게 구현하는 것이 아닌 기존 모델들의 파라미터나 구조를 조금씩 변경해보면서 성능을 높이는데 초점을 두었다. 그러나 똑같은 데이터셋을 사용한 선행 연구보다 낮은 정확도를 보였다. 성능이 떨어지는 원인을 찾기 위해 여러 시도들을 해보았지만 모델 구조도 조금씩 수정하였고 입력 데이터셋 또한 matlab 파일을 사용한 선행 연구와는 달리 jpg 로 변환해서 사용하는 등 통제 변인과 조작변인이 명확하지 않은 상태였다. 때문에 성능 저하의 원인을 찾는데 어려움이 있었다. 이를 통해 성능 개선을 위한 연구에서 독립변인을 정확히 나누는 것에 대한 중요성을 깨닫게 되었다.  
또한 팀 프로젝트에서는 개인의 역량, 아이디어 등도 중요하지만 무엇보다 중요한 것은 팀원들과 정보 공유, 소통이라는 것을 알게 되었다. 초반에는 코드 작업을 할 때 각자 진행하였기 때문에 코드를 통합하는 과정에서 어려움이 있었다. 이를 해결하기위해 notion 이나 github 를 적극적으로 활용하며 서로의 결과물들을 공유했고 회의를 통해 각자의 진행상황, 어려운 점 등을 공유하면서 적극적으로 의사소통을 했기에 프로젝트를 성공적으로 마무리 할 수 있었다고 생각한다.
