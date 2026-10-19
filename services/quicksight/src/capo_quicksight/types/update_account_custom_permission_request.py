"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAccountCustomPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.custom_permissions_name


class UpdateAccountCustomPermissionRequest(TypedDict, closed=True):
    custom_permissions_name: (
        "capo_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile that you want to apply to an account.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account for which you want to apply a custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomPermissionRequest) -> dict:
    out: dict = {}
    out["CustomPermissionsName"] = value["custom_permissions_name"]
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomPermissionRequest:
    out: UpdateAccountCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CustomPermissionsName") is not None:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    else:
        out["custom_permissions_name"] = ""
    return out
