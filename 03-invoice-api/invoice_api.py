"""Local Invoice API Service (Starter with 2 intentional bugs for Remote Control lab)."""

from decimal import Decimal, ROUND_HALF_UP
from typing import Any, Dict, List


def calculate_invoice_total(
    items: List[Dict[str, Any]],
    tax_rate: Decimal = Decimal("0.0825"),
) -> Dict[str, str]:
    """Calculates subtotal, tax, and total for a list of invoice line items."""
    subtotal = Decimal("0.00")
    taxable_amount = Decimal("0.00")

    for item in items:
        line_total = Decimal(str(item["unit_price"])) * int(item["qty"])
        subtotal += line_total
        taxable_amount += line_total

    tax = (taxable_amount * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    total = (subtotal + tax).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {
        "subtotal": str(subtotal.quantize(Decimal("0.01"))),
        "tax": str(tax),
        "total": str(total),
    }


def build_invoice_gcs_uri(bucket_name: str, invoice_id: str) -> str:
    """Returns the Cloud Storage URI where the generated PDF invoice will be stored."""
    return f"gs://{bucket_name}/invoices/{invoice_id}.pdf"
