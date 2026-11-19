"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.application_attributes
    import capo_appstream.types.arn
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.name
    import capo_appstream.types.s3_location
    import capo_appstream.types.string


class UpdateApplicationRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the application. This name is visible to users when display name is not specified.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The display name of the application. This name is visible to users in the application catalog.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description of the application.</p>"""
    icon_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The icon S3 location of the application.</p>"""
    launch_path: NotRequired["capo_appstream.types.string.String"]
    """<p>The launch path of the application.</p>"""
    working_directory: NotRequired["capo_appstream.types.string.String"]
    """<p>The working directory of the application.</p>"""
    launch_parameters: NotRequired["capo_appstream.types.string.String"]
    """<p>The launch parameters of the application.</p>"""
    app_block_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the app block.</p>"""
    attributes_to_delete: NotRequired[
        "capo_appstream.types.application_attributes.ApplicationAttributes"
    ]
    """<p>The attributes to delete for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
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
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "attributes_to_delete" in value:
        import capo_appstream.types.application_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.application_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.application_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.application_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateApplicationRequest) -> dict:
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
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "attributes_to_delete" in value:
        import capo_appstream.types.application_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.application_attributes.serialize_cbor(
                value["attributes_to_delete"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.application_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.application_attributes.deserialize_cbor(
                data["AttributesToDelete"]
            )
        )
    return out
