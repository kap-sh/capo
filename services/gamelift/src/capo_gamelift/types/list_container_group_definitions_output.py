"""Generated from Smithy shape ``com.amazonaws.gamelift#ListContainerGroupDefinitionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_list
    import capo_gamelift.types.non_zero_and_max_string


class ListContainerGroupDefinitionsOutput(TypedDict, closed=True):
    container_group_definitions: NotRequired[
        "capo_gamelift.types.container_group_definition_list.ContainerGroupDefinitionList"
    ]
    """<p>A result set of container group definitions that match the request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerGroupDefinitionsOutput) -> dict:
    out: dict = {}
    if "container_group_definitions" in value:
        import capo_gamelift.types.container_group_definition_list

        out["ContainerGroupDefinitions"] = (
            capo_gamelift.types.container_group_definition_list.serialize_aws_json_1_1(
                value["container_group_definitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerGroupDefinitionsOutput:
    out: ListContainerGroupDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerGroupDefinitions") is not None:
        import capo_gamelift.types.container_group_definition_list

        out["container_group_definitions"] = (
            capo_gamelift.types.container_group_definition_list.deserialize_aws_json_1_1(
                data["ContainerGroupDefinitions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListContainerGroupDefinitionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "container_group_definitions" in value:
        import capo_gamelift.types.container_group_definition_list

        out["container_group_definitions"] = (
            capo_gamelift.types.container_group_definition_list.redact_sensitive(
                value["container_group_definitions"]
            )
        )
    return out
