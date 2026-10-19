"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeleteDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_cluster_id


class DeleteDbClusterInput(TypedDict, closed=True):
    db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster.</p>"""
    retain_automated_backups: NotRequired["bool"]
    """<p>Specifies whether to retain automated backups after the DB cluster is deleted. If set to true, automated backups are not deleted and can be restored later.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    if "retain_automated_backups" in value:
        out["retainAutomatedBackups"] = value["retain_automated_backups"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDbClusterInput:
    out: DeleteDbClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("dbClusterId") is not None:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        out["db_cluster_id"] = ""
    if data.get("retainAutomatedBackups") is not None:
        out["retain_automated_backups"] = data["retainAutomatedBackups"]
    return out
