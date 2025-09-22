from abc import ABC, abstractmethod


class Deposit(ABC):
    def __init__(self, amount: float, months: int, percent: float):
        self.amount = amount
        self.months = months
        self.percent = percent

    @abstractmethod
    def calculate_final_amount(self) -> float:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class InstantDeposit(Deposit):
    def calculate_final_amount(self) -> float:
        years = self.months / 12
        return self.amount * (1 + self.percent / 100 * years)

    def get_name(self) -> str:
        return "Срочный вклад"


class BonusDeposit(Deposit):
    def __init__(self, amount: float, months: int, percent: float,
                 min_bonus_amount: float, bonus_percent: float = None, bonus_fixed: float = None):
        super().__init__(amount, months, percent)
        self.min_bonus_amount = min_bonus_amount
        self.bonus_percent = bonus_percent
        self.bonus_fixed = bonus_fixed

    def calculate_final_amount(self) -> float:
        years = self.months / 12
        base_amount = self.amount * (1 + self.percent / 100 * years)

        bonus = 0.0
        if self.amount >= self.min_bonus_amount:
            if self.bonus_percent is not None:
                bonus = self.amount * (self.bonus_percent / 100)
            elif self.bonus_fixed is not None:
                bonus = self.bonus_fixed

        return base_amount + bonus

    def get_name(self) -> str:
        return "Бонусный вклад"


class CapitalizedDeposit(Deposit):
    def calculate_final_amount(self) -> float:
        monthly_rate = self.percent / 100 / 12
        amount = self.amount
        for _ in range(self.months):
            amount += amount * monthly_rate
        return amount

    def get_name(self) -> str:
        return "Вклад с капитализацией"


class DepositSelector:
    def __init__(self, deposits: list[Deposit]):
        self.deposits = deposits

    def select_best_deposit(self) -> Deposit:
        best_deposit = max(self.deposits, key=lambda d: d.calculate_final_amount())
        return best_deposit

    def show_comparison(self):
        for deposit in self.deposits:
            final = deposit.calculate_final_amount()
            print(f"{deposit.get_name()}: {final:.2f} ₽")

    def recommend(self):
        best = self.select_best_deposit()
        print(f"Рекомендуемый вклад: {best.get_name()}")
        print(f"Итоговая сумма: {best.calculate_final_amount():,.2f} ₽")


def main():

    amount = float(input("Введите сумму вклада: "))
    term = int(input("Введите срок вклада (месяцев): "))
    rate = float(input("Введите годовую процентную ставку (%): "))

    deposits = [
        InstantDeposit(amount, term, rate),
        CapitalizedDeposit(amount, term, rate),
        BonusDeposit(
            amount=amount,
            months=term,
            percent=rate,
            min_bonus_amount=100_000,      # бонус при сумме от 100 тыс.
            bonus_percent=2.0              # +2% бонусом
        )
    ]

    selector = DepositSelector(deposits)
    selector.show_comparison()
    selector.recommend()

if __name__ == "__main__":
    main()