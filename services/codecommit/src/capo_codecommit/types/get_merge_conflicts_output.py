"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeConflictsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.conflict_metadata_list
    import capo_codecommit.types.is_mergeable
    import capo_codecommit.types.next_token
    import capo_codecommit.types.object_id


class GetMergeConflictsOutput(TypedDict, closed=True):
    mergeable: "capo_codecommit.types.is_mergeable.IsMergeable"
    """<p>A Boolean value that indicates whether the code is mergeable by the specified merge option.</p>"""
    destination_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    source_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge base.</p>"""
    conflict_metadata_list: (
        "capo_codecommit.types.conflict_metadata_list.ConflictMetadataList"
    )
    """<p>A list of metadata for any conflicting files. If the specified merge strategy is FAST_FORWARD_MERGE, this list is always empty.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeConflictsOutput) -> dict:
    out: dict = {}
    out["mergeable"] = value.get("mergeable", False)
    out["destinationCommitId"] = value["destination_commit_id"]
    out["sourceCommitId"] = value["source_commit_id"]
    if "base_commit_id" in value:
        out["baseCommitId"] = value["base_commit_id"]
    import capo_codecommit.types.conflict_metadata_list

    out["conflictMetadataList"] = (
        capo_codecommit.types.conflict_metadata_list.serialize_aws_json_1_1(
            value["conflict_metadata_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeConflictsOutput:
    out: GetMergeConflictsOutput = {}  # type: ignore[typeddict-item]
    if data.get("mergeable") is not None:
        out["mergeable"] = data["mergeable"]
    else:
        out["mergeable"] = False
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
    if data.get("conflictMetadataList") is not None:
        import capo_codecommit.types.conflict_metadata_list

        out["conflict_metadata_list"] = (
            capo_codecommit.types.conflict_metadata_list.deserialize_aws_json_1_1(
                data["conflictMetadataList"]
            )
        )
    else:
        out["conflict_metadata_list"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
