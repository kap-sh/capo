"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutLogGroupDeletionProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.deletion_protection_enabled
    import capo_cloudwatch_logs.types.log_group_identifier


class PutLogGroupDeletionProtectionRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    r"""<p>The name or ARN of the log group.</p> <p>Type: String</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512.</p> <p>Pattern: <code>[\.\-_/#A-Za-z0-9]+</code> </p> <p>Required: Yes</p>"""
    deletion_protection_enabled: "capo_cloudwatch_logs.types.deletion_protection_enabled.DeletionProtectionEnabled"
    """<p>Whether to enable deletion protection.</p> <p>Type: Boolean</p> <p>Required: Yes</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLogGroupDeletionProtectionRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLogGroupDeletionProtectionRequest:
    out: PutLogGroupDeletionProtectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        out["log_group_identifier"] = ""
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    return out
