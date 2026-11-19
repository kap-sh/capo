"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationS3Response``."""

from typing_extensions import TypedDict


class UpdateLocationS3Response(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationS3Response) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationS3Response:
    out: UpdateLocationS3Response = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationS3Response) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationS3Response:
    out: UpdateLocationS3Response = {}  # type: ignore[typeddict-item]
    return out
