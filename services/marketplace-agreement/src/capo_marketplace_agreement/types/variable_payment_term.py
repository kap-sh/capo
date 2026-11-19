"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#VariablePaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type
    import capo_marketplace_agreement.types.variable_payment_term_configuration


class VariablePaymentTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Type of the term.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in the term.</p>"""
    max_total_charge_amount: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The maximum total amount that can be charged to the customer through variable payment requests under this term.</p>"""
    configuration: NotRequired[
        "capo_marketplace_agreement.types.variable_payment_term_configuration.VariablePaymentTermConfiguration"
    ]
    """<p>Additional parameters specified by the acceptor while accepting the term.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VariablePaymentTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "max_total_charge_amount" in value:
        out["maxTotalChargeAmount"] = value["max_total_charge_amount"]
    if "configuration" in value:
        import capo_marketplace_agreement.types.variable_payment_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.variable_payment_term_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VariablePaymentTerm:
    out: VariablePaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("maxTotalChargeAmount") is not None:
        out["max_total_charge_amount"] = data["maxTotalChargeAmount"]
    if data.get("configuration") is not None:
        import capo_marketplace_agreement.types.variable_payment_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.variable_payment_term_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VariablePaymentTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "max_total_charge_amount" in value:
        out["maxTotalChargeAmount"] = value["max_total_charge_amount"]
    if "configuration" in value:
        import capo_marketplace_agreement.types.variable_payment_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.variable_payment_term_configuration.serialize_cbor(
                value["configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> VariablePaymentTerm:
    out: VariablePaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("maxTotalChargeAmount") is not None:
        out["max_total_charge_amount"] = data["maxTotalChargeAmount"]
    if data.get("configuration") is not None:
        import capo_marketplace_agreement.types.variable_payment_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.variable_payment_term_configuration.deserialize_cbor(
                data["configuration"]
            )
        )
    return out
