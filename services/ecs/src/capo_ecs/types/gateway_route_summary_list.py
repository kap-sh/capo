"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_summary

GatewayRouteSummaryList: TypeAlias = list[
    "capo_ecs.types.gateway_route_summary.GatewayRouteSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteSummaryList) -> list:
    import capo_ecs.types.gateway_route_summary

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_route_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewayRouteSummaryList:
    import capo_ecs.types.gateway_route_summary

    out: GatewayRouteSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gateway_route_summary.deserialize_aws_json_1_1(item))
    return out
