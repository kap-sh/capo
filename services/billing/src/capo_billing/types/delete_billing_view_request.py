"""Generated from Smithy shape ``com.amazonaws.billing#DeleteBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn


class DeleteBillingViewRequest(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    force: NotRequired["bool"]
    """<p> If set to true, forces deletion of the billing view even if it has derived resources (e.g. other billing views or budgets). Use with caution as this may break dependent resources. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBillingViewRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBillingViewRequest:
    out: DeleteBillingViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteBillingViewRequest.arn required")
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out
