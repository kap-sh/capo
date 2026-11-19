"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DecryptionAction``."""

from typing import Literal, TypeAlias, cast

DecryptionAction: TypeAlias = Literal[
    "DECRYPT",
    "BYPASS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecryptionAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DecryptionAction:
    return cast(DecryptionAction, data)
