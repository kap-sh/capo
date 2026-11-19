"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.routing_target

RoutingTargetList: TypeAlias = list["capo_sagemaker.types.routing_target.RoutingTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingTargetList) -> list:
    import capo_sagemaker.types.routing_target

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.routing_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RoutingTargetList:
    import capo_sagemaker.types.routing_target

    out: RoutingTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sagemaker.types.routing_target.deserialize_aws_json_1_1(item))
    return out
