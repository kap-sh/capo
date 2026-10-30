"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.string


class GetInstancesRequest(TypedDict, closed=True):
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetInstances</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""
    include_health_status: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether to include the instance health status checks of each instance in the response of your request.</p> <p>When set to <code>true</code>, the response includes the <code>instanceStatus</code> and <code>systemStatus</code> of each instance. When omitted or set to <code>false</code>, the response doesn't include them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstancesRequest) -> dict:
    out: dict = {}
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    if "include_health_status" in value:
        out["includeHealthStatus"] = value["include_health_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstancesRequest:
    out: GetInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    if data.get("includeHealthStatus") is not None:
        out["include_health_status"] = data["includeHealthStatus"]
    return out
