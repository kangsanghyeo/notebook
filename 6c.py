def main():
    try:
        X = int(input("대중교통을 탄 일 수를 입력하세요: "))

        car = (225 / 365) * X
        public_transport = (50 / 365) * X

        Y = car - public_transport

        print(f"\n{X}일 동안 자가용으로 소비한 비용: {car:.2f}만원")
        print(f"{X}일 동안 대중교통으로 소비한 비용: {public_transport:.2f}만원")
        print(f"당신은 {X}일 동안 자가용을 탄 사람보다 {Y:.2f}만원을 절약하였습니다.")

    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    main()

