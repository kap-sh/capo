"""Generated from Smithy shape ``com.amazonaws.billing#UpdateBillingViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.billing_view_arn


class UpdateBillingViewResponse(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p> The time when the billing view was last updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillingViewResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "updated_at" in value:
        import capo_billing.types._prelude.timestamp

        out["updatedAt"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillingViewResponse:
    out: UpdateBillingViewResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("updatedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["updated_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
