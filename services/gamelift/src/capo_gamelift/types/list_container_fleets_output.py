"""Generated from Smithy shape ``com.amazonaws.gamelift#ListContainerFleetsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_fleet_list
    import capo_gamelift.types.non_zero_and_max_string


class ListContainerFleetsOutput(TypedDict, closed=True):
    container_fleets: NotRequired[
        "capo_gamelift.types.container_fleet_list.ContainerFleetList"
    ]
    """<p>A collection of container fleet objects for all fleets that match the request criteria.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerFleetsOutput) -> dict:
    out: dict = {}
    if "container_fleets" in value:
        import capo_gamelift.types.container_fleet_list

        out["ContainerFleets"] = (
            capo_gamelift.types.container_fleet_list.serialize_aws_json_1_1(
                value["container_fleets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerFleetsOutput:
    out: ListContainerFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerFleets") is not None:
        import capo_gamelift.types.container_fleet_list

        out["container_fleets"] = (
            capo_gamelift.types.container_fleet_list.deserialize_aws_json_1_1(
                data["ContainerFleets"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListContainerFleetsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "container_fleets" in value:
        import capo_gamelift.types.container_fleet_list

        out["container_fleets"] = (
            capo_gamelift.types.container_fleet_list.redact_sensitive(
                value["container_fleets"]
            )
        )
    return out
