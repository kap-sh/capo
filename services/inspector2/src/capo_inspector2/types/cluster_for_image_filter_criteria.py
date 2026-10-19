"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterForImageFilterCriteria``."""

from typing_extensions import TypedDict


class ClusterForImageFilterCriteria(TypedDict, closed=True):
    resource_id: "str"
    """<p>The resource Id to be used in the filter criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterForImageFilterCriteria) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ClusterForImageFilterCriteria:
    out: ClusterForImageFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    return out
