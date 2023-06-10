# facewallet E2E Test
facewallet 데모 웹사이트를 통한 E2E test 스크립트
데모 웹사이트: https://haechi-labs.github.io/face-sample-dapp/

# 환경

## 테스트 환경
- Mac OS
- Python3

## 사전 설치 필요한 사항들

- Python 3.11 이상 설치
- 셀레니움 설치 (크롬 드라이버 설치)
- 구글 로그인을 셀레니움으로 진행하기 위해 아래 명령어 실행해서 python 모듈 설치 필요
```
$ pip3 install undetected-chromedriver

```




# 테스트 실행 방법
## preconditon
1. 테스트에 사용할 계정은 구글 메일로 가입이 되어 있어야 함
2. face wallet pin 설정이 미리 되어 있어야 함

## 유의 사항
- youtube에 연동되어 있는 계정 사용시 구글 2차 인증을 개인 디바이스에서 직접해야 함, 테스트 계정을 만들어서 실행할 것을 권유

## test 실행
- 소스 다운로드 후 아래 커맨드 형식으로 실행
```
python3 e2e.py --email (your email) --pw (your mail password) --pin(your pin number)
```
- 3개의 parameter 입력해야 테스트 가능

테스트 계정이 없다면 

- --email testsungho310 --pw testtest!! --pin 135790

계정 사용 가능 

# 테스트 시나리오
(로그인)
1. connect network에서 바오밥 선택 (추후 체인을 파라미터로 받을 예정)
2. 구글 메일로 Login 진행 (--email, --pw 값 사용)
3. 로그인 후 Pin 입력 (--pin값 사용)
4. login 성공 화면에서 continue 버튼을 눌러서 메인 화면으로 돌아옴
5. "Address" 정보 영역이 떴는지 확인

(Coin Transaction)

6. Coin Transaction Amount의 input 값 clear 후 1로 변경
7. Receiver Address input 값 clear 후 address 입력
8. Transfer coin 버튼 클릭 > send now 버튼 클릭 
9. pin 입력 (--pin값 사용)
10. Succees 화면 확인 후 x버튼으로 메인 화면으로 돌아옴
11. Explore Link 생성 확인 > 버튼을 눌러서 Klaytn scope 화면 이동
