"""Generated from Smithy shape ``com.amazonaws.appstream#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.name
    import capo_appstream.types.platforms
    import capo_appstream.types.s3_location
    import capo_appstream.types.string
    import capo_appstream.types.string_list
    import capo_appstream.types.tags


class CreateApplicationRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the application. This name is visible to users when display name is not specified.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The display name of the application. This name is visible to users in the application catalog.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description of the application.</p>"""
    icon_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The location in S3 of the application icon.</p>"""
    launch_path: NotRequired["capo_appstream.types.string.String"]
    """<p>The launch path of the application.</p>"""
    working_directory: NotRequired["capo_appstream.types.string.String"]
    """<p>The working directory of the application.</p>"""
    launch_parameters: NotRequired["capo_appstream.types.string.String"]
    """<p>The launch parameters of the application.</p>"""
    platforms: NotRequired["capo_appstream.types.platforms.Platforms"]
    """<p>The platforms the application supports. WINDOWS_SERVER_2019, AMAZON_LINUX2 and UBUNTU_PRO_2404 are supported for Elastic fleets.</p>"""
    instance_families: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The instance families the application supports. Valid values are GENERAL_PURPOSE and GRAPHICS_G4.</p>"""
    app_block_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The app block ARN to which the application should be associated</p>"""
    tags: NotRequired["capo_appstream.types.tags.Tags"]
    """<p>The tags assigned to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_s3_location" in value:
        import capo_appstream.types.s3_location

        out["IconS3Location"] = capo_appstream.types.s3_location.serialize_aws_json_1_1(
            value["icon_s3_location"]
        )
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    if "platforms" in value:
        import capo_appstream.types.platforms

        out["Platforms"] = capo_appstream.types.platforms.serialize_aws_json_1_1(
            value["platforms"]
        )
    if "instance_families" in value:
        import capo_appstream.types.string_list

        out["InstanceFamilies"] = (
            capo_appstream.types.string_list.serialize_aws_json_1_1(
                value["instance_families"]
            )
        )
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "tags" in value:
        import capo_appstream.types.tags

        out["Tags"] = capo_appstream.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IconS3Location") is not None:
        import capo_appstream.types.s3_location

        out["icon_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["IconS3Location"]
            )
        )
    if data.get("LaunchPath") is not None:
        out["launch_path"] = data["LaunchPath"]
    if data.get("WorkingDirectory") is not None:
        out["working_directory"] = data["WorkingDirectory"]
    if data.get("LaunchParameters") is not None:
        out["launch_parameters"] = data["LaunchParameters"]
    if data.get("Platforms") is not None:
        import capo_appstream.types.platforms

        out["platforms"] = capo_appstream.types.platforms.deserialize_aws_json_1_1(
            data["Platforms"]
        )
    if data.get("InstanceFamilies") is not None:
        import capo_appstream.types.string_list

        out["instance_families"] = (
            capo_appstream.types.string_list.deserialize_aws_json_1_1(
                data["InstanceFamilies"]
            )
        )
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("Tags") is not None:
        import capo_appstream.types.tags

        out["tags"] = capo_appstream.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_s3_location" in value:
        import capo_appstream.types.s3_location

        out["IconS3Location"] = capo_appstream.types.s3_location.serialize_cbor(
            value["icon_s3_location"]
        )
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    if "platforms" in value:
        import capo_appstream.types.platforms

        out["Platforms"] = capo_appstream.types.platforms.serialize_cbor(
            value["platforms"]
        )
    if "instance_families" in value:
        import capo_appstream.types.string_list

        out["InstanceFamilies"] = capo_appstream.types.string_list.serialize_cbor(
            value["instance_families"]
        )
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "tags" in value:
        import capo_appstream.types.tags

        out["Tags"] = capo_appstream.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IconS3Location") is not None:
        import capo_appstream.types.s3_location

        out["icon_s3_location"] = capo_appstream.types.s3_location.deserialize_cbor(
            data["IconS3Location"]
        )
    if data.get("LaunchPath") is not None:
        out["launch_path"] = data["LaunchPath"]
    if data.get("WorkingDirectory") is not None:
        out["working_directory"] = data["WorkingDirectory"]
    if data.get("LaunchParameters") is not None:
        out["launch_parameters"] = data["LaunchParameters"]
    if data.get("Platforms") is not None:
        import capo_appstream.types.platforms

        out["platforms"] = capo_appstream.types.platforms.deserialize_cbor(
            data["Platforms"]
        )
    if data.get("InstanceFamilies") is not None:
        import capo_appstream.types.string_list

        out["instance_families"] = capo_appstream.types.string_list.deserialize_cbor(
            data["InstanceFamilies"]
        )
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("Tags") is not None:
        import capo_appstream.types.tags

        out["tags"] = capo_appstream.types.tags.deserialize_cbor(data["Tags"])
    return out
