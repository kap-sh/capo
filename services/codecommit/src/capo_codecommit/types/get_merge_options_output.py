"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.merge_options
    import capo_codecommit.types.object_id


class GetMergeOptionsOutput(TypedDict, closed=True):
    merge_options: "capo_codecommit.types.merge_options.MergeOptions"
    """<p>The merge option or strategy used to merge the code.</p>"""
    source_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    destination_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The commit ID of the merge base.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeOptionsOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.merge_options

    out["mergeOptions"] = capo_codecommit.types.merge_options.serialize_aws_json_1_1(
        value["merge_options"]
    )
    out["sourceCommitId"] = value["source_commit_id"]
    out["destinationCommitId"] = value["destination_commit_id"]
    out["baseCommitId"] = value["base_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeOptionsOutput:
    out: GetMergeOptionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("mergeOptions") is not None:
        import capo_codecommit.types.merge_options

        out["merge_options"] = (
            capo_codecommit.types.merge_options.deserialize_aws_json_1_1(
                data["mergeOptions"]
            )
        )
    else:
        out["merge_options"] = []
    if data.get("sourceCommitId") is not None:
        out["source_commit_id"] = data["sourceCommitId"]
    else:
        out["source_commit_id"] = ""
    if data.get("destinationCommitId") is not None:
        out["destination_commit_id"] = data["destinationCommitId"]
    else:
        out["destination_commit_id"] = ""
    if data.get("baseCommitId") is not None:
        out["base_commit_id"] = data["baseCommitId"]
    else:
        out["base_commit_id"] = ""
    return out
