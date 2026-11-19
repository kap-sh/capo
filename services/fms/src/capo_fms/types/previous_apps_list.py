"""Generated from Smithy shape ``com.amazonaws.fms#PreviousAppsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.apps_list
    import capo_fms.types.previous_list_version

PreviousAppsList: TypeAlias = dict[
    "capo_fms.types.previous_list_version.PreviousListVersion",
    "capo_fms.types.apps_list.AppsList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PreviousAppsList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.apps_list

        out[key] = capo_fms.types.apps_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviousAppsList:
    out: PreviousAppsList = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_fms.types.apps_list

        out[key] = capo_fms.types.apps_list.deserialize_aws_json_1_1(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: PreviousAppsList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.apps_list

        out[key] = capo_fms.types.apps_list.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> PreviousAppsList:
    out: PreviousAppsList = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_fms.types.apps_list

        out[key] = capo_fms.types.apps_list.deserialize_cbor(value)
    return out
