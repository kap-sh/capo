"""Generated from Smithy shape ``com.amazonaws.ecs#AccessTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.access_type

AccessTypeList: TypeAlias = list["capo_ecs.types.access_type.AccessType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessTypeList) -> list:
    import capo_ecs.types.access_type

    out: list = []
    for item in value:
        out.append(capo_ecs.types.access_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccessTypeList:
    import capo_ecs.types.access_type

    out: AccessTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.access_type.deserialize_aws_json_1_1(item))
    return out
