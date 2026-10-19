"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSyncJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.sync_job_state
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class CreateSyncJobResponse(TypedDict, closed=True):
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The SyncJob ARN.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time for the SyncJob creation.</p>"""
    state: "capo_iottwinmaker.types.sync_job_state.SyncJobState"
    """<p>The SyncJob response state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSyncJobResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> CreateSyncJobResponse:
    out: CreateSyncJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out
