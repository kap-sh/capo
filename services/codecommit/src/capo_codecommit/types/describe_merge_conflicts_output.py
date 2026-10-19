"""Generated from Smithy shape ``com.amazonaws.codecommit#DescribeMergeConflictsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.conflict_metadata
    import capo_codecommit.types.merge_hunks
    import capo_codecommit.types.next_token
    import capo_codecommit.types.object_id


class DescribeMergeConflictsOutput(TypedDict, closed=True):
    conflict_metadata: "capo_codecommit.types.conflict_metadata.ConflictMetadata"
    """<p>Contains metadata about the conflicts found in the merge.</p>"""
    merge_hunks: "capo_codecommit.types.merge_hunks.MergeHunks"
    """<p>A list of merge hunks of the differences between the files or lines.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""
    destination_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    source_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge base.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMergeConflictsOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.conflict_metadata

    out["conflictMetadata"] = (
        capo_codecommit.types.conflict_metadata.serialize_aws_json_1_1(
            value["conflict_metadata"]
        )
    )
    import capo_codecommit.types.merge_hunks

    out["mergeHunks"] = capo_codecommit.types.merge_hunks.serialize_aws_json_1_1(
        value["merge_hunks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["destinationCommitId"] = value["destination_commit_id"]
    out["sourceCommitId"] = value["source_commit_id"]
    if "base_commit_id" in value:
        out["baseCommitId"] = value["base_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMergeConflictsOutput:
    out: DescribeMergeConflictsOutput = {}  # type: ignore[typeddict-item]
    if data.get("conflictMetadata") is not None:
        import capo_codecommit.types.conflict_metadata

        out["conflict_metadata"] = (
            capo_codecommit.types.conflict_metadata.deserialize_aws_json_1_1(
                data["conflictMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeMergeConflictsOutput.conflict_metadata required"
        )
    if data.get("mergeHunks") is not None:
        import capo_codecommit.types.merge_hunks

        out["merge_hunks"] = capo_codecommit.types.merge_hunks.deserialize_aws_json_1_1(
            data["mergeHunks"]
        )
    else:
        out["merge_hunks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
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
