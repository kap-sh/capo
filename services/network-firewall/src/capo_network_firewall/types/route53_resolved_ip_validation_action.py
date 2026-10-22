"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Route53ResolvedIPValidationAction``."""

from typing import Literal, TypeAlias, cast

Route53ResolvedIPValidationAction: TypeAlias = Literal[
    "REJECT",
    "DROP",
    "ALERT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53ResolvedIPValidationAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Route53ResolvedIPValidationAction:
    return cast(Route53ResolvedIPValidationAction, data)
