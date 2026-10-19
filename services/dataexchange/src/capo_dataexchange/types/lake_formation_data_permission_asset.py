"""Generated from Smithy shape ``com.amazonaws.dataexchange#LakeFormationDataPermissionAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.lake_formation_data_permission_details
    import capo_dataexchange.types.lake_formation_data_permission_type
    import capo_dataexchange.types.list_of_lf_permissions
    import capo_dataexchange.types.role_arn


class LakeFormationDataPermissionAsset(TypedDict, closed=True):
    lake_formation_data_permission_details: "capo_dataexchange.types.lake_formation_data_permission_details.LakeFormationDataPermissionDetails"
    """<p>Details about the AWS Lake Formation data permission.</p>"""
    lake_formation_data_permission_type: "capo_dataexchange.types.lake_formation_data_permission_type.LakeFormationDataPermissionType"
    """<p>The data permission type.</p>"""
    permissions: "capo_dataexchange.types.list_of_lf_permissions.ListOfLFPermissions"
    """<p>The permissions granted to the subscribers on the resource.</p>"""
    role_arn: NotRequired["capo_dataexchange.types.role_arn.RoleArn"]
    """<p>The IAM role's ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions to AWS Lake Formation data permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationDataPermissionAsset) -> dict:
    out: dict = {}
    import capo_dataexchange.types.lake_formation_data_permission_details

    out["LakeFormationDataPermissionDetails"] = (
        capo_dataexchange.types.lake_formation_data_permission_details.serialize_json(
            value["lake_formation_data_permission_details"]
        )
    )
    out["LakeFormationDataPermissionType"] = value[
        "lake_formation_data_permission_type"
    ]
    import capo_dataexchange.types.list_of_lf_permissions

    out["Permissions"] = capo_dataexchange.types.list_of_lf_permissions.serialize_json(
        value["permissions"]
    )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> LakeFormationDataPermissionAsset:
    out: LakeFormationDataPermissionAsset = {}  # type: ignore[typeddict-item]
    if data.get("LakeFormationDataPermissionDetails") is not None:
        import capo_dataexchange.types.lake_formation_data_permission_details

        out["lake_formation_data_permission_details"] = (
            capo_dataexchange.types.lake_formation_data_permission_details.deserialize_json(
                data["LakeFormationDataPermissionDetails"]
            )
        )
    else:
        raise DeserializationError(
            "LakeFormationDataPermissionAsset.lake_formation_data_permission_details required"
        )
    if data.get("LakeFormationDataPermissionType") is not None:
        out["lake_formation_data_permission_type"] = data[
            "LakeFormationDataPermissionType"
        ]
    else:
        out["lake_formation_data_permission_type"] = ""
    if data.get("Permissions") is not None:
        import capo_dataexchange.types.list_of_lf_permissions

        out["permissions"] = (
            capo_dataexchange.types.list_of_lf_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        out["permissions"] = []
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
