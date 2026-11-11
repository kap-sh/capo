"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#TrafficSplitRequestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.traffic_percent
    import capo_elasticsearch_service.types.traffic_strategy


class TrafficSplitRequestOptions(TypedDict, closed=True):
    strategy: "capo_elasticsearch_service.types.traffic_strategy.TrafficStrategy"
    """<p>The traffic shifting strategy. The only valid value is <code>ShiftReadTrafficPercent</code>.</p>"""
    clone_read_traffic_percent: (
        "capo_elasticsearch_service.types.traffic_percent.TrafficPercent"
    )
    """<p>The percentage of search traffic, from 0 to 100, to send to the cloned cluster. The rest goes to the primary cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitRequestOptions) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.traffic_strategy

    out["Strategy"] = capo_elasticsearch_service.types.traffic_strategy.serialize_json(
        value["strategy"]
    )
    out["CloneReadTrafficPercent"] = value.get("clone_read_traffic_percent", 0)
    return out


def deserialize_json(data: dict) -> TrafficSplitRequestOptions:
    out: TrafficSplitRequestOptions = {}  # type: ignore[typeddict-item]
    if data.get("Strategy") is not None:
        import capo_elasticsearch_service.types.traffic_strategy

        out["strategy"] = (
            capo_elasticsearch_service.types.traffic_strategy.deserialize_json(
                data["Strategy"]
            )
        )
    else:
        import typing

        out["strategy"] = typing.cast(
            "capo_elasticsearch_service.types.traffic_strategy.TrafficStrategy", ""
        )
    if data.get("CloneReadTrafficPercent") is not None:
        out["clone_read_traffic_percent"] = data["CloneReadTrafficPercent"]
    else:
        out["clone_read_traffic_percent"] = 0
    return out
