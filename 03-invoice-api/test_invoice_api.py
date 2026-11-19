"""Unit test suite for `invoice_api.py`."""

import unittest

from invoice_api import build_invoice_gcs_uri, calculate_invoice_total


class TestLocalInvoiceApi(unittest.TestCase):

    def test_standard_taxable_items(self) -> None:
        items = [{"sku": "cloud-seat", "unit_price": "100.00", "qty": 2, "tax_exempt": False}]
        result = calculate_invoice_total(items)
        self.assertEqual(result["subtotal"], "200.00")
        self.assertEqual(result["tax"], "16.50")
        self.assertEqual(result["total"], "216.50")

    def test_tax_exempt_items_not_taxed(self) -> None:
        items = [
            {"sku": "cloud-seat", "unit_price": "100.00", "qty": 1, "tax_exempt": False},
            {"sku": "nonprofit-grant", "unit_price": "200.00", "qty": 1, "tax_exempt": True},
        ]
        result = calculate_invoice_total(items)
        self.assertEqual(result["subtotal"], "300.00")
        self.assertEqual(result["tax"], "8.25")
        self.assertEqual(result["total"], "308.25")

    def test_gcs_invoice_uri_rejects_invalid_id(self) -> None:
        self.assertEqual(
            build_invoice_gcs_uri("acme-invoices-prod", "INV-2026-009"),
            "gs://acme-invoices-prod/invoices/INV-2026-009.pdf",
        )
        with self.assertRaises(ValueError):
            build_invoice_gcs_uri("acme-invoices-prod", "../secret")
        with self.assertRaises(ValueError):
            build_invoice_gcs_uri("acme-invoices-prod", "   ")


if __name__ == "__main__":
    unittest.main()
