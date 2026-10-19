"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftClusterStorage``."""

from typing_extensions import TypedDict


class RedshiftClusterStorage(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The name of an Amazon Redshift cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftClusterStorage) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    return out


def deserialize_json(data: dict) -> RedshiftClusterStorage:
    out: RedshiftClusterStorage = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    return out
