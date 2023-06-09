# facewalletE2E
facewallet E2E test

# 환경 세팅
## 셀레니움 설치

기타 등등

pip3 install selenium-stealth

pip3 install undetected-chromedriver





# 테스트 실행 방법
## preconditon
1. 테스트에 사용할 계정은 구글 메일로 가입이 되어 있어야 함
2. pin 설정이 되어 있어야 함

## test command
- python3 e2e.py --email (your email) --pw (your mail password) --pin(your pin number)
- 3개의 parameter 입력해야 테스트 가능

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
