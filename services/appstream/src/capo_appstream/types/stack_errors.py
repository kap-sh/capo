"""Generated from Smithy shape ``com.amazonaws.appstream#StackErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.stack_error

StackErrors: TypeAlias = list["capo_appstream.types.stack_error.StackError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackErrors) -> list:
    import capo_appstream.types.stack_error

    out: list = []
    for item in value:
        out.append(capo_appstream.types.stack_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StackErrors:
    import capo_appstream.types.stack_error

    out: StackErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.stack_error.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StackErrors) -> list:
    import capo_appstream.types.stack_error

    out: list = []
    for item in value:
        out.append(capo_appstream.types.stack_error.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StackErrors:
    import capo_appstream.types.stack_error

    out: StackErrors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.stack_error.deserialize_cbor(item))
    return out
