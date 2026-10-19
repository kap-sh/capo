"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.boolean
    import capo_panorama.types.node_package_arn
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version
    import capo_panorama.types.package_owner_account
    import capo_panorama.types.package_version_status
    import capo_panorama.types.package_version_status_description
    import capo_panorama.types.time_stamp


class DescribePackageVersionResponse(TypedDict, closed=True):
    owner_account: NotRequired[
        "capo_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>The account ID of the version's owner.</p>"""
    package_id: "capo_panorama.types.node_package_id.NodePackageId"
    """<p>The version's ID.</p>"""
    package_arn: NotRequired["capo_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The ARN of the package.</p>"""
    package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The version's name.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>The version's version.</p>"""
    patch_version: (
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The version's patch version.</p>"""
    is_latest_patch: "capo_panorama.types.boolean.Boolean"
    """<p>Whether the version is the latest available.</p>"""
    status: "capo_panorama.types.package_version_status.PackageVersionStatus"
    """<p>The version's status.</p>"""
    status_description: NotRequired[
        "capo_panorama.types.package_version_status_description.PackageVersionStatusDescription"
    ]
    """<p>The version's status description.</p>"""
    registered_time: NotRequired["capo_panorama.types.time_stamp.TimeStamp"]
    """<p>The version's registered time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageVersionResponse) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    out["PackageId"] = value["package_id"]
    if "package_arn" in value:
        out["PackageArn"] = value["package_arn"]
    out["PackageName"] = value["package_name"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    out["IsLatestPatch"] = value.get("is_latest_patch", False)
    out["Status"] = value["status"]
    if "status_description" in value:
        out["StatusDescription"] = value["status_description"]
    if "registered_time" in value:
        import capo_panorama.types.time_stamp

        out["RegisteredTime"] = capo_panorama.types.time_stamp.serialize_json(
            value["registered_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribePackageVersionResponse:
    out: DescribePackageVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    if data.get("PackageId") is not None:
        out["package_id"] = data["PackageId"]
    else:
        out["package_id"] = ""
    if data.get("PackageArn") is not None:
        out["package_arn"] = data["PackageArn"]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    else:
        out["package_name"] = ""
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    else:
        out["package_version"] = ""
    if data.get("PatchVersion") is not None:
        out["patch_version"] = data["PatchVersion"]
    else:
        out["patch_version"] = ""
    if data.get("IsLatestPatch") is not None:
        out["is_latest_patch"] = data["IsLatestPatch"]
    else:
        out["is_latest_patch"] = False
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("StatusDescription") is not None:
        out["status_description"] = data["StatusDescription"]
    if data.get("RegisteredTime") is not None:
        import capo_panorama.types.time_stamp

        out["registered_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["RegisteredTime"]
        )
    return out
