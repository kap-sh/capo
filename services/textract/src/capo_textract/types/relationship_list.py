"""Generated from Smithy shape ``com.amazonaws.textract#RelationshipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.relationship

RelationshipList: TypeAlias = list["capo_textract.types.relationship.Relationship"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationshipList) -> list:
    import capo_textract.types.relationship

    out: list = []
    for item in value:
        out.append(capo_textract.types.relationship.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RelationshipList:
    import capo_textract.types.relationship

    out: RelationshipList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.relationship.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelationshipList) -> list:
    import capo_textract.types.relationship

    out: list = []
    for item in value:
        out.append(capo_textract.types.relationship.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RelationshipList:
    import capo_textract.types.relationship

    out: RelationshipList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.relationship.deserialize_cbor(item))
    return out
