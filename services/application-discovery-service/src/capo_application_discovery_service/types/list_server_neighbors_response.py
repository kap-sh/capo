"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ListServerNeighborsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.long
    import capo_application_discovery_service.types.neighbor_details_list
    import capo_application_discovery_service.types.string


class ListServerNeighborsResponse(TypedDict, closed=True):
    neighbors: "capo_application_discovery_service.types.neighbor_details_list.NeighborDetailsList"
    """<p>List of distinct servers that are one hop away from the given server.</p>"""
    next_token: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>Token to retrieve the next set of results. For example, if you specified 100 IDs for <code>ListServerNeighborsRequest$neighborConfigurationIds</code> but set <code>ListServerNeighborsRequest$maxResults</code> to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.</p>"""
    known_dependency_count: "capo_application_discovery_service.types.long.Long"
    """<p>Count of distinct servers that are one hop away from the given server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServerNeighborsResponse) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.neighbor_details_list

    out["neighbors"] = (
        capo_application_discovery_service.types.neighbor_details_list.serialize_aws_json_1_1(
            value["neighbors"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["knownDependencyCount"] = value.get("known_dependency_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServerNeighborsResponse:
    out: ListServerNeighborsResponse = {}  # type: ignore[typeddict-item]
    if data.get("neighbors") is not None:
        import capo_application_discovery_service.types.neighbor_details_list

        out["neighbors"] = (
            capo_application_discovery_service.types.neighbor_details_list.deserialize_aws_json_1_1(
                data["neighbors"]
            )
        )
    else:
        out["neighbors"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("knownDependencyCount") is not None:
        out["known_dependency_count"] = data["knownDependencyCount"]
    else:
        out["known_dependency_count"] = 0
    return out
