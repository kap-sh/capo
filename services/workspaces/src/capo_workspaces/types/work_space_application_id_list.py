"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.work_space_application_id

WorkSpaceApplicationIdList: TypeAlias = list[
    "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplicationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkSpaceApplicationIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkSpaceApplicationIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> WorkSpaceApplicationIdList:
    return [item for item in data if item is not None]
