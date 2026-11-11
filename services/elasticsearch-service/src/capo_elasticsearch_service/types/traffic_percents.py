"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#TrafficPercents``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.traffic_percent


class TrafficPercents(TypedDict, closed=True):
    primary_read_traffic_percent: (
        "capo_elasticsearch_service.types.traffic_percent.TrafficPercent"
    )
    """<p>The percentage of search traffic sent to the primary cluster.</p>"""
    clone_read_traffic_percent: (
        "capo_elasticsearch_service.types.traffic_percent.TrafficPercent"
    )
    """<p>The percentage of search traffic sent to the cloned cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficPercents) -> dict:
    out: dict = {}
    out["PrimaryReadTrafficPercent"] = value.get("primary_read_traffic_percent", 0)
    out["CloneReadTrafficPercent"] = value.get("clone_read_traffic_percent", 0)
    return out


def deserialize_json(data: dict) -> TrafficPercents:
    out: TrafficPercents = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryReadTrafficPercent") is not None:
        out["primary_read_traffic_percent"] = data["PrimaryReadTrafficPercent"]
    else:
        out["primary_read_traffic_percent"] = 0
    if data.get("CloneReadTrafficPercent") is not None:
        out["clone_read_traffic_percent"] = data["CloneReadTrafficPercent"]
    else:
        out["clone_read_traffic_percent"] = 0
    return out
