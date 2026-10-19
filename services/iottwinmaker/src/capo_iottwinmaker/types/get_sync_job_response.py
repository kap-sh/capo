"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetSyncJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.role_arn
    import capo_iottwinmaker.types.sync_job_status
    import capo_iottwinmaker.types.sync_source
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class GetSyncJobResponse(TypedDict, closed=True):
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The sync job ARN.</p>"""
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the sync job.</p>"""
    sync_source: "capo_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync soucre.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>"""
    sync_role: "capo_iottwinmaker.types.role_arn.RoleArn"
    """<p>The sync IAM role.</p>"""
    status: "capo_iottwinmaker.types.sync_job_status.SyncJobStatus"
    """<p>The SyncJob response status.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The creation date and time.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The update date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSyncJobResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["workspaceId"] = value["workspace_id"]
    out["syncSource"] = value["sync_source"]
    out["syncRole"] = value["sync_role"]
    import capo_iottwinmaker.types.sync_job_status

    out["status"] = capo_iottwinmaker.types.sync_job_status.serialize_json(
        value["status"]
    )
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> GetSyncJobResponse:
    out: GetSyncJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("syncSource") is not None:
        out["sync_source"] = data["syncSource"]
    else:
        out["sync_source"] = ""
    if data.get("syncRole") is not None:
        out["sync_role"] = data["syncRole"]
    else:
        out["sync_role"] = ""
    if data.get("status") is not None:
        import capo_iottwinmaker.types.sync_job_status

        out["status"] = capo_iottwinmaker.types.sync_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetSyncJobResponse.status required")
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
