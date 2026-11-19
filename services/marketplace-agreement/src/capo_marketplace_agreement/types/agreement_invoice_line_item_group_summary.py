"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementInvoiceLineItemGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.invoice_billing_period
    import capo_marketplace_agreement.types.invoice_type
    import capo_marketplace_agreement.types.invoicing_entity
    import capo_marketplace_agreement.types.pricing_currency_amount
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.timestamp


class AgreementInvoiceLineItemGroupSummary(TypedDict, closed=True):
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement.</p>"""
    invoice_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The identifier of the invoice for this group.</p>"""
    pricing_currency_amount: NotRequired[
        "capo_marketplace_agreement.types.pricing_currency_amount.PricingCurrencyAmount"
    ]
    """<p>Monetary amounts for this invoice group.</p>"""
    invoice_billing_period: NotRequired[
        "capo_marketplace_agreement.types.invoice_billing_period.InvoiceBillingPeriod"
    ]
    """<p>The billing period associated with this group.</p>"""
    issued_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The timestamp when the invoice containing this group was created.</p>"""
    invoice_type: NotRequired[
        "capo_marketplace_agreement.types.invoice_type.InvoiceType"
    ]
    """<p>The type of invoice. Valid values are <code>INVOICE</code> and <code>CREDIT_MEMO</code>.</p>"""
    invoicing_entity: NotRequired[
        "capo_marketplace_agreement.types.invoicing_entity.InvoicingEntity"
    ]
    """<p>The entity that issues the invoice.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementInvoiceLineItemGroupSummary) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "invoice_id" in value:
        out["invoiceId"] = value["invoice_id"]
    if "pricing_currency_amount" in value:
        import capo_marketplace_agreement.types.pricing_currency_amount

        out["pricingCurrencyAmount"] = (
            capo_marketplace_agreement.types.pricing_currency_amount.serialize_aws_json_1_0(
                value["pricing_currency_amount"]
            )
        )
    if "invoice_billing_period" in value:
        import capo_marketplace_agreement.types.invoice_billing_period

        out["invoiceBillingPeriod"] = (
            capo_marketplace_agreement.types.invoice_billing_period.serialize_aws_json_1_0(
                value["invoice_billing_period"]
            )
        )
    if "issued_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["issuedTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["issued_time"]
            )
        )
    if "invoice_type" in value:
        import capo_marketplace_agreement.types.invoice_type

        out["invoiceType"] = (
            capo_marketplace_agreement.types.invoice_type.serialize_aws_json_1_0(
                value["invoice_type"]
            )
        )
    if "invoicing_entity" in value:
        import capo_marketplace_agreement.types.invoicing_entity

        out["invoicingEntity"] = (
            capo_marketplace_agreement.types.invoicing_entity.serialize_aws_json_1_0(
                value["invoicing_entity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementInvoiceLineItemGroupSummary:
    out: AgreementInvoiceLineItemGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("invoiceId") is not None:
        out["invoice_id"] = data["invoiceId"]
    if data.get("pricingCurrencyAmount") is not None:
        import capo_marketplace_agreement.types.pricing_currency_amount

        out["pricing_currency_amount"] = (
            capo_marketplace_agreement.types.pricing_currency_amount.deserialize_aws_json_1_0(
                data["pricingCurrencyAmount"]
            )
        )
    if data.get("invoiceBillingPeriod") is not None:
        import capo_marketplace_agreement.types.invoice_billing_period

        out["invoice_billing_period"] = (
            capo_marketplace_agreement.types.invoice_billing_period.deserialize_aws_json_1_0(
                data["invoiceBillingPeriod"]
            )
        )
    if data.get("issuedTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["issued_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["issuedTime"]
            )
        )
    if data.get("invoiceType") is not None:
        import capo_marketplace_agreement.types.invoice_type

        out["invoice_type"] = (
            capo_marketplace_agreement.types.invoice_type.deserialize_aws_json_1_0(
                data["invoiceType"]
            )
        )
    if data.get("invoicingEntity") is not None:
        import capo_marketplace_agreement.types.invoicing_entity

        out["invoicing_entity"] = (
            capo_marketplace_agreement.types.invoicing_entity.deserialize_aws_json_1_0(
                data["invoicingEntity"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementInvoiceLineItemGroupSummary) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "invoice_id" in value:
        out["invoiceId"] = value["invoice_id"]
    if "pricing_currency_amount" in value:
        import capo_marketplace_agreement.types.pricing_currency_amount

        out["pricingCurrencyAmount"] = (
            capo_marketplace_agreement.types.pricing_currency_amount.serialize_cbor(
                value["pricing_currency_amount"]
            )
        )
    if "invoice_billing_period" in value:
        import capo_marketplace_agreement.types.invoice_billing_period

        out["invoiceBillingPeriod"] = (
            capo_marketplace_agreement.types.invoice_billing_period.serialize_cbor(
                value["invoice_billing_period"]
            )
        )
    if "issued_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["issuedTime"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["issued_time"]
        )
    if "invoice_type" in value:
        import capo_marketplace_agreement.types.invoice_type

        out["invoiceType"] = (
            capo_marketplace_agreement.types.invoice_type.serialize_cbor(
                value["invoice_type"]
            )
        )
    if "invoicing_entity" in value:
        import capo_marketplace_agreement.types.invoicing_entity

        out["invoicingEntity"] = (
            capo_marketplace_agreement.types.invoicing_entity.serialize_cbor(
                value["invoicing_entity"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AgreementInvoiceLineItemGroupSummary:
    out: AgreementInvoiceLineItemGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("invoiceId") is not None:
        out["invoice_id"] = data["invoiceId"]
    if data.get("pricingCurrencyAmount") is not None:
        import capo_marketplace_agreement.types.pricing_currency_amount

        out["pricing_currency_amount"] = (
            capo_marketplace_agreement.types.pricing_currency_amount.deserialize_cbor(
                data["pricingCurrencyAmount"]
            )
        )
    if data.get("invoiceBillingPeriod") is not None:
        import capo_marketplace_agreement.types.invoice_billing_period

        out["invoice_billing_period"] = (
            capo_marketplace_agreement.types.invoice_billing_period.deserialize_cbor(
                data["invoiceBillingPeriod"]
            )
        )
    if data.get("issuedTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["issued_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_cbor(
                data["issuedTime"]
            )
        )
    if data.get("invoiceType") is not None:
        import capo_marketplace_agreement.types.invoice_type

        out["invoice_type"] = (
            capo_marketplace_agreement.types.invoice_type.deserialize_cbor(
                data["invoiceType"]
            )
        )
    if data.get("invoicingEntity") is not None:
        import capo_marketplace_agreement.types.invoicing_entity

        out["invoicing_entity"] = (
            capo_marketplace_agreement.types.invoicing_entity.deserialize_cbor(
                data["invoicingEntity"]
            )
        )
    return out
