"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSandboxesForProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox_ids
    import capo_codebuild.types.string


class ListSandboxesForProjectOutput(TypedDict, closed=True):
    ids: NotRequired["capo_codebuild.types.sandbox_ids.SandboxIds"]
    """<p>Information about the requested sandbox IDs.</p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>Information about the next token to get paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSandboxesForProjectOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_codebuild.types.sandbox_ids

        out["ids"] = capo_codebuild.types.sandbox_ids.serialize_aws_json_1_1(
            value["ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSandboxesForProjectOutput:
    out: ListSandboxesForProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.sandbox_ids

        out["ids"] = capo_codebuild.types.sandbox_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSandboxesForProjectOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_codebuild.types.sandbox_ids

        out["ids"] = capo_codebuild.types.sandbox_ids.serialize_cbor(value["ids"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSandboxesForProjectOutput:
    out: ListSandboxesForProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.sandbox_ids

        out["ids"] = capo_codebuild.types.sandbox_ids.deserialize_cbor(data["ids"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
