"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterInList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.status


class ClusterInList(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The name of the elastic cluster.</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    status: "capo_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInList) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    out["clusterArn"] = value["cluster_arn"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ClusterInList:
    out: ClusterInList = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
