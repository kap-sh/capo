"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportErrorDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.custom_workspace_image_import_error_details

CustomWorkspaceImageImportErrorDetailsList: TypeAlias = list[
    "capo_workspaces.types.custom_workspace_image_import_error_details.CustomWorkspaceImageImportErrorDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomWorkspaceImageImportErrorDetailsList) -> list:
    import capo_workspaces.types.custom_workspace_image_import_error_details

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.custom_workspace_image_import_error_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomWorkspaceImageImportErrorDetailsList:
    import capo_workspaces.types.custom_workspace_image_import_error_details

    out: CustomWorkspaceImageImportErrorDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.custom_workspace_image_import_error_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomWorkspaceImageImportErrorDetailsList) -> list:
    import capo_workspaces.types.custom_workspace_image_import_error_details

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.custom_workspace_image_import_error_details.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CustomWorkspaceImageImportErrorDetailsList:
    import capo_workspaces.types.custom_workspace_image_import_error_details

    out: CustomWorkspaceImageImportErrorDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.custom_workspace_image_import_error_details.deserialize_cbor(
                item
            )
        )
    return out
