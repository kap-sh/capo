"""Generated from Smithy shape ``com.amazonaws.memorydb#ParameterNameValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.parameter_name_value

ParameterNameValueList: TypeAlias = list[
    "capo_memorydb.types.parameter_name_value.ParameterNameValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNameValueList) -> list:
    import capo_memorydb.types.parameter_name_value

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.parameter_name_value.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterNameValueList:
    import capo_memorydb.types.parameter_name_value

    out: ParameterNameValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.parameter_name_value.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParameterNameValueList) -> list:
    import capo_memorydb.types.parameter_name_value

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.parameter_name_value.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ParameterNameValueList:
    import capo_memorydb.types.parameter_name_value

    out: ParameterNameValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.parameter_name_value.deserialize_cbor(item))
    return out
