# My Food Diary (맛뿌다)

#### 프로젝트 개요

* 사용자 보유한 식재료에 기반해 레시피를 추천해 주는 웹 서비스.



#### 주요 기능

* 사용자가 보유한 식재료를 등록할 수 있다.
  * 식재료 목록을 수정, 삭제할 수 있다.
  * 식재료의 유통기한을 확인할 수 있다.
* 등록한 식재료나 추가로 사용할 식재료를 선택해 레시피를 추천받을 수 있다.
* 추천받은 레시피의 상세 정보를 확인할 수 있다.
* 레시피를 등록할 수 있다.
  * 레시피에 들어갈 식재료를 검색하여 선택할 수 있다.

* 레시피의 리뷰를 달 수 있다.
* 마이 페이지에서 사용자 정보를 확인 및 수정 가능하다.
* 관리페이지에서 간단한 시각화 자료를 볼 수 있다.




#### 데이터베이스 ERD

[**https://www.erdcloud.com/d/gBDj573CbAxbdeTz4**]



#### 개발 환경

* Python 3.8.5

* anaconda3

* Django 3.1.5

* mysql Ver 15.1 Distrib 10.3.11-MariaDB, for Win64

* Bootstrap 4



#### 개발 일정

| 년.월   | 일    | 내용               |
| ------- | ----- | ------------------ |
| 2021.01 | 19    | 프로젝트 주제 설정 |
|         | 20~22 | ERD 설계           |
|         | 25~29 | 화면 설계          |
| 2021.02 | 01~   | 구현               |



#### 초기 db 데이터 크롤링([경로](./frame/scraping/scraping.py))

<img src="https://github.com/cano721/my-food-diary/blob/master/images/스크롤1.JPG?raw=true">



* 초기 식재료 및 레시피 데이터 db 구축을 위한 크롤링 작업
  * beautifulsoup을 통한 웹크롤링과 정규화를 통한 데이터 처리



#### 메인 화면

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155883409-cf448176-a5ee-4a95-9776-710821fa944c.gif">
</p>

* 오늘의 추천 : 추천도 높은 순서대로 3종류 추천
* 레시피 이미지: 레시피 중 일부 이미지 표시
* 최근 작성된 리뷰
* 최근 방문기록
* 푸터 작성 : 개발자 깃허브 연동 및 임시 회사 위치 표시



#### 관리자 페이지 화면

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155886502-6f278e9f-b32b-4467-aa96-558fb1e60acf.gif">
</p>

* 관리자 전용 화면
* highChart를 이용한 간단한 시각화 자료 제공(회원가입 수, 인기 식재료, 레시피 등)



#### 로그인& 로그아웃& 회원가입 화면

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155886486-71727dc2-ab09-4798-bcb8-94402525c1c9.gif">
</p>

* 로그인 및 로그아웃 기능
* 회원가입 : id 중복체크 기능



#### 레시피 추천받기 화면

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155885367-d71ad042-8ad4-450b-a1fa-fc242b6e9960.gif">
</p>

* 식재료에 따른 레시피 추천
* 초기값은 사용자가 가지고 있는 식재료 선택
* 식재료 검색해서 추가하여 검색 가능



#### 레시피 상세 화면


<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155885415-22016926-4663-40d2-a7b8-bc524b49286d.gif">
</p>

* 레시피 재료 소개
* 조리방법 소개
* 레시피 평가 및 리뷰
* 바로 리뷰 달 수 있음



#### 레시피 즐겨찾기

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155886499-30010abe-d1d3-4f8e-bc97-f702012b7623.gif">
</p>

* 레시피 즐겨찾기 추가(채워진 하트) 및 취소(빈 하트)



#### 레시피 등록 화면

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155887296-8b03dcf8-77ec-4227-960d-68b4ff0bf22b.gif">
</p>

* 레시피 등록
* 레시피 내 식재료 추가, 삭제 가능
* 식재료 검색하여 선택
* 레시피 사진 삽입
* 공개, 비공개 여부 선택 가능



#### 내 재료 확인 화면

<p aligin="center">
 <img src="https://user-images.githubusercontent.com/76922918/155886493-ad68e4ff-8ff3-4b51-bad0-03f4f7711725.gif">
</p>

* 사용자가 가진 식재료 표시
* 유통기한에 따른 구분
* 수정 및 삭제 가능




#### 개발자 정보

조재언 [**injoe90**](https://github.com/injoe90)

계해범 [**cano721**](https://github.com/cano721)

김송현 [**songhyunn**](https://github.com/songhyunn)

김우림 [**woorim1022**](https://github.com/woorim1022)

