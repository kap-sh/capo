"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetBuildBatchesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_batch_ids


class BatchGetBuildBatchesInput(TypedDict, closed=True):
    ids: "capo_codebuild.types.build_batch_ids.BuildBatchIds"
    """<p>An array that contains the batch build identifiers to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBuildBatchesInput) -> dict:
    out: dict = {}
    import capo_codebuild.types.build_batch_ids

    out["ids"] = capo_codebuild.types.build_batch_ids.serialize_aws_json_1_1(
        value["ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBuildBatchesInput:
    out: BatchGetBuildBatchesInput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.build_batch_ids

        out["ids"] = capo_codebuild.types.build_batch_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        out["ids"] = []
    return out
