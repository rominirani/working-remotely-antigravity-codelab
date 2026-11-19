"""Unit test suite for `order_discounts.py`."""

from datetime import date
import unittest

from order_discounts import PromoCode, calculate_final_total


class TestOrderDiscounts(unittest.TestCase):

    def test_no_promo_code(self) -> None:
        self.assertEqual(calculate_final_total(49.99, None, date(2026, 11, 4)), 49.99)

    def test_percentage_discount_rounding(self) -> None:
        # 15% off $19.99 is $16.9915 -> should round cleanly to $16.99
        promo = PromoCode(code="SAVE15", percent_off=15.0)
        self.assertEqual(
            calculate_final_total(19.99, promo, date(2026, 11, 4)),
            16.99,
        )

    def test_fixed_voucher_never_goes_negative(self) -> None:
        # $25 voucher on a $12.50 order should clamp at $0.00
        promo = PromoCode(code="GIFT25", fixed_off=25.0)
        self.assertEqual(
            calculate_final_total(12.50, promo, date(2026, 11, 4)),
            0.00,
        )

    def test_promo_valid_on_expiration_date(self) -> None:
        # A promo expiring on 2026-11-04 should still be valid on 2026-11-04
        promo = PromoCode(
            code="LASTDAY10",
            percent_off=10.0,
            expires_on=date(2026, 11, 4),
        )
        self.assertEqual(
            calculate_final_total(100.00, promo, date(2026, 11, 4)),
            90.00,
        )

    def test_promo_rejected_day_after_expiration(self) -> None:
        promo = PromoCode(
            code="LASTDAY10",
            percent_off=10.0,
            expires_on=date(2026, 11, 4),
        )
        with self.assertRaises(ValueError):
            calculate_final_total(100.00, promo, date(2026, 11, 5))

    def test_combined_percentage_and_fixed_discount(self) -> None:
        # 20% off $59.95 ($47.96) minus $5.00 fixed = $42.96
        promo = PromoCode(code="COMBO", percent_off=20.0, fixed_off=5.0)
        self.assertEqual(
            calculate_final_total(59.95, promo, date(2026, 11, 4)),
            42.96,
        )


if __name__ == "__main__":
    unittest.main()
