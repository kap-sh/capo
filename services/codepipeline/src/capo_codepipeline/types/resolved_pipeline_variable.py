"""Generated from Smithy shape ``com.amazonaws.codepipeline#ResolvedPipelineVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.string


class ResolvedPipelineVariable(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The name of a pipeline-level variable.</p>"""
    resolved_value: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The resolved value of a pipeline-level variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedPipelineVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "resolved_value" in value:
        out["resolvedValue"] = value["resolved_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedPipelineVariable:
    out: ResolvedPipelineVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("resolvedValue") is not None:
        out["resolved_value"] = data["resolvedValue"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResolvedPipelineVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "resolved_value" in value:
        out["resolvedValue"] = value["resolved_value"]
    return out


def deserialize_cbor(data: dict) -> ResolvedPipelineVariable:
    out: ResolvedPipelineVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("resolvedValue") is not None:
        out["resolved_value"] = data["resolvedValue"]
    return out
