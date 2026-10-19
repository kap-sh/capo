"""Generated from Smithy shape ``com.amazonaws.billing#AdditionalCharge``."""

from typing_extensions import NotRequired, TypedDict


class AdditionalCharge(TypedDict, closed=True):
    description: "str"
    """<p>A description of the additional charge.</p>"""
    amount: NotRequired["str"]
    """<p>The charge amount.</p>"""
    charge_type: NotRequired["str"]
    """<p>The type of additional charge.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdditionalCharge) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    if "amount" in value:
        out["amount"] = value["amount"]
    if "charge_type" in value:
        out["chargeType"] = value["charge_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AdditionalCharge:
    out: AdditionalCharge = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("chargeType") is not None:
        out["charge_type"] = data["chargeType"]
    return out
