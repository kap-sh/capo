"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeNodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.description
    import capo_panorama.types.node_asset_name
    import capo_panorama.types.node_category
    import capo_panorama.types.node_id
    import capo_panorama.types.node_interface
    import capo_panorama.types.node_name
    import capo_panorama.types.node_package_arn
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version
    import capo_panorama.types.package_owner_account
    import capo_panorama.types.time_stamp


class DescribeNodeResponse(TypedDict, closed=True):
    node_id: "capo_panorama.types.node_id.NodeId"
    """<p>The node's ID.</p>"""
    name: "capo_panorama.types.node_name.NodeName"
    """<p>The node's name.</p>"""
    category: "capo_panorama.types.node_category.NodeCategory"
    """<p>The node's category.</p>"""
    owner_account: "capo_panorama.types.package_owner_account.PackageOwnerAccount"
    """<p>The account ID of the node's owner.</p>"""
    package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The node's package name.</p>"""
    package_id: "capo_panorama.types.node_package_id.NodePackageId"
    """<p>The node's package ID.</p>"""
    package_arn: NotRequired["capo_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The node's ARN.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>The node's package version.</p>"""
    patch_version: (
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The node's patch version.</p>"""
    node_interface: "capo_panorama.types.node_interface.NodeInterface"
    """<p>The node's interface.</p>"""
    asset_name: NotRequired["capo_panorama.types.node_asset_name.NodeAssetName"]
    """<p>The node's asset name.</p>"""
    description: "capo_panorama.types.description.Description"
    """<p>The node's description.</p>"""
    created_time: "capo_panorama.types.time_stamp.TimeStamp"
    """<p>When the node was created.</p>"""
    last_updated_time: "capo_panorama.types.time_stamp.TimeStamp"
    """<p>When the node was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodeResponse) -> dict:
    out: dict = {}
    out["NodeId"] = value["node_id"]
    out["Name"] = value["name"]
    out["Category"] = value["category"]
    out["OwnerAccount"] = value["owner_account"]
    out["PackageName"] = value["package_name"]
    out["PackageId"] = value["package_id"]
    if "package_arn" in value:
        out["PackageArn"] = value["package_arn"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    import capo_panorama.types.node_interface

    out["NodeInterface"] = capo_panorama.types.node_interface.serialize_json(
        value["node_interface"]
    )
    if "asset_name" in value:
        out["AssetName"] = value["asset_name"]
    out["Description"] = value["description"]
    import capo_panorama.types.time_stamp

    out["CreatedTime"] = capo_panorama.types.time_stamp.serialize_json(
        value["created_time"]
    )
    import capo_panorama.types.time_stamp

    out["LastUpdatedTime"] = capo_panorama.types.time_stamp.serialize_json(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> DescribeNodeResponse:
    out: DescribeNodeResponse = {}  # type: ignore[typeddict-item]
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    else:
        out["node_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        out["category"] = ""
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    else:
        out["owner_account"] = ""
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    else:
        out["package_name"] = ""
    if data.get("PackageId") is not None:
        out["package_id"] = data["PackageId"]
    else:
        out["package_id"] = ""
    if data.get("PackageArn") is not None:
        out["package_arn"] = data["PackageArn"]
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    else:
        out["package_version"] = ""
    if data.get("PatchVersion") is not None:
        out["patch_version"] = data["PatchVersion"]
    else:
        out["patch_version"] = ""
    if data.get("NodeInterface") is not None:
        import capo_panorama.types.node_interface

        out["node_interface"] = capo_panorama.types.node_interface.deserialize_json(
            data["NodeInterface"]
        )
    else:
        raise DeserializationError("DescribeNodeResponse.node_interface required")
    if data.get("AssetName") is not None:
        out["asset_name"] = data["AssetName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("CreatedTime") is not None:
        import capo_panorama.types.time_stamp

        out["created_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_panorama.types.time_stamp

        out["last_updated_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
