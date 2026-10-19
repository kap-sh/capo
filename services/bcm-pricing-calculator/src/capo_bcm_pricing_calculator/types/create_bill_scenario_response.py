"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CreateBillScenarioResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_pricing_calculator.types.bill_interval
    import capo_bcm_pricing_calculator.types.bill_scenario_name
    import capo_bcm_pricing_calculator.types.bill_scenario_status
    import capo_bcm_pricing_calculator.types.cost_category_arn
    import capo_bcm_pricing_calculator.types.group_sharing_preference_enum
    import capo_bcm_pricing_calculator.types.resource_id


class CreateBillScenarioResponse(TypedDict, closed=True):
    id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier for the created bill scenario. </p>"""
    name: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
    ]
    """<p> The name of the created bill scenario. </p>"""
    bill_interval: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_interval.BillInterval"
    ]
    """<p> The time period covered by the bill scenario. </p>"""
    status: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_scenario_status.BillScenarioStatus"
    ]
    """<p> The current status of the bill scenario. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill scenario was created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill scenario will expire. </p>"""
    failure_message: NotRequired["str"]
    """<p> An error message if the bill scenario creation failed. </p>"""
    group_sharing_preference: NotRequired[
        "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
    ]
    """<p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>"""
    cost_category_group_sharing_preference_arn: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
    ]
    """<p>The arn of the cost category used in the reserved and prioritized group sharing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBillScenarioResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "bill_interval" in value:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["billInterval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
                value["bill_interval"]
            )
        )
    if "status" in value:
        import capo_bcm_pricing_calculator.types.bill_scenario_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_status.serialize_aws_json_1_0(
                value["status"]
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
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBillScenarioResponse:
    out: CreateBillScenarioResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("billInterval") is not None:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    if data.get("status") is not None:
        import capo_bcm_pricing_calculator.types.bill_scenario_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_status.deserialize_aws_json_1_0(
                data["status"]
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
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
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
    return out
