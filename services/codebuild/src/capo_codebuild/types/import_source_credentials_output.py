"""Generated from Smithy shape ``com.amazonaws.codebuild#ImportSourceCredentialsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class ImportSourceCredentialsOutput(TypedDict, closed=True):
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSourceCredentialsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSourceCredentialsOutput:
    out: ImportSourceCredentialsOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportSourceCredentialsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> ImportSourceCredentialsOutput:
    out: ImportSourceCredentialsOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
