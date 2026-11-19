"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionInvocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.remote_source_action_arn
    import capo_mgn.types.remote_source_action_invocation_status
    import capo_mgn.types.source_server_arn
    import capo_mgn.types.ssm_command_invocation_id


class RemoteSourceActionInvocation(TypedDict, closed=True):
    source_server_arn: NotRequired["capo_mgn.types.source_server_arn.SourceServerArn"]
    """<p>The ARN of the source server.</p>"""
    remote_source_action_arn: NotRequired[
        "capo_mgn.types.remote_source_action_arn.RemoteSourceActionArn"
    ]
    """<p>The ARN of the source action.</p>"""
    ssm_command_invocation_id: NotRequired[
        "capo_mgn.types.ssm_command_invocation_id.SsmCommandInvocationID"
    ]
    """<p>The ID of the AWS Systems Manager command that runs the source action on the connector.</p>"""
    status: NotRequired[
        "capo_mgn.types.remote_source_action_invocation_status.RemoteSourceActionInvocationStatus"
    ]
    """<p>The current status of the invocation.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the command started running.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the command finished.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionInvocation) -> dict:
    out: dict = {}
    if "source_server_arn" in value:
        out["sourceServerArn"] = value["source_server_arn"]
    if "remote_source_action_arn" in value:
        out["remoteSourceActionArn"] = value["remote_source_action_arn"]
    if "ssm_command_invocation_id" in value:
        out["ssmCommandInvocationID"] = value["ssm_command_invocation_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "started_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["startedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["endedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    return out


def deserialize_json(data: dict) -> RemoteSourceActionInvocation:
    out: RemoteSourceActionInvocation = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerArn") is not None:
        out["source_server_arn"] = data["sourceServerArn"]
    if data.get("remoteSourceActionArn") is not None:
        out["remote_source_action_arn"] = data["remoteSourceActionArn"]
    if data.get("ssmCommandInvocationID") is not None:
        out["ssm_command_invocation_id"] = data["ssmCommandInvocationID"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("startedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["started_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["ended_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    return out
