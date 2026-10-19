"""Generated from Smithy shape ``com.amazonaws.billing#CreateBillingViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.billing_view_arn


class CreateBillingViewResponse(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The time when the billing view was created. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBillingViewResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_billing.types._prelude.timestamp

        out["createdAt"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBillingViewResponse:
    out: CreateBillingViewResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("createdAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["created_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    return out
