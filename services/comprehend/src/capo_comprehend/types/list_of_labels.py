"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.document_label

ListOfLabels: TypeAlias = list["capo_comprehend.types.document_label.DocumentLabel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfLabels) -> list:
    import capo_comprehend.types.document_label

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.document_label.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfLabels:
    import capo_comprehend.types.document_label

    out: ListOfLabels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.document_label.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfLabels) -> list:
    import capo_comprehend.types.document_label

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.document_label.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfLabels:
    import capo_comprehend.types.document_label

    out: ListOfLabels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.document_label.deserialize_cbor(item))
    return out
