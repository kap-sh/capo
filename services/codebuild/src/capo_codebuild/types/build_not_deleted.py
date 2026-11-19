"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildNotDeleted``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.string


class BuildNotDeleted(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the build that could not be successfully deleted.</p>"""
    status_code: NotRequired["capo_codebuild.types.string.String"]
    """<p>Additional information about the build that could not be successfully deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildNotDeleted) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildNotDeleted:
    out: BuildNotDeleted = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildNotDeleted) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    return out


def deserialize_cbor(data: dict) -> BuildNotDeleted:
    out: BuildNotDeleted = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    return out
