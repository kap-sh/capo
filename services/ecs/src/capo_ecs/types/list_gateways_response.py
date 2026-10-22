"""Generated from Smithy shape ``com.amazonaws.ecs#ListGatewaysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_summary_list
    import capo_ecs.types.string


class ListGatewaysResponse(TypedDict, closed=True):
    gateways: NotRequired["capo_ecs.types.gateway_summary_list.GatewaySummaryList"]
    """<p>The list of gateways that match the request.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListGateways</code> request. When the results of a <code>ListGateways</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewaysResponse) -> dict:
    out: dict = {}
    if "gateways" in value:
        import capo_ecs.types.gateway_summary_list

        out["gateways"] = capo_ecs.types.gateway_summary_list.serialize_aws_json_1_1(
            value["gateways"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewaysResponse:
    out: ListGatewaysResponse = {}  # type: ignore[typeddict-item]
    if data.get("gateways") is not None:
        import capo_ecs.types.gateway_summary_list

        out["gateways"] = capo_ecs.types.gateway_summary_list.deserialize_aws_json_1_1(
            data["gateways"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
