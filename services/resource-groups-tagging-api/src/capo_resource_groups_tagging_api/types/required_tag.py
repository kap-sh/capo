"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#RequiredTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.cloud_formation_resource_types
    import capo_resource_groups_tagging_api.types.reporting_tag_keys
    import capo_resource_groups_tagging_api.types.resource_type


class RequiredTag(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_resource_groups_tagging_api.types.resource_type.ResourceType"
    ]
    """<p>Describes the resource type for the required tag keys.</p>"""
    cloud_formation_resource_types: NotRequired[
        "capo_resource_groups_tagging_api.types.cloud_formation_resource_types.CloudFormationResourceTypes"
    ]
    """<p>Describes the CloudFormation resource type assigned the required tag keys.</p>"""
    reporting_tag_keys: NotRequired[
        "capo_resource_groups_tagging_api.types.reporting_tag_keys.ReportingTagKeys"
    ]
    """<p>These tag keys are marked as <code>required</code> in the <code>report_required_tag_for</code> block of the effective tag policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequiredTag) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "cloud_formation_resource_types" in value:
        import capo_resource_groups_tagging_api.types.cloud_formation_resource_types

        out["CloudFormationResourceTypes"] = (
            capo_resource_groups_tagging_api.types.cloud_formation_resource_types.serialize_aws_json_1_1(
                value["cloud_formation_resource_types"]
            )
        )
    if "reporting_tag_keys" in value:
        import capo_resource_groups_tagging_api.types.reporting_tag_keys

        out["ReportingTagKeys"] = (
            capo_resource_groups_tagging_api.types.reporting_tag_keys.serialize_aws_json_1_1(
                value["reporting_tag_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequiredTag:
    out: RequiredTag = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("CloudFormationResourceTypes") is not None:
        import capo_resource_groups_tagging_api.types.cloud_formation_resource_types

        out["cloud_formation_resource_types"] = (
            capo_resource_groups_tagging_api.types.cloud_formation_resource_types.deserialize_aws_json_1_1(
                data["CloudFormationResourceTypes"]
            )
        )
    if data.get("ReportingTagKeys") is not None:
        import capo_resource_groups_tagging_api.types.reporting_tag_keys

        out["reporting_tag_keys"] = (
            capo_resource_groups_tagging_api.types.reporting_tag_keys.deserialize_aws_json_1_1(
                data["ReportingTagKeys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RequiredTag) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "cloud_formation_resource_types" in value:
        import capo_resource_groups_tagging_api.types.cloud_formation_resource_types

        out["CloudFormationResourceTypes"] = (
            capo_resource_groups_tagging_api.types.cloud_formation_resource_types.serialize_cbor(
                value["cloud_formation_resource_types"]
            )
        )
    if "reporting_tag_keys" in value:
        import capo_resource_groups_tagging_api.types.reporting_tag_keys

        out["ReportingTagKeys"] = (
            capo_resource_groups_tagging_api.types.reporting_tag_keys.serialize_cbor(
                value["reporting_tag_keys"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RequiredTag:
    out: RequiredTag = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("CloudFormationResourceTypes") is not None:
        import capo_resource_groups_tagging_api.types.cloud_formation_resource_types

        out["cloud_formation_resource_types"] = (
            capo_resource_groups_tagging_api.types.cloud_formation_resource_types.deserialize_cbor(
                data["CloudFormationResourceTypes"]
            )
        )
    if data.get("ReportingTagKeys") is not None:
        import capo_resource_groups_tagging_api.types.reporting_tag_keys

        out["reporting_tag_keys"] = (
            capo_resource_groups_tagging_api.types.reporting_tag_keys.deserialize_cbor(
                data["ReportingTagKeys"]
            )
        )
    return out
