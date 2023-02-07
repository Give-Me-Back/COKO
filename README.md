# COKO
- 코로나 공공 데이터를 활용한 대시보드 서비스

## GIVE-ME-BACK TEAM
- 김정현([xc7230](https://github.com/xc7230))
- 이창민([AiLEE96](https://github.com/AiLEE96))
- 백재열([jaeyeol2](https://github.com/jaeyeol2))

## 1. 기술 스택
- Python, Django : 기본 개발 언어, 웹 프레임 워크
- HTML5, JavaScript, CSS, Bootstrap, JQuery, ajax : 웹 개발을 위한 개발언어들
- Github : 협업 및 버전관리를 위한 Git
- 공공데이터 포털 API, NAVER API : 코로나 데이터, 코로나 관련 뉴스 기사를 위한 API
- AWS : Cloud 환경을 통한 Server 배포
- CICD

## 2. 상세 동작 내용
![3tier](https://user-images.githubusercontent.com/33945185/208352254-5f3f2bc5-1009-48b1-bd46-b895b8e82771.png)
- 기본 구성은 크게 API, 3Tier, CICD 부분으로 이루어져 있다.

### 2-1. API 데이터 수집
![api](https://user-images.githubusercontent.com/33945185/208352487-a53dfc7d-c9f6-4f6a-a8ab-e3a2793ddc83.png)
![api_1](https://user-images.githubusercontent.com/33945185/208352626-a695453e-68fb-47a3-9b98-de21fcecbf94.png)
- 공공데이터 포털의 API와 NAVER API를 파이썬에서 크롤링, 전처리 후 DB(MySql)에 데이터를 보내 테이블을 만든다.
- 크론탭을 사용해 매일 0시에 데이터를 갱신하여 DB를 최신화 한다.


### 2-2. 3계층
![3tier_1](https://user-images.githubusercontent.com/33945185/208353630-de45a7c8-0568-4262-bf3e-216377710a0a.png)

![3tier_2](https://user-images.githubusercontent.com/33945185/208352976-a6248983-5a9d-404b-a740-b4ecda0a3d6e.png)



### 2-3. CICD
![cicd](https://user-images.githubusercontent.com/33945185/208353747-67aa129e-9c24-4ccd-9208-b32cf9afaf82.png)
![cicid_1](https://user-images.githubusercontent.com/33945185/208353189-3663b967-61bb-4dbb-a2dc-7cfec8cb0bb3.png)


## 3. 시연 화면
### 3-1. 기본 메인 화면
![dash01](https://user-images.githubusercontent.com/33945185/208354353-3f6124e1-16a5-40dd-9142-8520d4f1d578.png)


### 3-2. 기능 화면
![dash02](https://user-images.githubusercontent.com/33945185/208354350-c62eb349-a82b-44c0-b4e5-bc4852d6817c.png)
![dash03](https://user-images.githubusercontent.com/33945185/208354363-cfcd63db-02d7-4b70-8cf5-ccdca97280df.png)
![dash04](https://user-images.githubusercontent.com/33945185/208354360-06a4e3b3-fe36-425a-ab19-dc15bce1621d.png)
![dash05](https://user-images.githubusercontent.com/33945185/208354356-b2ae6b49-96e7-4aad-b7d7-429e7f12c67f.png)


## 4. 아쉬운점 및 향후과제
### 4-1. 아쉬운점
- 스마트폰 환경에서 가독성이 떨어진다.
- 쿠버네티스와 코드형 인프라를 사용하지 못했다.
- 원래 목표인 지역구 별 데이터 까지 출력하지 못했다.

### 4-2. 향후과제
- 지역구 데이터를 확보해 좀 더 세세한 코로나 지도 구현
- 쿠버네티스를 활용한 컨테이너 환경 구축
- 테라폼 및 엔서블을 이용한 자동화
- 더 보기 편한 UI 구성


## 5. 후기
- 김정현<br/>
    ```
    그동안 프레임워크를 이용해 웹서버를 띄우는 프로젝트를 했었는데, 클라우드환경을 이용해 각각 다른 서버를 연결해서 인프라를 만드는 작업까지 할 수 있어서 많은 공부가 됐다.
    ```

