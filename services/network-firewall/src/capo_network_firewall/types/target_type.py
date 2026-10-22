"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TargetType``."""

from typing import Literal, TypeAlias, cast

TargetType: TypeAlias = Literal[
    "TLS_SNI",
    "HTTP_HOST",
    "AWS_ROUTE_53_RESOLVED_DOMAIN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TargetType:
    return cast(TargetType, data)
