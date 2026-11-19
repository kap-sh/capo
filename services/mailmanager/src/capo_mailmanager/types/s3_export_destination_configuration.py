"""Generated from Smithy shape ``com.amazonaws.mailmanager#S3ExportDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.s3_location


class S3ExportDestinationConfiguration(TypedDict, closed=True):
    s3_location: NotRequired["capo_mailmanager.types.s3_location.S3Location"]
    """<p>The S3 location to deliver the exported email data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ExportDestinationConfiguration) -> dict:
    out: dict = {}
    if "s3_location" in value:
        out["S3Location"] = value["s3_location"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ExportDestinationConfiguration:
    out: S3ExportDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("S3Location") is not None:
        out["s3_location"] = data["S3Location"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3ExportDestinationConfiguration) -> dict:
    out: dict = {}
    if "s3_location" in value:
        out["S3Location"] = value["s3_location"]
    return out


def deserialize_cbor(data: dict) -> S3ExportDestinationConfiguration:
    out: S3ExportDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("S3Location") is not None:
        out["s3_location"] = data["S3Location"]
    return out
