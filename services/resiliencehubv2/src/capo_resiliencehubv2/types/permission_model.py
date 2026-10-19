"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PermissionModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.cross_account_role_list
    import capo_resiliencehubv2.types.iam_role_name


class PermissionModel(TypedDict, closed=True):
    invoker_role_name: "capo_resiliencehubv2.types.iam_role_name.IamRoleName"
    cross_account_roles: NotRequired[
        "capo_resiliencehubv2.types.cross_account_role_list.CrossAccountRoleList"
    ]
    """<p>The list of cross-account IAM role ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionModel) -> dict:
    out: dict = {}
    out["invokerRoleName"] = value["invoker_role_name"]
    if "cross_account_roles" in value:
        import capo_resiliencehubv2.types.cross_account_role_list

        out["crossAccountRoles"] = (
            capo_resiliencehubv2.types.cross_account_role_list.serialize_json(
                value["cross_account_roles"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionModel:
    out: PermissionModel = {}  # type: ignore[typeddict-item]
    if data.get("invokerRoleName") is not None:
        out["invoker_role_name"] = data["invokerRoleName"]
    else:
        out["invoker_role_name"] = ""
    if data.get("crossAccountRoles") is not None:
        import capo_resiliencehubv2.types.cross_account_role_list

        out["cross_account_roles"] = (
            capo_resiliencehubv2.types.cross_account_role_list.deserialize_json(
                data["crossAccountRoles"]
            )
        )
    return out
