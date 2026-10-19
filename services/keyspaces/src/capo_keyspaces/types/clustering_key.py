"""Generated from Smithy shape ``com.amazonaws.keyspaces#ClusteringKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.generic_string
    import capo_keyspaces.types.sort_order


class ClusteringKey(TypedDict, closed=True):
    name: "capo_keyspaces.types.generic_string.GenericString"
    """<p>The name(s) of the clustering column(s).</p>"""
    order_by: "capo_keyspaces.types.sort_order.SortOrder"
    """<p>Sets the ascendant (<code>ASC</code>) or descendant (<code>DESC</code>) order modifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusteringKey) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["orderBy"] = value["order_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ClusteringKey:
    out: ClusteringKey = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("orderBy") is not None:
        out["order_by"] = data["orderBy"]
    else:
        out["order_by"] = ""
    return out
