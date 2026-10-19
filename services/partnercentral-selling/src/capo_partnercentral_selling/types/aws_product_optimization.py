"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductOptimization``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.monetary_amount


class AwsProductOptimization(TypedDict, closed=True):
    description: "str"
    """<p>Human-readable explanation of the optimization strategy.</p>"""
    savings_amount: "capo_partnercentral_selling.types.monetary_amount.MonetaryAmount"
    """<p>Quantified cost savings achievable by implementing this optimization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductOptimization) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    out["SavingsAmount"] = value["savings_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductOptimization:
    out: AwsProductOptimization = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("SavingsAmount") is not None:
        out["savings_amount"] = data["SavingsAmount"]
    else:
        out["savings_amount"] = ""
    return out


def redact_sensitive(value: AwsProductOptimization) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "savings_amount" in value:
        out["savings_amount"] = "*** Sensitive Data Redacted ***"
    return out
