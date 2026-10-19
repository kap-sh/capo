"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ListRoutingControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.page_token
    import capo_route53_recovery_cluster.types.routing_controls


class ListRoutingControlsResponse(TypedDict, closed=True):
    routing_controls: (
        "capo_route53_recovery_cluster.types.routing_controls.RoutingControls"
    )
    """<p>The list of routing controls.</p>"""
    next_token: NotRequired["capo_route53_recovery_cluster.types.page_token.PageToken"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRoutingControlsResponse) -> dict:
    out: dict = {}
    import capo_route53_recovery_cluster.types.routing_controls

    out["RoutingControls"] = (
        capo_route53_recovery_cluster.types.routing_controls.serialize_aws_json_1_0(
            value["routing_controls"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRoutingControlsResponse:
    out: ListRoutingControlsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RoutingControls") is not None:
        import capo_route53_recovery_cluster.types.routing_controls

        out["routing_controls"] = (
            capo_route53_recovery_cluster.types.routing_controls.deserialize_aws_json_1_0(
                data["RoutingControls"]
            )
        )
    else:
        out["routing_controls"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
