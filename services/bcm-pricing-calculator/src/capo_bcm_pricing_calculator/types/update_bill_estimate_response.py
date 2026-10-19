"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdateBillEstimateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_pricing_calculator.types.bill_estimate_cost_summary
    import capo_bcm_pricing_calculator.types.bill_estimate_name
    import capo_bcm_pricing_calculator.types.bill_estimate_status
    import capo_bcm_pricing_calculator.types.bill_interval
    import capo_bcm_pricing_calculator.types.cost_category_arn
    import capo_bcm_pricing_calculator.types.group_sharing_preference_enum
    import capo_bcm_pricing_calculator.types.resource_id


class UpdateBillEstimateResponse(TypedDict, closed=True):
    id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the updated bill estimate. </p>"""
    name: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
    ]
    """<p> The updated name of the bill estimate. </p>"""
    status: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_estimate_status.BillEstimateStatus"
    ]
    """<p> The current status of the updated bill estimate. </p>"""
    failure_message: NotRequired["str"]
    """<p> An error message if the bill estimate update failed. </p>"""
    bill_interval: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_interval.BillInterval"
    ]
    """<p> The time period covered by the updated bill estimate. </p>"""
    cost_summary: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_estimate_cost_summary.BillEstimateCostSummary"
    ]
    """<p> A summary of the updated estimated costs. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate was originally created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The updated expiration timestamp for the bill estimate. </p>"""
    group_sharing_preference: NotRequired[
        "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
    ]
    """<p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>"""
    cost_category_group_sharing_preference_arn: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
    ]
    """<p>The arn of the cost category used in the reserved and prioritized group sharing.</p>"""
    cost_category_group_sharing_preference_effective_date: NotRequired[
        "datetime.datetime"
    ]
    """<p>Timestamp of the effective date of the cost category used in the group sharing settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillEstimateResponse) -> dict:
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
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "bill_interval" in value:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["billInterval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
                value["bill_interval"]
            )
        )
    if "cost_summary" in value:
        import capo_bcm_pricing_calculator.types.bill_estimate_cost_summary

        out["costSummary"] = (
            capo_bcm_pricing_calculator.types.bill_estimate_cost_summary.serialize_aws_json_1_0(
                value["cost_summary"]
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
    if "group_sharing_preference" in value:
        import capo_bcm_pricing_calculator.types.group_sharing_preference_enum

        out["groupSharingPreference"] = (
            capo_bcm_pricing_calculator.types.group_sharing_preference_enum.serialize_aws_json_1_0(
                value["group_sharing_preference"]
            )
        )
    if "cost_category_group_sharing_preference_arn" in value:
        out["costCategoryGroupSharingPreferenceArn"] = value[
            "cost_category_group_sharing_preference_arn"
        ]
    if "cost_category_group_sharing_preference_effective_date" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["costCategoryGroupSharingPreferenceEffectiveDate"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["cost_category_group_sharing_preference_effective_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillEstimateResponse:
    out: UpdateBillEstimateResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("billInterval") is not None:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    if data.get("costSummary") is not None:
        import capo_bcm_pricing_calculator.types.bill_estimate_cost_summary

        out["cost_summary"] = (
            capo_bcm_pricing_calculator.types.bill_estimate_cost_summary.deserialize_aws_json_1_0(
                data["costSummary"]
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
    if data.get("groupSharingPreference") is not None:
        import capo_bcm_pricing_calculator.types.group_sharing_preference_enum

        out["group_sharing_preference"] = (
            capo_bcm_pricing_calculator.types.group_sharing_preference_enum.deserialize_aws_json_1_0(
                data["groupSharingPreference"]
            )
        )
    if data.get("costCategoryGroupSharingPreferenceArn") is not None:
        out["cost_category_group_sharing_preference_arn"] = data[
            "costCategoryGroupSharingPreferenceArn"
        ]
    if data.get("costCategoryGroupSharingPreferenceEffectiveDate") is not None:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["cost_category_group_sharing_preference_effective_date"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["costCategoryGroupSharingPreferenceEffectiveDate"]
            )
        )
    return out
