"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateImagePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.aws_account_id
    import capo_appstream.types.image_permissions
    import capo_appstream.types.name


class UpdateImagePermissionsRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the private image.</p>"""
    shared_account_id: NotRequired["capo_appstream.types.aws_account_id.AwsAccountId"]
    """<p>The 12-digit identifier of the AWS account for which you want add or update image permissions.</p>"""
    image_permissions: NotRequired[
        "capo_appstream.types.image_permissions.ImagePermissions"
    ]
    """<p>The permissions for the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    if "image_permissions" in value:
        import capo_appstream.types.image_permissions

        out["ImagePermissions"] = (
            capo_appstream.types.image_permissions.serialize_aws_json_1_1(
                value["image_permissions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImagePermissionsRequest:
    out: UpdateImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    if data.get("ImagePermissions") is not None:
        import capo_appstream.types.image_permissions

        out["image_permissions"] = (
            capo_appstream.types.image_permissions.deserialize_aws_json_1_1(
                data["ImagePermissions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    if "image_permissions" in value:
        import capo_appstream.types.image_permissions

        out["ImagePermissions"] = capo_appstream.types.image_permissions.serialize_cbor(
            value["image_permissions"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateImagePermissionsRequest:
    out: UpdateImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    if data.get("ImagePermissions") is not None:
        import capo_appstream.types.image_permissions

        out["image_permissions"] = (
            capo_appstream.types.image_permissions.deserialize_cbor(
                data["ImagePermissions"]
            )
        )
    return out
