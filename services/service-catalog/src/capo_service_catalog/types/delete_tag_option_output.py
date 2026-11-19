"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteTagOptionOutput``."""

from typing_extensions import TypedDict


class DeleteTagOptionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagOptionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagOptionOutput:
    out: DeleteTagOptionOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteTagOptionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteTagOptionOutput:
    out: DeleteTagOptionOutput = {}  # type: ignore[typeddict-item]
    return out
