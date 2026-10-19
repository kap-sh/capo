"""Generated from Smithy shape ``com.amazonaws.iotsitewise#WorkspaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.workspace_name
    import capo_iotsitewise.types.workspace_status


class WorkspaceSummary(TypedDict, closed=True):
    name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the workspace.</p>"""
    status: "capo_iotsitewise.types.workspace_status.WorkspaceStatus"
    """<p>The status of the workspace.</p>"""
    created_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the workspace was created, in Unix epoch time.</p>"""
    updated_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the workspace was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_iotsitewise.types.workspace_status

    out["status"] = capo_iotsitewise.types.workspace_status.serialize_json(
        value["status"]
    )
    import capo_iotsitewise.types.timestamp

    out["createdAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_iotsitewise.types.timestamp

    out["updatedAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> WorkspaceSummary:
    out: WorkspaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.workspace_status

        out["status"] = capo_iotsitewise.types.workspace_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("WorkspaceSummary.status required")
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["created_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["updated_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
