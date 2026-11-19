"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetSandboxesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox_ids
    import capo_codebuild.types.sandboxes


class BatchGetSandboxesOutput(TypedDict, closed=True):
    sandboxes: NotRequired["capo_codebuild.types.sandboxes.Sandboxes"]
    """<p>Information about the requested sandboxes.</p>"""
    sandboxes_not_found: NotRequired["capo_codebuild.types.sandbox_ids.SandboxIds"]
    """<p>The IDs of sandboxes for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSandboxesOutput) -> dict:
    out: dict = {}
    if "sandboxes" in value:
        import capo_codebuild.types.sandboxes

        out["sandboxes"] = capo_codebuild.types.sandboxes.serialize_aws_json_1_1(
            value["sandboxes"]
        )
    if "sandboxes_not_found" in value:
        import capo_codebuild.types.sandbox_ids

        out["sandboxesNotFound"] = (
            capo_codebuild.types.sandbox_ids.serialize_aws_json_1_1(
                value["sandboxes_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSandboxesOutput:
    out: BatchGetSandboxesOutput = {}  # type: ignore[typeddict-item]
    if data.get("sandboxes") is not None:
        import capo_codebuild.types.sandboxes

        out["sandboxes"] = capo_codebuild.types.sandboxes.deserialize_aws_json_1_1(
            data["sandboxes"]
        )
    if data.get("sandboxesNotFound") is not None:
        import capo_codebuild.types.sandbox_ids

        out["sandboxes_not_found"] = (
            capo_codebuild.types.sandbox_ids.deserialize_aws_json_1_1(
                data["sandboxesNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetSandboxesOutput) -> dict:
    out: dict = {}
    if "sandboxes" in value:
        import capo_codebuild.types.sandboxes

        out["sandboxes"] = capo_codebuild.types.sandboxes.serialize_cbor(
            value["sandboxes"]
        )
    if "sandboxes_not_found" in value:
        import capo_codebuild.types.sandbox_ids

        out["sandboxesNotFound"] = capo_codebuild.types.sandbox_ids.serialize_cbor(
            value["sandboxes_not_found"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetSandboxesOutput:
    out: BatchGetSandboxesOutput = {}  # type: ignore[typeddict-item]
    if data.get("sandboxes") is not None:
        import capo_codebuild.types.sandboxes

        out["sandboxes"] = capo_codebuild.types.sandboxes.deserialize_cbor(
            data["sandboxes"]
        )
    if data.get("sandboxesNotFound") is not None:
        import capo_codebuild.types.sandbox_ids

        out["sandboxes_not_found"] = capo_codebuild.types.sandbox_ids.deserialize_cbor(
            data["sandboxesNotFound"]
        )
    return out
