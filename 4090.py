def calculate_mileage(distance, fuel_used):
    try:
        distance = float(distance)
        fuel_used = float(fuel_used)

        if distance <= 0 or fuel_used <= 0:
            raise ValueError("거리와 연료 사용량은 양수여야 합니다.")

        mileage = distance / fuel_used
        return mileage
    except ValueError as e:
        return str(e)

def calculate_efficiency(distance, energy_used):
    try:
        distance = float(distance)
        energy_used = float(energy_used)

        if distance <= 0 or energy_used <= 0:
            raise ValueError("거리와 에너지 사용량은 양수여야 합니다.")

        efficiency = distance / energy_used
        return efficiency
    except ValueError as e:
        return str(e)

def compare_efficiency(fuel_efficiency, electric_efficiency):
    try:
        fuel_efficiency = float(fuel_efficiency)
        electric_efficiency = float(electric_efficiency)

        if fuel_efficiency <= 0 or electric_efficiency <= 0:
            raise ValueError("연비는 양수여야 합니다.")

        return fuel_efficiency, electric_efficiency
    except ValueError as e:
        return str(e), None, None

def get_efficiency():
    print("차량 종류를 선택해주세요.")
    print("1. 연료 차량")
    print("2. 전기 차량")

    choice = input("선택 (1 또는 2): ")

    if choice == '1':
        print("연료 차량을 선택하셨습니다.")
        distance = input("총 주행 거리 (km): ")
        fuel_used = input("사용된 연료 양 (L): ")
        efficiency = calculate_mileage(distance, fuel_used)
        unit = "km/L"

    elif choice == '2':
        print("전기 차량을 선택하셨습니다.")
        distance = input("총 주행 거리 (km): ")
        energy_used = input("사용된 전력 양 (kWh): ")
        efficiency = calculate_efficiency(distance, energy_used)
        unit = "km/kWh"

    else:
        print("잘못된 선택입니다. 1 또는 2 중에서 선택해주세요.")
        return None, None, None

    if isinstance(efficiency, float):
        print(f"차량 효율: {efficiency:.2f} {unit}")
        return efficiency, choice
    else:
        print(f"오류: {efficiency}")
        return None, None, None

def compare_and_output(efficiency1, choice1, efficiency2, choice2):
    if efficiency1 is not None and efficiency2 is not None:
        print(f"\n{choice2} 차량을 선택하셨습니다.")

        if choice2 == '1':
            print("연료 차량을 선택하셨습니다.")
            distance = input("총 주행 거리 (km): ")
            fuel_used = input("사용된 연료 양 (L): ")
            efficiency_second = calculate_mileage(distance, fuel_used)
            unit = "km/L"

        elif choice2 == '2':
            print("전기 차량을 선택하셨습니다.")
            distance = input("총 주행 거리 (km): ")
            energy_used = input("사용된 전력 양 (kWh): ")
            efficiency_second = calculate_efficiency(distance, energy_used)
            unit = "km/kWh"

        else:
            print("잘못된 선택입니다. 1 또는 2 중에서 선택해주세요.")
            return

        if isinstance(efficiency_second, float):
            print(f"차량 효율: {efficiency_second:.2f} {unit}")

            # 두 차량의 연비 비교
            if efficiency1 > efficiency_second:
                print("첫 번째 차량이 더 좋은 연비를 가집니다.")
            elif efficiency1 < efficiency_second:
                print("두 번째 차량이 더 좋은 연비를 가집니다.")
            else:
                print("두 차량의 연비가 같습니다.")

        else:
            print(f"오류: {efficiency_second}")

def main():
    print("첫 번째 차량을 선택해주세요.")
    efficiency1, choice1 = get_efficiency()

    if efficiency1 is not None:
        efficiency2, choice2 = get_efficiency()

        compare_and_output(efficiency1, choice1, efficiency2, choice2)

if __name__ == "__main__":
    main()





