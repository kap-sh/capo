"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#Criteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.double_criteria_condition_list
    import capo_compute_optimizer_automation.types.integer_criteria_condition_list
    import capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list
    import capo_compute_optimizer_automation.types.string_criteria_condition_list


class Criteria(TypedDict, closed=True):
    region: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria for Amazon Web Services regions where resources must be located.</p>"""
    resource_arn: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria for specific resource ARNs to include or exclude.</p>"""
    ebs_volume_type: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria for EBS volume types, such as gp2, gp3, io1, io2, st1, or sc1.</p>"""
    ebs_volume_size_in_gib: NotRequired[
        "capo_compute_optimizer_automation.types.integer_criteria_condition_list.IntegerCriteriaConditionList"
    ]
    """<p>Filter criteria for EBS volume sizes in gibibytes (GiB).</p>"""
    estimated_monthly_savings: NotRequired[
        "capo_compute_optimizer_automation.types.double_criteria_condition_list.DoubleCriteriaConditionList"
    ]
    """<p>Filter criteria for estimated monthly cost savings from the recommended action.</p>"""
    resource_tag: NotRequired[
        "capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list.ResourceTagsCriteriaConditionList"
    ]
    """<p>Filter criteria for resource tags, allowing filtering by tag key and value combinations.</p>"""
    look_back_period_in_days: NotRequired[
        "capo_compute_optimizer_automation.types.integer_criteria_condition_list.IntegerCriteriaConditionList"
    ]
    """<p>Filter criteria for the lookback period in days used to analyze resource utilization.</p>"""
    restart_needed: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_condition_list.StringCriteriaConditionList"
    ]
    """<p>Filter criteria indicating whether the recommended action requires a resource restart.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Criteria) -> dict:
    out: dict = {}
    if "region" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["region"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["region"]
            )
        )
    if "resource_arn" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["resourceArn"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["resource_arn"]
            )
        )
    if "ebs_volume_type" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["ebsVolumeType"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["ebs_volume_type"]
            )
        )
    if "ebs_volume_size_in_gib" in value:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["ebsVolumeSizeInGib"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.serialize_aws_json_1_0(
                value["ebs_volume_size_in_gib"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.double_criteria_condition_list

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.double_criteria_condition_list.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    if "resource_tag" in value:
        import capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list

        out["resourceTag"] = (
            capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list.serialize_aws_json_1_0(
                value["resource_tag"]
            )
        )
    if "look_back_period_in_days" in value:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["lookBackPeriodInDays"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.serialize_aws_json_1_0(
                value["look_back_period_in_days"]
            )
        )
    if "restart_needed" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["restartNeeded"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_aws_json_1_0(
                value["restart_needed"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Criteria:
    out: Criteria = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["region"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["region"]
            )
        )
    if data.get("resourceArn") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["resource_arn"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["resourceArn"]
            )
        )
    if data.get("ebsVolumeType") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["ebs_volume_type"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["ebsVolumeType"]
            )
        )
    if data.get("ebsVolumeSizeInGib") is not None:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["ebs_volume_size_in_gib"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.deserialize_aws_json_1_0(
                data["ebsVolumeSizeInGib"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.double_criteria_condition_list

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.double_criteria_condition_list.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    if data.get("resourceTag") is not None:
        import capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list

        out["resource_tag"] = (
            capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list.deserialize_aws_json_1_0(
                data["resourceTag"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["look_back_period_in_days"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.deserialize_aws_json_1_0(
                data["lookBackPeriodInDays"]
            )
        )
    if data.get("restartNeeded") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["restart_needed"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_aws_json_1_0(
                data["restartNeeded"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Criteria) -> dict:
    out: dict = {}
    if "region" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["region"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_cbor(
                value["region"]
            )
        )
    if "resource_arn" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["resourceArn"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_cbor(
                value["resource_arn"]
            )
        )
    if "ebs_volume_type" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["ebsVolumeType"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_cbor(
                value["ebs_volume_type"]
            )
        )
    if "ebs_volume_size_in_gib" in value:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["ebsVolumeSizeInGib"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.serialize_cbor(
                value["ebs_volume_size_in_gib"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.double_criteria_condition_list

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.double_criteria_condition_list.serialize_cbor(
                value["estimated_monthly_savings"]
            )
        )
    if "resource_tag" in value:
        import capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list

        out["resourceTag"] = (
            capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list.serialize_cbor(
                value["resource_tag"]
            )
        )
    if "look_back_period_in_days" in value:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["lookBackPeriodInDays"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.serialize_cbor(
                value["look_back_period_in_days"]
            )
        )
    if "restart_needed" in value:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["restartNeeded"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.serialize_cbor(
                value["restart_needed"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Criteria:
    out: Criteria = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["region"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_cbor(
                data["region"]
            )
        )
    if data.get("resourceArn") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["resource_arn"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_cbor(
                data["resourceArn"]
            )
        )
    if data.get("ebsVolumeType") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["ebs_volume_type"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_cbor(
                data["ebsVolumeType"]
            )
        )
    if data.get("ebsVolumeSizeInGib") is not None:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["ebs_volume_size_in_gib"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.deserialize_cbor(
                data["ebsVolumeSizeInGib"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.double_criteria_condition_list

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.double_criteria_condition_list.deserialize_cbor(
                data["estimatedMonthlySavings"]
            )
        )
    if data.get("resourceTag") is not None:
        import capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list

        out["resource_tag"] = (
            capo_compute_optimizer_automation.types.resource_tags_criteria_condition_list.deserialize_cbor(
                data["resourceTag"]
            )
        )
    if data.get("lookBackPeriodInDays") is not None:
        import capo_compute_optimizer_automation.types.integer_criteria_condition_list

        out["look_back_period_in_days"] = (
            capo_compute_optimizer_automation.types.integer_criteria_condition_list.deserialize_cbor(
                data["lookBackPeriodInDays"]
            )
        )
    if data.get("restartNeeded") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_condition_list

        out["restart_needed"] = (
            capo_compute_optimizer_automation.types.string_criteria_condition_list.deserialize_cbor(
                data["restartNeeded"]
            )
        )
    return out
