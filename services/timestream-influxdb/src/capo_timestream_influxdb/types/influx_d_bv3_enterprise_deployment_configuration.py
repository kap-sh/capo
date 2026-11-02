"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InfluxDBv3EnterpriseDeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.node_group_list


class InfluxDBv3EnterpriseDeploymentConfiguration(TypedDict, closed=True):
    node_groups: "capo_timestream_influxdb.types.node_group_list.NodeGroupList"
    """<p>The node groups that make up the cluster. Across all node groups, the cluster must include 1 to 4 nodes with the INGEST mode, 0 to 14 nodes with the QUERY mode, and exactly one node with the COMPACT mode.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InfluxDBv3EnterpriseDeploymentConfiguration) -> dict:
    out: dict = {}
    import capo_timestream_influxdb.types.node_group_list

    out["nodeGroups"] = (
        capo_timestream_influxdb.types.node_group_list.serialize_aws_json_1_0(
            value["node_groups"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InfluxDBv3EnterpriseDeploymentConfiguration:
    out: InfluxDBv3EnterpriseDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("nodeGroups") is not None:
        import capo_timestream_influxdb.types.node_group_list

        out["node_groups"] = (
            capo_timestream_influxdb.types.node_group_list.deserialize_aws_json_1_0(
                data["nodeGroups"]
            )
        )
    else:
        out["node_groups"] = []
    return out
