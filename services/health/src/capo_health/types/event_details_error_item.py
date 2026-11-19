"""Generated from Smithy shape ``com.amazonaws.health#EventDetailsErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_arn
    import capo_health.types.string


class EventDetailsErrorItem(TypedDict, closed=True):
    event_arn: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    error_name: NotRequired["capo_health.types.string.string"]
    """<p>The name of the error.</p>"""
    error_message: NotRequired["capo_health.types.string.string"]
    """<p>A message that describes the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDetailsErrorItem) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "error_name" in value:
        out["errorName"] = value["error_name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDetailsErrorItem:
    out: EventDetailsErrorItem = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("errorName") is not None:
        out["error_name"] = data["errorName"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventDetailsErrorItem) -> dict:
    out: dict = {}
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "error_name" in value:
        out["errorName"] = value["error_name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> EventDetailsErrorItem:
    out: EventDetailsErrorItem = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("errorName") is not None:
        out["error_name"] = data["errorName"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
