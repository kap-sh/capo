"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_pricing_calculator.types.bill_estimate_name
    import capo_bcm_pricing_calculator.types.bill_estimate_status
    import capo_bcm_pricing_calculator.types.bill_interval
    import capo_bcm_pricing_calculator.types.resource_id


class BillEstimateSummary(TypedDict, closed=True):
    id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill estimate. </p>"""
    name: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
    ]
    """<p> The name of the bill estimate. </p>"""
    status: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_estimate_status.BillEstimateStatus"
    ]
    """<p> The current status of the bill estimate. </p>"""
    bill_interval: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_interval.BillInterval"
    ]
    """<p> The time period covered by the bill estimate. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate was created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate will expire. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_bcm_pricing_calculator.types.bill_estimate_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.bill_estimate_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "bill_interval" in value:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["billInterval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
                value["bill_interval"]
            )
        )
    if "created_at" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["createdAt"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "expires_at" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillEstimateSummary:
    out: BillEstimateSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_bcm_pricing_calculator.types.bill_estimate_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.bill_estimate_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("billInterval") is not None:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["created_at"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if data.get("expiresAt") is not None:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    return out
