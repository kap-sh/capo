"""Generated from Smithy shape ``com.amazonaws.codedeploy#RawString``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.raw_string_content
    import capo_codedeploy.types.raw_string_sha256


class RawString(TypedDict, closed=True):
    content: NotRequired["capo_codedeploy.types.raw_string_content.RawStringContent"]
    """<p>The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.</p>"""
    sha256: NotRequired["capo_codedeploy.types.raw_string_sha256.RawStringSha256"]
    """<p>The SHA256 hash value of the revision content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RawString) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RawString:
    out: RawString = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RawString) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_cbor(data: dict) -> RawString:
    out: RawString = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    return out
