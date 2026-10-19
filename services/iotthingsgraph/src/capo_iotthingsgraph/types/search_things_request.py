"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchThingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.max_results
    import capo_iotthingsgraph.types.next_token
    import capo_iotthingsgraph.types.urn
    import capo_iotthingsgraph.types.version


class SearchThingsRequest(TypedDict, closed=True):
    entity_id: "capo_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the entity to which the things are associated.</p> <p>The IDs should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["capo_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchThingsRequest) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchThingsRequest:
    out: SearchThingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("namespaceVersion") is not None:
        out["namespace_version"] = data["namespaceVersion"]
    return out
