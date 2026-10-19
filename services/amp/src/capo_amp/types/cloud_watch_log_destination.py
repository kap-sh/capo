"""Generated from Smithy shape ``com.amazonaws.amp#CloudWatchLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.log_group_arn


class CloudWatchLogDestination(TypedDict, closed=True):
    log_group_arn: "capo_amp.types.log_group_arn.LogGroupArn"
    """<p>The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogDestination) -> dict:
    out: dict = {}
    out["logGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogDestination:
    out: CloudWatchLogDestination = {}  # type: ignore[typeddict-item]
    if data.get("logGroupArn") is not None:
        out["log_group_arn"] = data["logGroupArn"]
    else:
        out["log_group_arn"] = ""
    return out
