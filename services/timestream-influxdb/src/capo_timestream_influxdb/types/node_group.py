"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#NodeGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.instance_mode_list


class NodeGroup(TypedDict, closed=True):
    instance_modes: "capo_timestream_influxdb.types.instance_mode_list.InstanceModeList"
    """<p>The functions that the nodes in this group perform. Provide from 1 to 4 unique modes. Valid modes:</p> <ul> <li> <p>INGEST – Nodes in this mode ingest data. Across all node groups, INGEST nodes must total between 1 and 4.</p> </li> <li> <p>QUERY – Nodes in this mode query data. Across all node groups, QUERY nodes must total between 0 and 14.</p> </li> <li> <p>COMPACT – Nodes in this mode compact data. Exactly one node across all node groups must have this mode. If the cluster has more than three non-compaction nodes, place the COMPACT node in its own dedicated node group.</p> </li> <li> <p>PROCESS – Nodes in this mode process data with the processing engine.</p> </li> </ul>"""
    instance_type: "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    """<p>The Timestream for InfluxDB DB instance type to run InfluxDB on for the nodes in this group.</p>"""
    count: "int"
    """<p>The number of nodes in this group. Valid values are 1 to 13.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeGroup) -> dict:
    out: dict = {}
    import capo_timestream_influxdb.types.instance_mode_list

    out["instanceModes"] = (
        capo_timestream_influxdb.types.instance_mode_list.serialize_aws_json_1_0(
            value["instance_modes"]
        )
    )
    import capo_timestream_influxdb.types.db_instance_type

    out["instanceType"] = (
        capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
            value["instance_type"]
        )
    )
    out["count"] = value["count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NodeGroup:
    out: NodeGroup = {}  # type: ignore[typeddict-item]
    if data.get("instanceModes") is not None:
        import capo_timestream_influxdb.types.instance_mode_list

        out["instance_modes"] = (
            capo_timestream_influxdb.types.instance_mode_list.deserialize_aws_json_1_0(
                data["instanceModes"]
            )
        )
    else:
        out["instance_modes"] = []
    if data.get("instanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["instanceType"]
            )
        )
    else:
        import typing

        out["instance_type"] = typing.cast(
            "capo_timestream_influxdb.types.db_instance_type.DbInstanceType", ""
        )
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
