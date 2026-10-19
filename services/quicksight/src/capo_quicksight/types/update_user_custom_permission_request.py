"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateUserCustomPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.custom_permissions_name
    import capo_quicksight.types.namespace
    import capo_quicksight.types.user_name


class UpdateUserCustomPermissionRequest(TypedDict, closed=True):
    user_name: "capo_quicksight.types.user_name.UserName"
    """<p>The username of the user that you want to update custom permissions for.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permission configuration that you want to update.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that the user belongs to.</p>"""
    custom_permissions_name: (
        "capo_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserCustomPermissionRequest) -> dict:
    out: dict = {}
    out["CustomPermissionsName"] = value["custom_permissions_name"]
    return out


def deserialize_json(data: dict) -> UpdateUserCustomPermissionRequest:
    out: UpdateUserCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CustomPermissionsName") is not None:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    else:
        out["custom_permissions_name"] = ""
    return out
