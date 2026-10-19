"""Generated from Smithy shape ``com.amazonaws.codepipeline#CurrentRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.revision
    import capo_codepipeline.types.revision_change_identifier
    import capo_codepipeline.types.revision_summary
    import capo_codepipeline.types.time


class CurrentRevision(TypedDict, closed=True):
    revision: "capo_codepipeline.types.revision.Revision"
    """<p>The revision ID of the current version of an artifact.</p>"""
    change_identifier: (
        "capo_codepipeline.types.revision_change_identifier.RevisionChangeIdentifier"
    )
    """<p>The change identifier for the current revision.</p>"""
    created: NotRequired["capo_codepipeline.types.time.Time"]
    """<p>The date and time when the most recent revision of the artifact was created, in timestamp format.</p>"""
    revision_summary: NotRequired[
        "capo_codepipeline.types.revision_summary.RevisionSummary"
    ]
    """<p>The summary of the most recent revision of the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CurrentRevision) -> dict:
    out: dict = {}
    out["revision"] = value["revision"]
    out["changeIdentifier"] = value["change_identifier"]
    if "created" in value:
        import capo_codepipeline.types.time

        out["created"] = capo_codepipeline.types.time.serialize_aws_json_1_1(
            value["created"]
        )
    if "revision_summary" in value:
        out["revisionSummary"] = value["revision_summary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CurrentRevision:
    out: CurrentRevision = {}  # type: ignore[typeddict-item]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = ""
    if data.get("changeIdentifier") is not None:
        out["change_identifier"] = data["changeIdentifier"]
    else:
        out["change_identifier"] = ""
    if data.get("created") is not None:
        import capo_codepipeline.types.time

        out["created"] = capo_codepipeline.types.time.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("revisionSummary") is not None:
        out["revision_summary"] = data["revisionSummary"]
    return out
