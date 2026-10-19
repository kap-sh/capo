"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.billing_adjustment_error_code
    import capo_marketplace_agreement.types.client_token


class BatchCreateBillingAdjustmentError(TypedDict, closed=True):
    code: "capo_marketplace_agreement.types.billing_adjustment_error_code.BillingAdjustmentErrorCode"
    """<p>The error code indicating the reason for failure.</p>"""
    message: "str"
    """<p>A human-readable message describing the error.</p>"""
    client_token: "capo_marketplace_agreement.types.client_token.ClientToken"
    """<p>The client token of the request entry that failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentError) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.billing_adjustment_error_code

    out["code"] = (
        capo_marketplace_agreement.types.billing_adjustment_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    out["message"] = value["message"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentError:
    out: BatchCreateBillingAdjustmentError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_marketplace_agreement.types.billing_adjustment_error_code

        out["code"] = (
            capo_marketplace_agreement.types.billing_adjustment_error_code.deserialize_aws_json_1_0(
                data["code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_marketplace_agreement.types.billing_adjustment_error_code.BillingAdjustmentErrorCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
