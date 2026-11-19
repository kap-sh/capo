"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfToxicLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.toxic_labels

ListOfToxicLabels: TypeAlias = list["capo_comprehend.types.toxic_labels.ToxicLabels"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfToxicLabels) -> list:
    import capo_comprehend.types.toxic_labels

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.toxic_labels.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfToxicLabels:
    import capo_comprehend.types.toxic_labels

    out: ListOfToxicLabels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.toxic_labels.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfToxicLabels) -> list:
    import capo_comprehend.types.toxic_labels

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.toxic_labels.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfToxicLabels:
    import capo_comprehend.types.toxic_labels

    out: ListOfToxicLabels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.toxic_labels.deserialize_cbor(item))
    return out
