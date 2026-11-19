"""Generated from Smithy shape ``com.amazonaws.comprehend#RelationshipType``."""

from typing import Literal, TypeAlias, cast

RelationshipType: TypeAlias = Literal["CHILD",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationshipType:
    return cast(RelationshipType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelationshipType) -> str:
    return value


def deserialize_cbor(data: str) -> RelationshipType:
    return cast(RelationshipType, data)
