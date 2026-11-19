"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetBuildBatchesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_batch_ids
    import capo_codebuild.types.build_batches


class BatchGetBuildBatchesOutput(TypedDict, closed=True):
    build_batches: NotRequired["capo_codebuild.types.build_batches.BuildBatches"]
    """<p>An array of <code>BuildBatch</code> objects that represent the retrieved batch builds.</p>"""
    build_batches_not_found: NotRequired[
        "capo_codebuild.types.build_batch_ids.BuildBatchIds"
    ]
    """<p>An array that contains the identifiers of any batch builds that are not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBuildBatchesOutput) -> dict:
    out: dict = {}
    if "build_batches" in value:
        import capo_codebuild.types.build_batches

        out["buildBatches"] = capo_codebuild.types.build_batches.serialize_aws_json_1_1(
            value["build_batches"]
        )
    if "build_batches_not_found" in value:
        import capo_codebuild.types.build_batch_ids

        out["buildBatchesNotFound"] = (
            capo_codebuild.types.build_batch_ids.serialize_aws_json_1_1(
                value["build_batches_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBuildBatchesOutput:
    out: BatchGetBuildBatchesOutput = {}  # type: ignore[typeddict-item]
    if data.get("buildBatches") is not None:
        import capo_codebuild.types.build_batches

        out["build_batches"] = (
            capo_codebuild.types.build_batches.deserialize_aws_json_1_1(
                data["buildBatches"]
            )
        )
    if data.get("buildBatchesNotFound") is not None:
        import capo_codebuild.types.build_batch_ids

        out["build_batches_not_found"] = (
            capo_codebuild.types.build_batch_ids.deserialize_aws_json_1_1(
                data["buildBatchesNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetBuildBatchesOutput) -> dict:
    out: dict = {}
    if "build_batches" in value:
        import capo_codebuild.types.build_batches

        out["buildBatches"] = capo_codebuild.types.build_batches.serialize_cbor(
            value["build_batches"]
        )
    if "build_batches_not_found" in value:
        import capo_codebuild.types.build_batch_ids

        out["buildBatchesNotFound"] = (
            capo_codebuild.types.build_batch_ids.serialize_cbor(
                value["build_batches_not_found"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetBuildBatchesOutput:
    out: BatchGetBuildBatchesOutput = {}  # type: ignore[typeddict-item]
    if data.get("buildBatches") is not None:
        import capo_codebuild.types.build_batches

        out["build_batches"] = capo_codebuild.types.build_batches.deserialize_cbor(
            data["buildBatches"]
        )
    if data.get("buildBatchesNotFound") is not None:
        import capo_codebuild.types.build_batch_ids

        out["build_batches_not_found"] = (
            capo_codebuild.types.build_batch_ids.deserialize_cbor(
                data["buildBatchesNotFound"]
            )
        )
    return out
