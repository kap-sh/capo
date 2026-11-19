"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ContactType``."""

from typing import Literal, TypeAlias, cast

ContactType: TypeAlias = Literal["ACCEPTOR",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContactType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContactType:
    return cast(ContactType, data)
