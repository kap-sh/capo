"""Generated from Smithy shape ``com.amazonaws.codebuild#ExportedEnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.string


class ExportedEnvironmentVariable(TypedDict, closed=True):
    name: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of the exported environment variable.</p>"""
    value: NotRequired["capo_codebuild.types.string.String"]
    """<p>The value assigned to the exported environment variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportedEnvironmentVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportedEnvironmentVariable:
    out: ExportedEnvironmentVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportedEnvironmentVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> ExportedEnvironmentVariable:
    out: ExportedEnvironmentVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
