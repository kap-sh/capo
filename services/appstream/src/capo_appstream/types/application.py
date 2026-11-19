"""Generated from Smithy shape ``com.amazonaws.appstream#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.boolean
    import capo_appstream.types.metadata
    import capo_appstream.types.platforms
    import capo_appstream.types.s3_location
    import capo_appstream.types.string
    import capo_appstream.types.string_list
    import capo_appstream.types.timestamp


class Application(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the application.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The application name to display.</p>"""
    icon_url: NotRequired["capo_appstream.types.string.String"]
    """<p>The URL for the application icon. This URL might be time-limited.</p>"""
    launch_path: NotRequired["capo_appstream.types.string.String"]
    """<p>The path to the application executable in the instance.</p>"""
    launch_parameters: NotRequired["capo_appstream.types.string.String"]
    """<p>The arguments that are passed to the application at launch.</p>"""
    enabled: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>If there is a problem, the application can be disabled after image creation.</p>"""
    metadata: NotRequired["capo_appstream.types.metadata.Metadata"]
    """<p>Additional attributes that describe the application.</p>"""
    working_directory: NotRequired["capo_appstream.types.string.String"]
    """<p>The working directory for the application.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description of the application.</p>"""
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the application.</p>"""
    app_block_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The app block ARN of the application.</p>"""
    icon_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The S3 location of the application icon.</p>"""
    platforms: NotRequired["capo_appstream.types.platforms.Platforms"]
    """<p>The platforms on which the application can run.</p>"""
    instance_families: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The instance families for the application.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time at which the application was created within the app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Application) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "icon_url" in value:
        out["IconURL"] = value["icon_url"]
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "metadata" in value:
        import capo_appstream.types.metadata

        out["Metadata"] = capo_appstream.types.metadata.serialize_aws_json_1_1(
            value["metadata"]
        )
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "icon_s3_location" in value:
        import capo_appstream.types.s3_location

        out["IconS3Location"] = capo_appstream.types.s3_location.serialize_aws_json_1_1(
            value["icon_s3_location"]
        )
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
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("IconURL") is not None:
        out["icon_url"] = data["IconURL"]
    if data.get("LaunchPath") is not None:
        out["launch_path"] = data["LaunchPath"]
    if data.get("LaunchParameters") is not None:
        out["launch_parameters"] = data["LaunchParameters"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Metadata") is not None:
        import capo_appstream.types.metadata

        out["metadata"] = capo_appstream.types.metadata.deserialize_aws_json_1_1(
            data["Metadata"]
        )
    if data.get("WorkingDirectory") is not None:
        out["working_directory"] = data["WorkingDirectory"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("IconS3Location") is not None:
        import capo_appstream.types.s3_location

        out["icon_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["IconS3Location"]
            )
        )
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
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Application) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "icon_url" in value:
        out["IconURL"] = value["icon_url"]
    if "launch_path" in value:
        out["LaunchPath"] = value["launch_path"]
    if "launch_parameters" in value:
        out["LaunchParameters"] = value["launch_parameters"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "metadata" in value:
        import capo_appstream.types.metadata

        out["Metadata"] = capo_appstream.types.metadata.serialize_cbor(
            value["metadata"]
        )
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "icon_s3_location" in value:
        import capo_appstream.types.s3_location

        out["IconS3Location"] = capo_appstream.types.s3_location.serialize_cbor(
            value["icon_s3_location"]
        )
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
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_cbor(
            value["created_time"]
        )
    return out


def deserialize_cbor(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("IconURL") is not None:
        out["icon_url"] = data["IconURL"]
    if data.get("LaunchPath") is not None:
        out["launch_path"] = data["LaunchPath"]
    if data.get("LaunchParameters") is not None:
        out["launch_parameters"] = data["LaunchParameters"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Metadata") is not None:
        import capo_appstream.types.metadata

        out["metadata"] = capo_appstream.types.metadata.deserialize_cbor(
            data["Metadata"]
        )
    if data.get("WorkingDirectory") is not None:
        out["working_directory"] = data["WorkingDirectory"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("IconS3Location") is not None:
        import capo_appstream.types.s3_location

        out["icon_s3_location"] = capo_appstream.types.s3_location.deserialize_cbor(
            data["IconS3Location"]
        )
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
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["CreatedTime"]
        )
    return out
