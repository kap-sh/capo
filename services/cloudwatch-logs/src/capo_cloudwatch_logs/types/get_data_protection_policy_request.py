"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDataProtectionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier


class GetDataProtectionPolicyRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>The name or ARN of the log group that contains the data protection policy that you want to see.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataProtectionPolicyRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataProtectionPolicyRequest:
    out: GetDataProtectionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        out["log_group_identifier"] = ""
    return out
