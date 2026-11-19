"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.application

ApplicationList: TypeAlias = list["capo_workspaces.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationList) -> list:
    import capo_workspaces.types.application

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.application.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationList:
    import capo_workspaces.types.application

    out: ApplicationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.application.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationList) -> list:
    import capo_workspaces.types.application

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.application.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ApplicationList:
    import capo_workspaces.types.application

    out: ApplicationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.application.deserialize_cbor(item))
    return out
