"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.revision
    import capo_codepipeline.types.revision_change_identifier
    import capo_codepipeline.types.timestamp


class ActionRevision(TypedDict, closed=True):
    revision_id: "capo_codepipeline.types.revision.Revision"
    """<p>The system-generated unique ID that identifies the revision number of the action.</p>"""
    revision_change_id: (
        "capo_codepipeline.types.revision_change_identifier.RevisionChangeIdentifier"
    )
    """<p>The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).</p>"""
    created: "capo_codepipeline.types.timestamp.Timestamp"
    """<p>The date and time when the most recent version of the action was created, in timestamp format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionRevision) -> dict:
    out: dict = {}
    out["revisionId"] = value["revision_id"]
    out["revisionChangeId"] = value["revision_change_id"]
    import capo_codepipeline.types.timestamp

    out["created"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
        value["created"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionRevision:
    out: ActionRevision = {}  # type: ignore[typeddict-item]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    if data.get("revisionChangeId") is not None:
        out["revision_change_id"] = data["revisionChangeId"]
    else:
        out["revision_change_id"] = ""
    if data.get("created") is not None:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    else:
        import datetime

        out["created"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
