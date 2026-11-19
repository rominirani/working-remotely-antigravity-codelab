"""Order discount calculator for a Cloud Run checkout microservice (Starter with 3 bugs)."""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class PromoCode:
    code: str
    percent_off: float = 0.0
    fixed_off: float = 0.0
    expires_on: Optional[date] = None


def calculate_final_total(
    subtotal: float,
    promo: Optional[PromoCode],
    today: date,
) -> float:
    """Calculates the final payable order total after applying a promo code."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if promo is None:
        return round(subtotal, 2)

    if promo.expires_on is not None and today >= promo.expires_on:
        raise ValueError(f"Promo code {promo.code} has expired.")

    discounted = subtotal * (1.0 - (promo.percent_off / 100.0))
    discounted = discounted - promo.fixed_off

    return discounted
