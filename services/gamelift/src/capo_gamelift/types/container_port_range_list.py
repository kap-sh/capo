"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortRangeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_port_range

ContainerPortRangeList: TypeAlias = list[
    "capo_gamelift.types.container_port_range.ContainerPortRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortRangeList) -> list:
    import capo_gamelift.types.container_port_range

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_port_range.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerPortRangeList:
    import capo_gamelift.types.container_port_range

    out: ContainerPortRangeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_port_range.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: ContainerPortRangeList) -> list[Any]:
    import capo_gamelift.types.container_port_range

    return [
        capo_gamelift.types.container_port_range.redact_sensitive(item)
        for item in value
    ]
