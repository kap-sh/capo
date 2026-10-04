"""Generated from Smithy shape ``com.amazonaws.health#ServiceLifecycleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.service_lifecycle

ServiceLifecycleList: TypeAlias = list[
    "capo_health.types.service_lifecycle.ServiceLifecycle"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLifecycleList) -> list:
    import capo_health.types.service_lifecycle

    out: list = []
    for item in value:
        out.append(capo_health.types.service_lifecycle.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceLifecycleList:
    import capo_health.types.service_lifecycle

    out: ServiceLifecycleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.service_lifecycle.deserialize_aws_json_1_1(item))
    return out
