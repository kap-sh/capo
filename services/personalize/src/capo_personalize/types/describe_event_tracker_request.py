"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeEventTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeEventTrackerRequest(TypedDict, closed=True):
    event_tracker_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the event tracker to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTrackerRequest) -> dict:
    out: dict = {}
    out["eventTrackerArn"] = value["event_tracker_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTrackerRequest:
    out: DescribeEventTrackerRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventTrackerArn") is not None:
        out["event_tracker_arn"] = data["eventTrackerArn"]
    else:
        out["event_tracker_arn"] = ""
    return out
