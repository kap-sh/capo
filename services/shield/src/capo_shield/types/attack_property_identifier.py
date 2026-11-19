"""Generated from Smithy shape ``com.amazonaws.shield#AttackPropertyIdentifier``."""

from typing import Literal, TypeAlias, cast

AttackPropertyIdentifier: TypeAlias = Literal[
    "DESTINATION_URL",
    "REFERRER",
    "SOURCE_ASN",
    "SOURCE_COUNTRY",
    "SOURCE_IP_ADDRESS",
    "SOURCE_USER_AGENT",
    "WORDPRESS_PINGBACK_REFLECTOR",
    "WORDPRESS_PINGBACK_SOURCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackPropertyIdentifier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttackPropertyIdentifier:
    return cast(AttackPropertyIdentifier, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttackPropertyIdentifier) -> str:
    return value


def deserialize_cbor(data: str) -> AttackPropertyIdentifier:
    return cast(AttackPropertyIdentifier, data)
