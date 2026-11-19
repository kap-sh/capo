"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildBatchesForProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_batch_ids
    import capo_codebuild.types.string


class ListBuildBatchesForProjectOutput(TypedDict, closed=True):
    ids: NotRequired["capo_codebuild.types.build_batch_ids.BuildBatchIds"]
    """<p>An array of strings that contains the batch build identifiers.</p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to <code>ListBuildBatchesForProject</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildBatchesForProjectOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_codebuild.types.build_batch_ids

        out["ids"] = capo_codebuild.types.build_batch_ids.serialize_aws_json_1_1(
            value["ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildBatchesForProjectOutput:
    out: ListBuildBatchesForProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.build_batch_ids

        out["ids"] = capo_codebuild.types.build_batch_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBuildBatchesForProjectOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_codebuild.types.build_batch_ids

        out["ids"] = capo_codebuild.types.build_batch_ids.serialize_cbor(value["ids"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListBuildBatchesForProjectOutput:
    out: ListBuildBatchesForProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.build_batch_ids

        out["ids"] = capo_codebuild.types.build_batch_ids.deserialize_cbor(data["ids"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
