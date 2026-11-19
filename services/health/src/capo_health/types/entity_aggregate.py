"""Generated from Smithy shape ``com.amazonaws.health#EntityAggregate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.count
    import capo_health.types.entity_statuses
    import capo_health.types.event_arn


class EntityAggregate(TypedDict, closed=True):
    event_arn: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    count: "capo_health.types.count.count"
    """<p>The number of entities that match the criteria for the specified events.</p>"""
    statuses: NotRequired["capo_health.types.entity_statuses.entityStatuses"]
    """<p>The number of affected entities aggregated by the entity status codes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityAggregate) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    out["count"] = value.get("count", 0)
    if "statuses" in value:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.serialize_aws_json_1_1(
            value["statuses"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityAggregate:
    out: EntityAggregate = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("statuses") is not None:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.deserialize_aws_json_1_1(
            data["statuses"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityAggregate) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    out["count"] = value.get("count", 0)
    if "statuses" in value:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.serialize_cbor(
            value["statuses"]
        )
    return out


def deserialize_cbor(data: dict) -> EntityAggregate:
    out: EntityAggregate = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("statuses") is not None:
        import capo_health.types.entity_statuses

        out["statuses"] = capo_health.types.entity_statuses.deserialize_cbor(
            data["statuses"]
        )
    return out
