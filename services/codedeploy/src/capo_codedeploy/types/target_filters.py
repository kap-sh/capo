"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.filter_value_list
    import capo_codedeploy.types.target_filter_name

TargetFilters: TypeAlias = dict[
    "capo_codedeploy.types.target_filter_name.TargetFilterName",
    "capo_codedeploy.types.filter_value_list.FilterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TargetFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codedeploy.types.filter_value_list
        import capo_codedeploy.types.target_filter_name

        out[capo_codedeploy.types.target_filter_name.serialize_aws_json_1_1(key)] = (
            capo_codedeploy.types.filter_value_list.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetFilters:
    out: TargetFilters = {}
    for key, value in data.items():
        import capo_codedeploy.types.target_filter_name

        if value is None:
            continue
        import capo_codedeploy.types.filter_value_list

        out[capo_codedeploy.types.target_filter_name.deserialize_aws_json_1_1(key)] = (
            capo_codedeploy.types.filter_value_list.deserialize_aws_json_1_1(value)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: TargetFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codedeploy.types.filter_value_list
        import capo_codedeploy.types.target_filter_name

        out[capo_codedeploy.types.target_filter_name.serialize_cbor(key)] = (
            capo_codedeploy.types.filter_value_list.serialize_cbor(value)
        )
    return out


def deserialize_cbor(data: dict) -> TargetFilters:
    out: TargetFilters = {}
    for key, value in data.items():
        import capo_codedeploy.types.target_filter_name

        if value is None:
            continue
        import capo_codedeploy.types.filter_value_list

        out[capo_codedeploy.types.target_filter_name.deserialize_cbor(key)] = (
            capo_codedeploy.types.filter_value_list.deserialize_cbor(value)
        )
    return out
