"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerGroupDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.positive_integer


class DescribeContainerGroupDefinitionInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The unique identifier for the container group definition to retrieve properties for. You can use either the <code>Name</code> or <code>ARN</code> value.</p>"""
    version_number: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The specific version to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerGroupDefinitionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerGroupDefinitionInput:
    out: DescribeContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeContainerGroupDefinitionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    return out


def deserialize_cbor(data: dict) -> DescribeContainerGroupDefinitionInput:
    out: DescribeContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    return out
