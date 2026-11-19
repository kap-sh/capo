"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EndTimeBehaviorReasonCode``."""

from typing import Literal, TypeAlias, cast

EndTimeBehaviorReasonCode: TypeAlias = Literal[
    "PROPOSER_RENEW_OPTED_OUT",
    "ACCEPTOR_RENEW_OPTED_OUT",
    "NO_RENEWAL_TERM",
    "RENEWAL_LIMIT_EXHAUSTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndTimeBehaviorReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EndTimeBehaviorReasonCode:
    return cast(EndTimeBehaviorReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndTimeBehaviorReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> EndTimeBehaviorReasonCode:
    return cast(EndTimeBehaviorReasonCode, data)
