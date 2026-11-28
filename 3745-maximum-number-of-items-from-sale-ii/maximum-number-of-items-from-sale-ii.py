class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        if not items or budget <= 0:
            return 0

        min_price = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        mult_count = [0] * (max_factor + 1)
        for factor, _ in items:
            mult_count[factor] += 1

        for f in range(1, max_factor + 1):
            if mult_count[f]:
                for m in range(2 * f, max_factor + 1, f):
                    mult_count[f] += mult_count[m]

        # (price, max_bonus_copies) for items that can give free items and beat baseline
        candidates = []
        for factor, price in items:
            cap = mult_count[factor] - 1
            if cap > 0 and price < 2 * min_price:
                candidates.append((price, cap))

        candidates.sort(key=lambda x: x[0])

        total = 0
        for price, cap in candidates:
            if budget < price:
                break
            take = min(cap, budget // price)
            total += 2 * take
            budget -= take * price

        total += budget // min_price
        return total
        