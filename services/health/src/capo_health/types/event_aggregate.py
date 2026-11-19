"""Generated from Smithy shape ``com.amazonaws.health#EventAggregate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.aggregate_value
    import capo_health.types.count


class EventAggregate(TypedDict, closed=True):
    aggregate_value: NotRequired["capo_health.types.aggregate_value.aggregateValue"]
    """<p>The issue type for the associated count.</p>"""
    count: "capo_health.types.count.count"
    """<p>The number of events of the associated issue type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventAggregate) -> dict:
    out: dict = {}
    if "aggregate_value" in value:
        out["aggregateValue"] = value["aggregate_value"]
    out["count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> EventAggregate:
    out: EventAggregate = {}  # type: ignore[typeddict-item]
    if data.get("aggregateValue") is not None:
        out["aggregate_value"] = data["aggregateValue"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventAggregate) -> dict:
    out: dict = {}
    if "aggregate_value" in value:
        out["aggregateValue"] = value["aggregate_value"]
    out["count"] = value.get("count", 0)
    return out


def deserialize_cbor(data: dict) -> EventAggregate:
    out: EventAggregate = {}  # type: ignore[typeddict-item]
    if data.get("aggregateValue") is not None:
        out["aggregate_value"] = data["aggregateValue"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
