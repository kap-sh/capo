"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.client_properties_result

ClientPropertiesList: TypeAlias = list[
    "capo_workspaces.types.client_properties_result.ClientPropertiesResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientPropertiesList) -> list:
    import capo_workspaces.types.client_properties_result

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.client_properties_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClientPropertiesList:
    import capo_workspaces.types.client_properties_result

    out: ClientPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.client_properties_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClientPropertiesList) -> list:
    import capo_workspaces.types.client_properties_result

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.client_properties_result.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ClientPropertiesList:
    import capo_workspaces.types.client_properties_result

    out: ClientPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.client_properties_result.deserialize_cbor(item)
        )
    return out
