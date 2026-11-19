"""Generated from Smithy shape ``com.amazonaws.lightsail#SubdomainAssociationAction``."""

from typing import Literal, TypeAlias, cast

SubdomainAssociationAction: TypeAlias = Literal[
    "ASSOCIATE",
    "DISASSOCIATE",
    "TRANSFER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubdomainAssociationAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubdomainAssociationAction:
    return cast(SubdomainAssociationAction, data)
