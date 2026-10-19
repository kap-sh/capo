"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListVehiclesInFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fleet_id
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token


class ListVehiclesInFleetRequest(TypedDict, closed=True):
    fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of a fleet. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired["capo_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVehiclesInFleetRequest) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVehiclesInFleetRequest:
    out: ListVehiclesInFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
