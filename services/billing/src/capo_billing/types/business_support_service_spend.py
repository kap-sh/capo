"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportServiceSpend``."""

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError


class BusinessSupportServiceSpend(TypedDict, closed=True):
    contributing_service: "str"
    """<p>The name of the Amazon Web Services service contributing to the Support-eligible spend.</p>"""
    item_type: "str"
    """<p>The type of the line item. Valid values: <code>Usage</code>.</p>"""
    description: NotRequired["str"]
    """<p>A human-readable description of the service spend entry.</p>"""
    charge_amount: "str"
    """<p>The Support-eligible spend amount for this service.</p>"""
    currency: "str"
    """<p>The ISO 4217 currency code for the charge amount (for example, <code>USD</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportServiceSpend) -> dict:
    out: dict = {}
    out["contributingService"] = value["contributing_service"]
    out["itemType"] = value["item_type"]
    if "description" in value:
        out["description"] = value["description"]
    out["chargeAmount"] = value["charge_amount"]
    out["currency"] = value["currency"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessSupportServiceSpend:
    out: BusinessSupportServiceSpend = {}  # type: ignore[typeddict-item]
    if data.get("contributingService") is not None:
        out["contributing_service"] = data["contributingService"]
    else:
        raise DeserializationError(
            "BusinessSupportServiceSpend.contributing_service required"
        )
    if data.get("itemType") is not None:
        out["item_type"] = data["itemType"]
    else:
        raise DeserializationError("BusinessSupportServiceSpend.item_type required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("chargeAmount") is not None:
        out["charge_amount"] = data["chargeAmount"]
    else:
        raise DeserializationError("BusinessSupportServiceSpend.charge_amount required")
    if data.get("currency") is not None:
        out["currency"] = data["currency"]
    else:
        raise DeserializationError("BusinessSupportServiceSpend.currency required")
    return out
