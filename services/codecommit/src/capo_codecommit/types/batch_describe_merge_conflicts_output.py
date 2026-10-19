"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDescribeMergeConflictsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.batch_describe_merge_conflicts_errors
    import capo_codecommit.types.conflicts
    import capo_codecommit.types.next_token
    import capo_codecommit.types.object_id


class BatchDescribeMergeConflictsOutput(TypedDict, closed=True):
    conflicts: "capo_codecommit.types.conflicts.Conflicts"
    """<p>A list of conflicts for each file, including the conflict metadata and the hunks of the differences between the files.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""
    errors: NotRequired[
        "capo_codecommit.types.batch_describe_merge_conflicts_errors.BatchDescribeMergeConflictsErrors"
    ]
    """<p>A list of any errors returned while describing the merge conflicts for each file.</p>"""
    destination_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    source_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge base.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeMergeConflictsOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.conflicts

    out["conflicts"] = capo_codecommit.types.conflicts.serialize_aws_json_1_1(
        value["conflicts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "errors" in value:
        import capo_codecommit.types.batch_describe_merge_conflicts_errors

        out["errors"] = (
            capo_codecommit.types.batch_describe_merge_conflicts_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    out["destinationCommitId"] = value["destination_commit_id"]
    out["sourceCommitId"] = value["source_commit_id"]
    if "base_commit_id" in value:
        out["baseCommitId"] = value["base_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeMergeConflictsOutput:
    out: BatchDescribeMergeConflictsOutput = {}  # type: ignore[typeddict-item]
    if data.get("conflicts") is not None:
        import capo_codecommit.types.conflicts

        out["conflicts"] = capo_codecommit.types.conflicts.deserialize_aws_json_1_1(
            data["conflicts"]
        )
    else:
        out["conflicts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("errors") is not None:
        import capo_codecommit.types.batch_describe_merge_conflicts_errors

        out["errors"] = (
            capo_codecommit.types.batch_describe_merge_conflicts_errors.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    if data.get("destinationCommitId") is not None:
        out["destination_commit_id"] = data["destinationCommitId"]
    else:
        out["destination_commit_id"] = ""
    if data.get("sourceCommitId") is not None:
        out["source_commit_id"] = data["sourceCommitId"]
    else:
        out["source_commit_id"] = ""
    if data.get("baseCommitId") is not None:
        out["base_commit_id"] = data["baseCommitId"]
    return out
