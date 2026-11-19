"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchItemError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.string


class BatchItemError(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    error_code: NotRequired["capo_comprehend.types.string.String"]
    """<p>The numeric error code of the error.</p>"""
    error_message: NotRequired["capo_comprehend.types.string.String"]
    """<p>A text description of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchItemError) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchItemError:
    out: BatchItemError = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchItemError) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> BatchItemError:
    out: BatchItemError = {}  # type: ignore[typeddict-item]
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
