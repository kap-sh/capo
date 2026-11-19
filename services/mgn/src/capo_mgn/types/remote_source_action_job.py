"""Generated from Smithy shape ``com.amazonaws.mgn#RemoteSourceActionJob``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.arn
    import capo_mgn.types.connector_arn
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.remote_source_action_arns
    import capo_mgn.types.remote_source_action_job_id
    import capo_mgn.types.remote_source_action_job_status
    import capo_mgn.types.source_server_arns
    import capo_mgn.types.tags_map


class RemoteSourceActionJob(TypedDict, closed=True):
    remote_source_action_job_id: NotRequired[
        "capo_mgn.types.remote_source_action_job_id.RemoteSourceActionJobID"
    ]
    """<p>The unique identifier of the job.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    status: NotRequired[
        "capo_mgn.types.remote_source_action_job_status.RemoteSourceActionJobStatus"
    ]
    """<p>The current status of the job.</p>"""
    source_server_arns: NotRequired[
        "capo_mgn.types.source_server_arns.SourceServerArns"
    ]
    """<p>The ARNs of the source servers that the job runs on.</p>"""
    remote_source_action_arns: NotRequired[
        "capo_mgn.types.remote_source_action_arns.RemoteSourceActionArns"
    ]
    """<p>The ARNs of the source actions that the job runs.</p>"""
    connector_arn: NotRequired["capo_mgn.types.connector_arn.ConnectorArn"]
    """<p>The ARN of the connector that runs the job.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job started running.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job completed or failed.</p>"""
    status_reason: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>The reason the job failed.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteSourceActionJob) -> dict:
    out: dict = {}
    if "remote_source_action_job_id" in value:
        out["remoteSourceActionJobID"] = value["remote_source_action_job_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "source_server_arns" in value:
        import capo_mgn.types.source_server_arns

        out["sourceServerArns"] = capo_mgn.types.source_server_arns.serialize_json(
            value["source_server_arns"]
        )
    if "remote_source_action_arns" in value:
        import capo_mgn.types.remote_source_action_arns

        out["remoteSourceActionArns"] = (
            capo_mgn.types.remote_source_action_arns.serialize_json(
                value["remote_source_action_arns"]
            )
        )
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
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
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RemoteSourceActionJob:
    out: RemoteSourceActionJob = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionJobID") is not None:
        out["remote_source_action_job_id"] = data["remoteSourceActionJobID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("sourceServerArns") is not None:
        import capo_mgn.types.source_server_arns

        out["source_server_arns"] = capo_mgn.types.source_server_arns.deserialize_json(
            data["sourceServerArns"]
        )
    if data.get("remoteSourceActionArns") is not None:
        import capo_mgn.types.remote_source_action_arns

        out["remote_source_action_arns"] = (
            capo_mgn.types.remote_source_action_arns.deserialize_json(
                data["remoteSourceActionArns"]
            )
        )
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
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
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: RemoteSourceActionJob) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
