"""Generated from Smithy shape ``com.amazonaws.health#LifecycleEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.lifecycle_event

LifecycleEventList: TypeAlias = list["capo_health.types.lifecycle_event.LifecycleEvent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleEventList) -> list:
    import capo_health.types.lifecycle_event

    out: list = []
    for item in value:
        out.append(capo_health.types.lifecycle_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LifecycleEventList:
    import capo_health.types.lifecycle_event

    out: LifecycleEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.lifecycle_event.deserialize_aws_json_1_1(item))
    return out
