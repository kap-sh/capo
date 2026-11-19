"""Generated from Smithy shape ``com.amazonaws.appstream#SharedImagePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.aws_account_id
    import capo_appstream.types.image_permissions


class SharedImagePermissions(TypedDict, closed=True):
    shared_account_id: NotRequired["capo_appstream.types.aws_account_id.AwsAccountId"]
    """<p>The 12-digit identifier of the AWS account with which the image is shared.</p>"""
    image_permissions: NotRequired[
        "capo_appstream.types.image_permissions.ImagePermissions"
    ]
    """<p>Describes the permissions for a shared image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedImagePermissions) -> dict:
    out: dict = {}
    if "shared_account_id" in value:
        out["sharedAccountId"] = value["shared_account_id"]
    if "image_permissions" in value:
        import capo_appstream.types.image_permissions

        out["imagePermissions"] = (
            capo_appstream.types.image_permissions.serialize_aws_json_1_1(
                value["image_permissions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SharedImagePermissions:
    out: SharedImagePermissions = {}  # type: ignore[typeddict-item]
    if data.get("sharedAccountId") is not None:
        out["shared_account_id"] = data["sharedAccountId"]
    if data.get("imagePermissions") is not None:
        import capo_appstream.types.image_permissions

        out["image_permissions"] = (
            capo_appstream.types.image_permissions.deserialize_aws_json_1_1(
                data["imagePermissions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SharedImagePermissions) -> dict:
    out: dict = {}
    if "shared_account_id" in value:
        out["sharedAccountId"] = value["shared_account_id"]
    if "image_permissions" in value:
        import capo_appstream.types.image_permissions

        out["imagePermissions"] = capo_appstream.types.image_permissions.serialize_cbor(
            value["image_permissions"]
        )
    return out


def deserialize_cbor(data: dict) -> SharedImagePermissions:
    out: SharedImagePermissions = {}  # type: ignore[typeddict-item]
    if data.get("sharedAccountId") is not None:
        out["shared_account_id"] = data["sharedAccountId"]
    if data.get("imagePermissions") is not None:
        import capo_appstream.types.image_permissions

        out["image_permissions"] = (
            capo_appstream.types.image_permissions.deserialize_cbor(
                data["imagePermissions"]
            )
        )
    return out
