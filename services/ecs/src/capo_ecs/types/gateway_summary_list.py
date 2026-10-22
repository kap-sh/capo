"""Generated from Smithy shape ``com.amazonaws.ecs#GatewaySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.gateway_summary

GatewaySummaryList: TypeAlias = list["capo_ecs.types.gateway_summary.GatewaySummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewaySummaryList) -> list:
    import capo_ecs.types.gateway_summary

    out: list = []
    for item in value:
        out.append(capo_ecs.types.gateway_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GatewaySummaryList:
    import capo_ecs.types.gateway_summary

    out: GatewaySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.gateway_summary.deserialize_aws_json_1_1(item))
    return out
