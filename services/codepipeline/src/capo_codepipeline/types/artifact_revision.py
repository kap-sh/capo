"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_name
    import capo_codepipeline.types.revision
    import capo_codepipeline.types.revision_change_identifier
    import capo_codepipeline.types.revision_summary
    import capo_codepipeline.types.timestamp
    import capo_codepipeline.types.url


class ArtifactRevision(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.artifact_name.ArtifactName"]
    """<p>The name of an artifact. This name might be system-generated, such as "MyApp", or defined by the user when an action is created.</p>"""
    revision_id: NotRequired["capo_codepipeline.types.revision.Revision"]
    """<p>The revision ID of the artifact.</p>"""
    revision_change_identifier: NotRequired[
        "capo_codepipeline.types.revision_change_identifier.RevisionChangeIdentifier"
    ]
    """<p>An additional identifier for a revision, such as a commit date or, for artifacts stored in Amazon S3 buckets, the ETag value.</p>"""
    revision_summary: NotRequired[
        "capo_codepipeline.types.revision_summary.RevisionSummary"
    ]
    """<p>Summary information about the most recent revision of the artifact. For GitHub and CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a <code>codepipeline-artifact-revision-summary</code> key specified in the object metadata.</p>"""
    created: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time when the most recent revision of the artifact was created, in timestamp format.</p>"""
    revision_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The commit ID for the artifact revision. For artifacts stored in GitHub or CodeCommit repositories, the commit ID is linked to a commit details page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactRevision) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "revision_change_identifier" in value:
        out["revisionChangeIdentifier"] = value["revision_change_identifier"]
    if "revision_summary" in value:
        out["revisionSummary"] = value["revision_summary"]
    if "created" in value:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactRevision:
    out: ArtifactRevision = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("revisionChangeIdentifier") is not None:
        out["revision_change_identifier"] = data["revisionChangeIdentifier"]
    if data.get("revisionSummary") is not None:
        out["revision_summary"] = data["revisionSummary"]
    if data.get("created") is not None:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("revisionUrl") is not None:
        out["revision_url"] = data["revisionUrl"]
    return out
