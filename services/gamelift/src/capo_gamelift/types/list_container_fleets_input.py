"""Generated from Smithy shape ``com.amazonaws.gamelift#ListContainerFleetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class ListContainerFleetsInput(TypedDict, closed=True):
    container_group_definition_name: NotRequired[
        "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>The container group definition to filter the list on. Use this parameter to retrieve only those fleets that use the specified container group definition. You can specify the container group definition's name to get fleets with the latest versions. Alternatively, provide an ARN value to get fleets with a specific version number.</p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerFleetsInput) -> dict:
    out: dict = {}
    if "container_group_definition_name" in value:
        out["ContainerGroupDefinitionName"] = value["container_group_definition_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerFleetsInput:
    out: ListContainerFleetsInput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerGroupDefinitionName") is not None:
        out["container_group_definition_name"] = data["ContainerGroupDefinitionName"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListContainerFleetsInput) -> dict:
    out: dict = {}
    if "container_group_definition_name" in value:
        out["ContainerGroupDefinitionName"] = value["container_group_definition_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListContainerFleetsInput:
    out: ListContainerFleetsInput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerGroupDefinitionName") is not None:
        out["container_group_definition_name"] = data["ContainerGroupDefinitionName"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
