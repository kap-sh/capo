"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.node_package_arn
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_name
    import capo_panorama.types.principal_arns_list
    import capo_panorama.types.storage_location
    import capo_panorama.types.tag_map
    import capo_panorama.types.time_stamp


class DescribePackageResponse(TypedDict, closed=True):
    package_id: "capo_panorama.types.node_package_id.NodePackageId"
    """<p>The package's ID.</p>"""
    package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The package's name.</p>"""
    arn: "capo_panorama.types.node_package_arn.NodePackageArn"
    """<p>The package's ARN.</p>"""
    storage_location: "capo_panorama.types.storage_location.StorageLocation"
    """<p>The package's storage location.</p>"""
    read_access_principal_arns: NotRequired[
        "capo_panorama.types.principal_arns_list.PrincipalArnsList"
    ]
    """<p>ARNs of accounts that have read access to the package.</p>"""
    write_access_principal_arns: NotRequired[
        "capo_panorama.types.principal_arns_list.PrincipalArnsList"
    ]
    """<p>ARNs of accounts that have write access to the package.</p>"""
    created_time: "capo_panorama.types.time_stamp.TimeStamp"
    """<p>When the package was created.</p>"""
    tags: "capo_panorama.types.tag_map.TagMap"
    """<p>The package's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageResponse) -> dict:
    out: dict = {}
    out["PackageId"] = value["package_id"]
    out["PackageName"] = value["package_name"]
    out["Arn"] = value["arn"]
    import capo_panorama.types.storage_location

    out["StorageLocation"] = capo_panorama.types.storage_location.serialize_json(
        value["storage_location"]
    )
    if "read_access_principal_arns" in value:
        import capo_panorama.types.principal_arns_list

        out["ReadAccessPrincipalArns"] = (
            capo_panorama.types.principal_arns_list.serialize_json(
                value["read_access_principal_arns"]
            )
        )
    if "write_access_principal_arns" in value:
        import capo_panorama.types.principal_arns_list

        out["WriteAccessPrincipalArns"] = (
            capo_panorama.types.principal_arns_list.serialize_json(
                value["write_access_principal_arns"]
            )
        )
    import capo_panorama.types.time_stamp

    out["CreatedTime"] = capo_panorama.types.time_stamp.serialize_json(
        value["created_time"]
    )
    import capo_panorama.types.tag_map

    out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePackageResponse:
    out: DescribePackageResponse = {}  # type: ignore[typeddict-item]
    if data.get("PackageId") is not None:
        out["package_id"] = data["PackageId"]
    else:
        out["package_id"] = ""
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    else:
        out["package_name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("StorageLocation") is not None:
        import capo_panorama.types.storage_location

        out["storage_location"] = capo_panorama.types.storage_location.deserialize_json(
            data["StorageLocation"]
        )
    else:
        raise DeserializationError("DescribePackageResponse.storage_location required")
    if data.get("ReadAccessPrincipalArns") is not None:
        import capo_panorama.types.principal_arns_list

        out["read_access_principal_arns"] = (
            capo_panorama.types.principal_arns_list.deserialize_json(
                data["ReadAccessPrincipalArns"]
            )
        )
    if data.get("WriteAccessPrincipalArns") is not None:
        import capo_panorama.types.principal_arns_list

        out["write_access_principal_arns"] = (
            capo_panorama.types.principal_arns_list.deserialize_json(
                data["WriteAccessPrincipalArns"]
            )
        )
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
    if data.get("Tags") is not None:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
