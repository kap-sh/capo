"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetInstances``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_scaling_group_name_list
    import capo_codedeploy.types.ec2_tag_filter_list
    import capo_codedeploy.types.ec2_tag_set


class TargetInstances(TypedDict, closed=True):
    tag_filters: NotRequired[
        "capo_codedeploy.types.ec2_tag_filter_list.EC2TagFilterList"
    ]
    """<p>The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as <code>ec2TagSet</code>.</p>"""
    auto_scaling_groups: NotRequired[
        "capo_codedeploy.types.auto_scaling_group_name_list.AutoScalingGroupNameList"
    ]
    """<p>The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.</p>"""
    ec2_tag_set: NotRequired["capo_codedeploy.types.ec2_tag_set.EC2TagSet"]
    """<p>Information about the groups of Amazon EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as <code>tagFilters</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetInstances) -> dict:
    out: dict = {}
    if "tag_filters" in value:
        import capo_codedeploy.types.ec2_tag_filter_list

        out["tagFilters"] = (
            capo_codedeploy.types.ec2_tag_filter_list.serialize_aws_json_1_1(
                value["tag_filters"]
            )
        )
    if "auto_scaling_groups" in value:
        import capo_codedeploy.types.auto_scaling_group_name_list

        out["autoScalingGroups"] = (
            capo_codedeploy.types.auto_scaling_group_name_list.serialize_aws_json_1_1(
                value["auto_scaling_groups"]
            )
        )
    if "ec2_tag_set" in value:
        import capo_codedeploy.types.ec2_tag_set

        out["ec2TagSet"] = capo_codedeploy.types.ec2_tag_set.serialize_aws_json_1_1(
            value["ec2_tag_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetInstances:
    out: TargetInstances = {}  # type: ignore[typeddict-item]
    if data.get("tagFilters") is not None:
        import capo_codedeploy.types.ec2_tag_filter_list

        out["tag_filters"] = (
            capo_codedeploy.types.ec2_tag_filter_list.deserialize_aws_json_1_1(
                data["tagFilters"]
            )
        )
    if data.get("autoScalingGroups") is not None:
        import capo_codedeploy.types.auto_scaling_group_name_list

        out["auto_scaling_groups"] = (
            capo_codedeploy.types.auto_scaling_group_name_list.deserialize_aws_json_1_1(
                data["autoScalingGroups"]
            )
        )
    if data.get("ec2TagSet") is not None:
        import capo_codedeploy.types.ec2_tag_set

        out["ec2_tag_set"] = capo_codedeploy.types.ec2_tag_set.deserialize_aws_json_1_1(
            data["ec2TagSet"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetInstances) -> dict:
    out: dict = {}
    if "tag_filters" in value:
        import capo_codedeploy.types.ec2_tag_filter_list

        out["tagFilters"] = capo_codedeploy.types.ec2_tag_filter_list.serialize_cbor(
            value["tag_filters"]
        )
    if "auto_scaling_groups" in value:
        import capo_codedeploy.types.auto_scaling_group_name_list

        out["autoScalingGroups"] = (
            capo_codedeploy.types.auto_scaling_group_name_list.serialize_cbor(
                value["auto_scaling_groups"]
            )
        )
    if "ec2_tag_set" in value:
        import capo_codedeploy.types.ec2_tag_set

        out["ec2TagSet"] = capo_codedeploy.types.ec2_tag_set.serialize_cbor(
            value["ec2_tag_set"]
        )
    return out


def deserialize_cbor(data: dict) -> TargetInstances:
    out: TargetInstances = {}  # type: ignore[typeddict-item]
    if data.get("tagFilters") is not None:
        import capo_codedeploy.types.ec2_tag_filter_list

        out["tag_filters"] = capo_codedeploy.types.ec2_tag_filter_list.deserialize_cbor(
            data["tagFilters"]
        )
    if data.get("autoScalingGroups") is not None:
        import capo_codedeploy.types.auto_scaling_group_name_list

        out["auto_scaling_groups"] = (
            capo_codedeploy.types.auto_scaling_group_name_list.deserialize_cbor(
                data["autoScalingGroups"]
            )
        )
    if data.get("ec2TagSet") is not None:
        import capo_codedeploy.types.ec2_tag_set

        out["ec2_tag_set"] = capo_codedeploy.types.ec2_tag_set.deserialize_cbor(
            data["ec2TagSet"]
        )
    return out
