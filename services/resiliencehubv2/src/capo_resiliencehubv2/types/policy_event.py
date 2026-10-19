"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.event_actor
    import capo_resiliencehubv2.types.policy_event_details
    import capo_resiliencehubv2.types.policy_event_type
    import capo_resiliencehubv2.types.uuid


class PolicyEvent(TypedDict, closed=True):
    event_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the event.</p>"""
    timestamp: "datetime.datetime"
    """<p>The time the event occurred.</p>"""
    event_type: "capo_resiliencehubv2.types.policy_event_type.PolicyEventType"
    """<p>The type of the event.</p>"""
    policy_arn: "capo_resiliencehubv2.types.arn.Arn"
    actor: "capo_resiliencehubv2.types.event_actor.EventActor"
    event_details: "capo_resiliencehubv2.types.policy_event_details.PolicyEventDetails"
    """<p>The details of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEvent) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_resiliencehubv2.types.policy_event_type

    out["eventType"] = capo_resiliencehubv2.types.policy_event_type.serialize_json(
        value["event_type"]
    )
    out["policyArn"] = value["policy_arn"]
    import capo_resiliencehubv2.types.event_actor

    out["actor"] = capo_resiliencehubv2.types.event_actor.serialize_json(value["actor"])
    import capo_resiliencehubv2.types.policy_event_details

    out["eventDetails"] = (
        capo_resiliencehubv2.types.policy_event_details.serialize_json(
            value["event_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> PolicyEvent:
    out: PolicyEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("timestamp") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("eventType") is not None:
        import capo_resiliencehubv2.types.policy_event_type

        out["event_type"] = (
            capo_resiliencehubv2.types.policy_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        import typing

        out["event_type"] = typing.cast(
            "capo_resiliencehubv2.types.policy_event_type.PolicyEventType", ""
        )
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("actor") is not None:
        import capo_resiliencehubv2.types.event_actor

        out["actor"] = capo_resiliencehubv2.types.event_actor.deserialize_json(
            data["actor"]
        )
    else:
        raise DeserializationError("PolicyEvent.actor required")
    if data.get("eventDetails") is not None:
        import capo_resiliencehubv2.types.policy_event_details

        out["event_details"] = (
            capo_resiliencehubv2.types.policy_event_details.deserialize_json(
                data["eventDetails"]
            )
        )
    else:
        raise DeserializationError("PolicyEvent.event_details required")
    return out
