"""Generated from Smithy shape ``com.amazonaws.amp#CreateLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.log_group_arn
    import capo_amp.types.workspace_id


class CreateLoggingConfigurationRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to create the logging configuration for.</p>"""
    log_group_arn: "capo_amp.types.log_group_arn.LogGroupArn"
    """<p>The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["logGroupArn"] = value["log_group_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateLoggingConfigurationRequest:
    out: CreateLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupArn") is not None:
        out["log_group_arn"] = data["logGroupArn"]
    else:
        out["log_group_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
