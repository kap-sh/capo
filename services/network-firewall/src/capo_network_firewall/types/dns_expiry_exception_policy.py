"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DNSExpiryExceptionPolicy``."""

from typing import Literal, TypeAlias, cast

DNSExpiryExceptionPolicy: TypeAlias = Literal[
    "REJECT",
    "DROP",
    "CONTINUE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DNSExpiryExceptionPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DNSExpiryExceptionPolicy:
    return cast(DNSExpiryExceptionPolicy, data)
