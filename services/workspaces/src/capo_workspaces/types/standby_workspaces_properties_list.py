"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspacesPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.standby_workspaces_properties

StandbyWorkspacesPropertiesList: TypeAlias = list[
    "capo_workspaces.types.standby_workspaces_properties.StandbyWorkspacesProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspacesPropertiesList) -> list:
    import capo_workspaces.types.standby_workspaces_properties

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.standby_workspaces_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StandbyWorkspacesPropertiesList:
    import capo_workspaces.types.standby_workspaces_properties

    out: StandbyWorkspacesPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.standby_workspaces_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StandbyWorkspacesPropertiesList) -> list:
    import capo_workspaces.types.standby_workspaces_properties

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.standby_workspaces_properties.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> StandbyWorkspacesPropertiesList:
    import capo_workspaces.types.standby_workspaces_properties

    out: StandbyWorkspacesPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.standby_workspaces_properties.deserialize_cbor(item)
        )
    return out
