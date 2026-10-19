"""Generated from Smithy shape ``com.amazonaws.health#EventAccountFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.account_id
    import capo_health.types.event_arn


class EventAccountFilter(TypedDict, closed=True):
    event_arn: "capo_health.types.event_arn.eventArn"
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    aws_account_id: NotRequired["capo_health.types.account_id.accountId"]
    """<p>The 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventAccountFilter) -> dict:
    out: dict = {}
    out["eventArn"] = value["event_arn"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventAccountFilter:
    out: EventAccountFilter = {}  # type: ignore[typeddict-item]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    else:
        out["event_arn"] = ""
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    return out
