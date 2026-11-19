"""Generated from Smithy shape ``com.amazonaws.kms#ResourceOwnerType``."""

from typing import Literal, TypeAlias, cast

"""<p>Identifies whose KMS keys <a>ListKeys</a> lists. <code>SELF</code> identifies the KMS keys in your Amazon Web Services account. <code>OTHER_ACCOUNTS_VIA_RAM</code> identifies the KMS keys that other Amazon Web Services accounts shared with your Amazon Web Services account through Resource Access Manager (RAM).</p>"""
ResourceOwnerType: TypeAlias = Literal[
    "SELF",
    "OTHER_ACCOUNTS_VIA_RAM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceOwnerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceOwnerType:
    return cast(ResourceOwnerType, data)
