"""Generated from Smithy shape ``com.amazonaws.codebuild#PhaseContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class PhaseContext(TypedDict, closed=True):
    status_code: NotRequired["capo_codebuild.types.string.String"]
    """<p>The status code for the context of the build phase.</p>"""
    message: NotRequired["capo_codebuild.types.string.String"]
    """<p>An explanation of the build phase's context. This might include a command ID and an exit code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhaseContext) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PhaseContext:
    out: PhaseContext = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PhaseContext) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> PhaseContext:
    out: PhaseContext = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
