"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthStatusDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.instance_health_status_detail

InstanceHealthStatusDetailList: TypeAlias = list[
    "capo_lightsail.types.instance_health_status_detail.InstanceHealthStatusDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthStatusDetailList) -> list:
    import capo_lightsail.types.instance_health_status_detail

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.instance_health_status_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceHealthStatusDetailList:
    import capo_lightsail.types.instance_health_status_detail

    out: InstanceHealthStatusDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lightsail.types.instance_health_status_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
