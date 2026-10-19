"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.max_results
    import capo_keyspaces.types.next_token


class ListTypesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_keyspaces.types.next_token.NextToken"]
    """<p> The pagination token. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation. </p>"""
    max_results: NotRequired["capo_keyspaces.types.max_results.MaxResults"]
    """<p> The total number of types to return in the output. If the total number of types available is more than the value specified, a <code>NextToken</code> is provided in the output. To resume pagination, provide the <code>NextToken</code> value as an argument of a subsequent API invocation. </p>"""
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace that contains the listed types. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTypesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["keyspaceName"] = value["keyspace_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTypesRequest:
    out: ListTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    return out
