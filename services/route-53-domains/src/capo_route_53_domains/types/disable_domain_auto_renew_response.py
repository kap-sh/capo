"""Generated from Smithy shape ``com.amazonaws.route53domains#DisableDomainAutoRenewResponse``."""

from typing_extensions import TypedDict


class DisableDomainAutoRenewResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableDomainAutoRenewResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableDomainAutoRenewResponse:
    out: DisableDomainAutoRenewResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableDomainAutoRenewResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableDomainAutoRenewResponse:
    out: DisableDomainAutoRenewResponse = {}  # type: ignore[typeddict-item]
    return out
