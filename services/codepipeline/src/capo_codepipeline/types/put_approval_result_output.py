"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutApprovalResultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.timestamp


class PutApprovalResultOutput(TypedDict, closed=True):
    approved_at: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The timestamp showing when the approval or rejection was submitted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApprovalResultOutput) -> dict:
    out: dict = {}
    if "approved_at" in value:
        import capo_codepipeline.types.timestamp

        out["approvedAt"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["approved_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApprovalResultOutput:
    out: PutApprovalResultOutput = {}  # type: ignore[typeddict-item]
    if data.get("approvedAt") is not None:
        import capo_codepipeline.types.timestamp

        out["approved_at"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["approvedAt"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutApprovalResultOutput) -> dict:
    out: dict = {}
    if "approved_at" in value:
        import capo_codepipeline.types.timestamp

        out["approvedAt"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["approved_at"]
        )
    return out


def deserialize_cbor(data: dict) -> PutApprovalResultOutput:
    out: PutApprovalResultOutput = {}  # type: ignore[typeddict-item]
    if data.get("approvedAt") is not None:
        import capo_codepipeline.types.timestamp

        out["approved_at"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["approvedAt"]
        )
    return out
