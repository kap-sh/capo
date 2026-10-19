"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_vpc_settings
    import capo_directory_service.types.region_name


class AddRegionRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory to which you want to add Region replication.</p>"""
    region_name: "capo_directory_service.types.region_name.RegionName"
    """<p>The name of the Region where you want to add domain controllers for replication. For example, <code>us-east-1</code>.</p>"""
    vpc_settings: (
        "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddRegionRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["RegionName"] = value["region_name"]
    import capo_directory_service.types.directory_vpc_settings

    out["VPCSettings"] = (
        capo_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
            value["vpc_settings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddRegionRequest:
    out: AddRegionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    if data.get("VPCSettings") is not None:
        import capo_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            capo_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VPCSettings"]
            )
        )
    else:
        raise DeserializationError("AddRegionRequest.vpc_settings required")
    return out
