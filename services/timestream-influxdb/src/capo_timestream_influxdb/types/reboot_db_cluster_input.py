"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RebootDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_instance_id_list


class RebootDbClusterInput(TypedDict, closed=True):
    db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to reboot.</p>"""
    instance_ids: NotRequired[
        "capo_timestream_influxdb.types.db_instance_id_list.DbInstanceIdList"
    ]
    """<p>A list of service-generated unique DB Instance Ids belonging to the DB Cluster to reboot.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    if "instance_ids" in value:
        import capo_timestream_influxdb.types.db_instance_id_list

        out["instanceIds"] = (
            capo_timestream_influxdb.types.db_instance_id_list.serialize_aws_json_1_0(
                value["instance_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootDbClusterInput:
    out: RebootDbClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("dbClusterId") is not None:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        out["db_cluster_id"] = ""
    if data.get("instanceIds") is not None:
        import capo_timestream_influxdb.types.db_instance_id_list

        out["instance_ids"] = (
            capo_timestream_influxdb.types.db_instance_id_list.deserialize_aws_json_1_0(
                data["instanceIds"]
            )
        )
    return out
