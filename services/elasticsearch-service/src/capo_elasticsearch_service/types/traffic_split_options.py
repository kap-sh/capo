"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#TrafficSplitOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.traffic_percents
    import capo_elasticsearch_service.types.traffic_split_status


class TrafficSplitOptions(TypedDict, closed=True):
    current: "capo_elasticsearch_service.types.traffic_percents.TrafficPercents"
    """<p>The traffic split currently in effect.</p>"""
    target: "capo_elasticsearch_service.types.traffic_percents.TrafficPercents"
    """<p>The requested traffic split.</p>"""
    status: "capo_elasticsearch_service.types.traffic_split_status.TrafficSplitStatus"
    """<p>The status of the traffic shift.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitOptions) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.traffic_percents

    out["Current"] = capo_elasticsearch_service.types.traffic_percents.serialize_json(
        value["current"]
    )
    import capo_elasticsearch_service.types.traffic_percents

    out["Target"] = capo_elasticsearch_service.types.traffic_percents.serialize_json(
        value["target"]
    )
    import capo_elasticsearch_service.types.traffic_split_status

    out["Status"] = (
        capo_elasticsearch_service.types.traffic_split_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> TrafficSplitOptions:
    out: TrafficSplitOptions = {}  # type: ignore[typeddict-item]
    if data.get("Current") is not None:
        import capo_elasticsearch_service.types.traffic_percents

        out["current"] = (
            capo_elasticsearch_service.types.traffic_percents.deserialize_json(
                data["Current"]
            )
        )
    else:
        raise DeserializationError("TrafficSplitOptions.current required")
    if data.get("Target") is not None:
        import capo_elasticsearch_service.types.traffic_percents

        out["target"] = (
            capo_elasticsearch_service.types.traffic_percents.deserialize_json(
                data["Target"]
            )
        )
    else:
        raise DeserializationError("TrafficSplitOptions.target required")
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.traffic_split_status

        out["status"] = (
            capo_elasticsearch_service.types.traffic_split_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elasticsearch_service.types.traffic_split_status.TrafficSplitStatus",
            "",
        )
    return out
