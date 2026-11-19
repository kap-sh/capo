"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfEntityLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.entity_label

ListOfEntityLabels: TypeAlias = list["capo_comprehend.types.entity_label.EntityLabel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEntityLabels) -> list:
    import capo_comprehend.types.entity_label

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.entity_label.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEntityLabels:
    import capo_comprehend.types.entity_label

    out: ListOfEntityLabels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.entity_label.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfEntityLabels) -> list:
    import capo_comprehend.types.entity_label

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.entity_label.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfEntityLabels:
    import capo_comprehend.types.entity_label

    out: ListOfEntityLabels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.entity_label.deserialize_cbor(item))
    return out
