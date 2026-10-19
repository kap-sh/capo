"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDataProtectionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier


class DeleteDataProtectionPolicyRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>The name or ARN of the log group that you want to delete the data protection policy for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataProtectionPolicyRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataProtectionPolicyRequest:
    out: DeleteDataProtectionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        out["log_group_identifier"] = ""
    return out
