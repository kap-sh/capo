"""Generated from Smithy shape ``com.amazonaws.route53domains#EnableDomainAutoRenewResponse``."""

from typing_extensions import TypedDict


class EnableDomainAutoRenewResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableDomainAutoRenewResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableDomainAutoRenewResponse:
    out: EnableDomainAutoRenewResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableDomainAutoRenewResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableDomainAutoRenewResponse:
    out: EnableDomainAutoRenewResponse = {}  # type: ignore[typeddict-item]
    return out
