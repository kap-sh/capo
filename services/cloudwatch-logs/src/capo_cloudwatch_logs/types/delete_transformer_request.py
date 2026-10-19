"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteTransformerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier


class DeleteTransformerRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>Specify either the name or ARN of the log group to delete the transformer for. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTransformerRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTransformerRequest:
    out: DeleteTransformerRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        out["log_group_identifier"] = ""
    return out
