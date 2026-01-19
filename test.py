# 1. 라이브러리 임포트 
import sys

# 2. 함수 정의 
def say_hello(name):
    return f"Hello, {name}! 프로젝트 서버에 오신 걸 환영합니다."

# 3. 메인 함수
def main():
    print("프로그램을 시작합니다...")
    
    user_name = "homsis"
    result = say_hello(user_name)
    print(result)

# 4. 실행부 
if __name__ == "__main__":
    main()
