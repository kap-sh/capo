"""Generated from Smithy shape ``com.amazonaws.appstream#StackAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.stack_attribute

StackAttributes: TypeAlias = list["capo_appstream.types.stack_attribute.StackAttribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackAttributes) -> list:
    import capo_appstream.types.stack_attribute

    out: list = []
    for item in value:
        out.append(capo_appstream.types.stack_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StackAttributes:
    import capo_appstream.types.stack_attribute

    out: StackAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.stack_attribute.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackAttributes) -> list:
    import capo_appstream.types.stack_attribute

    out: list = []
    for item in value:
        out.append(capo_appstream.types.stack_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StackAttributes:
    import capo_appstream.types.stack_attribute

    out: StackAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.stack_attribute.deserialize_cbor(item))
    return out
