"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ExecutionParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.execution_parameter_key
    import capo_service_catalog.types.execution_parameter_value_list

ExecutionParameterMap: TypeAlias = dict[
    "capo_service_catalog.types.execution_parameter_key.ExecutionParameterKey",
    "capo_service_catalog.types.execution_parameter_value_list.ExecutionParameterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExecutionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.execution_parameter_value_list

        out[key] = (
            capo_service_catalog.types.execution_parameter_value_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionParameterMap:
    out: ExecutionParameterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_service_catalog.types.execution_parameter_value_list

        out[key] = (
            capo_service_catalog.types.execution_parameter_value_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ExecutionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.execution_parameter_value_list

        out[key] = (
            capo_service_catalog.types.execution_parameter_value_list.serialize_cbor(
                value
            )
        )
    return out


def deserialize_cbor(data: dict) -> ExecutionParameterMap:
    out: ExecutionParameterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_service_catalog.types.execution_parameter_value_list

        out[key] = (
            capo_service_catalog.types.execution_parameter_value_list.deserialize_cbor(
                value
            )
        )
    return out
