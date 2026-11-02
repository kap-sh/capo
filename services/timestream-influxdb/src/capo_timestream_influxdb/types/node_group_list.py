"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#NodeGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.node_group

NodeGroupList: TypeAlias = list["capo_timestream_influxdb.types.node_group.NodeGroup"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeGroupList) -> list:
    import capo_timestream_influxdb.types.node_group

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.node_group.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NodeGroupList:
    import capo_timestream_influxdb.types.node_group

    out: NodeGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_timestream_influxdb.types.node_group.deserialize_aws_json_1_0(item)
        )
    return out
