"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteContainerGroupDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.whole_number


class DeleteContainerGroupDefinitionInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The unique identifier for the container group definition to delete. You can use either the <code>Name</code> or <code>ARN</code> value.</p>"""
    version_number: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The specific version to delete.</p>"""
    version_count_to_retain: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The number of most recent versions to keep while deleting all older versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContainerGroupDefinitionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "version_count_to_retain" in value:
        out["VersionCountToRetain"] = value["version_count_to_retain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContainerGroupDefinitionInput:
    out: DeleteContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    if data.get("VersionCountToRetain") is not None:
        out["version_count_to_retain"] = data["VersionCountToRetain"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteContainerGroupDefinitionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "version_count_to_retain" in value:
        out["VersionCountToRetain"] = value["version_count_to_retain"]
    return out


def deserialize_cbor(data: dict) -> DeleteContainerGroupDefinitionInput:
    out: DeleteContainerGroupDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    if data.get("VersionCountToRetain") is not None:
        out["version_count_to_retain"] = data["VersionCountToRetain"]
    return out
