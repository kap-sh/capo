"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_cluster_id


class GetDbClusterInput(TypedDict, closed=True):
    db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbClusterInput:
    out: GetDbClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("dbClusterId") is not None:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        out["db_cluster_id"] = ""
    return out
