"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagePermissionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name
    import capo_appstream.types.shared_image_permissions_list
    import capo_appstream.types.string


class DescribeImagePermissionsResult(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the private image.</p>"""
    shared_image_permissions_list: NotRequired[
        "capo_appstream.types.shared_image_permissions_list.SharedImagePermissionsList"
    ]
    """<p>The permissions for a private image that you own. </p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagePermissionsResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_image_permissions_list" in value:
        import capo_appstream.types.shared_image_permissions_list

        out["SharedImagePermissionsList"] = (
            capo_appstream.types.shared_image_permissions_list.serialize_aws_json_1_1(
                value["shared_image_permissions_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagePermissionsResult:
    out: DescribeImagePermissionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SharedImagePermissionsList") is not None:
        import capo_appstream.types.shared_image_permissions_list

        out["shared_image_permissions_list"] = (
            capo_appstream.types.shared_image_permissions_list.deserialize_aws_json_1_1(
                data["SharedImagePermissionsList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeImagePermissionsResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_image_permissions_list" in value:
        import capo_appstream.types.shared_image_permissions_list

        out["SharedImagePermissionsList"] = (
            capo_appstream.types.shared_image_permissions_list.serialize_cbor(
                value["shared_image_permissions_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeImagePermissionsResult:
    out: DescribeImagePermissionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SharedImagePermissionsList") is not None:
        import capo_appstream.types.shared_image_permissions_list

        out["shared_image_permissions_list"] = (
            capo_appstream.types.shared_image_permissions_list.deserialize_cbor(
                data["SharedImagePermissionsList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
