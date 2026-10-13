"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#MonetaryValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.currency_code


class MonetaryValue(TypedDict, closed=True):
    amount: "str"
    """<p>Specifies the payment amount.</p>"""
    currency_code: "capo_partnercentral_selling.types.currency_code.CurrencyCode"
    """<p>Specifies the payment currency. Accepted values are <code>USD</code> (US Dollars) and <code>EUR</code> (Euros). If the AWS Partition is <code>aws-eusc</code> (AWS European Sovereign Cloud), the currency code must be <code>EUR</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonetaryValue) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import capo_partnercentral_selling.types.currency_code

    out["CurrencyCode"] = (
        capo_partnercentral_selling.types.currency_code.serialize_aws_json_1_0(
            value["currency_code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonetaryValue:
    out: MonetaryValue = {}  # type: ignore[typeddict-item]
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        raise DeserializationError("MonetaryValue.amount required")
    if data.get("CurrencyCode") is not None:
        import capo_partnercentral_selling.types.currency_code

        out["currency_code"] = (
            capo_partnercentral_selling.types.currency_code.deserialize_aws_json_1_0(
                data["CurrencyCode"]
            )
        )
    else:
        raise DeserializationError("MonetaryValue.currency_code required")
    return out


def redact_sensitive(value: MonetaryValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "currency_code" in value:
        out["currency_code"] = "*** Sensitive Data Redacted ***"
    return out
