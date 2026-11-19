"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.work_space_application

WorkSpaceApplicationList: TypeAlias = list[
    "capo_workspaces.types.work_space_application.WorkSpaceApplication"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplicationList) -> list:
    import capo_workspaces.types.work_space_application

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.work_space_application.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkSpaceApplicationList:
    import capo_workspaces.types.work_space_application

    out: WorkSpaceApplicationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.work_space_application.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkSpaceApplicationList) -> list:
    import capo_workspaces.types.work_space_application

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.work_space_application.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WorkSpaceApplicationList:
    import capo_workspaces.types.work_space_application

    out: WorkSpaceApplicationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.work_space_application.deserialize_cbor(item))
    return out
