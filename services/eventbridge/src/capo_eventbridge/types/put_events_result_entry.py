"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutEventsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.error_code
    import capo_eventbridge.types.error_message
    import capo_eventbridge.types.event_id


class PutEventsResultEntry(TypedDict, closed=True):
    event_id: NotRequired["capo_eventbridge.types.event_id.EventId"]
    """<p>The ID of the event.</p>"""
    error_code: NotRequired["capo_eventbridge.types.error_code.ErrorCode"]
    """<p>The error code that indicates why the event submission failed.</p> <p>Retryable errors include:</p> <ul> <li> <p> <code> <a href="https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html">InternalFailure</a> </code> </p> <p>The request processing has failed because of an unknown error, exception or failure.</p> </li> <li> <p> <code> <a href="https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html">ThrottlingException</a> </code> </p> <p>The request was denied due to request throttling.</p> </li> </ul> <p>Non-retryable errors include:</p> <ul> <li> <p> <code> <a href="https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html">AccessDeniedException</a> </code> </p> <p>You do not have sufficient access to perform this action.</p> </li> <li> <p> <code>InvalidAccountIdException</code> </p> <p>The account ID provided is not valid.</p> </li> <li> <p> <code>InvalidArgument</code> </p> <p>A specified parameter is not valid.</p> </li> <li> <p> <code>MalformedDetail</code> </p> <p>The JSON provided is not valid.</p> </li> <li> <p> <code>RedactionFailure</code> </p> <p>Redacting the CloudTrail event failed.</p> </li> <li> <p> <code>NotAuthorizedForSourceException</code> </p> <p>You do not have permissions to publish events with this source onto this event bus.</p> </li> <li> <p> <code>NotAuthorizedForDetailTypeException</code> </p> <p>You do not have permissions to publish events with this detail type onto this event bus.</p> </li> </ul>"""
    error_message: NotRequired["capo_eventbridge.types.error_message.ErrorMessage"]
    """<p>The error message that explains why the event submission failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsResultEntry) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventsResultEntry:
    out: PutEventsResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
