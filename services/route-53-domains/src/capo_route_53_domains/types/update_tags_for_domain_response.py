"""Generated from Smithy shape ``com.amazonaws.route53domains#UpdateTagsForDomainResponse``."""

from typing_extensions import TypedDict


class UpdateTagsForDomainResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTagsForDomainResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTagsForDomainResponse:
    out: UpdateTagsForDomainResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateTagsForDomainResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateTagsForDomainResponse:
    out: UpdateTagsForDomainResponse = {}  # type: ignore[typeddict-item]
    return out
