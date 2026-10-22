"""Generated from Smithy shape ``com.amazonaws.ecs#ListGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gateway_status_list
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class ListGatewaysRequest(TypedDict, closed=True):
    names: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The gateway names to filter the results by. You can specify up to 10 names.</p>"""
    status: NotRequired["capo_ecs.types.gateway_status_list.GatewayStatusList"]
    """<p>The gateway statuses to filter the results by.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of gateway results that <code>ListGateways</code> returns in a single page. The default is 100.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListGateways</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewaysRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_ecs.types.string_list

        out["names"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["names"])
    if "status" in value:
        import capo_ecs.types.gateway_status_list

        out["status"] = capo_ecs.types.gateway_status_list.serialize_aws_json_1_1(
            value["status"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewaysRequest:
    out: ListGatewaysRequest = {}  # type: ignore[typeddict-item]
    if data.get("names") is not None:
        import capo_ecs.types.string_list

        out["names"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["names"]
        )
    if data.get("status") is not None:
        import capo_ecs.types.gateway_status_list

        out["status"] = capo_ecs.types.gateway_status_list.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
