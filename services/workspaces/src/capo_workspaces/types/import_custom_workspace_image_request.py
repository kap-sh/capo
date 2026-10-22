"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportCustomWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.custom_image_protocol
    import capo_workspaces.types.image_compute_type
    import capo_workspaces.types.image_source_identifier
    import capo_workspaces.types.image_validation_mode
    import capo_workspaces.types.infrastructure_configuration_arn
    import capo_workspaces.types.os_version
    import capo_workspaces.types.platform
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.workspace_image_description
    import capo_workspaces.types.workspace_image_name


class ImportCustomWorkspaceImageRequest(TypedDict, closed=True):
    image_name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the WorkSpace image.</p>"""
    image_description: (
        "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    )
    """<p>The description of the WorkSpace image.</p>"""
    compute_type: "capo_workspaces.types.image_compute_type.ImageComputeType"
    """<p>The supported compute type for the WorkSpace image.</p>"""
    protocol: "capo_workspaces.types.custom_image_protocol.CustomImageProtocol"
    """<p>The supported protocol for the WorkSpace image. Windows 11 does not support PCOIP protocol.</p>"""
    image_source: "capo_workspaces.types.image_source_identifier.ImageSourceIdentifier"
    """<p>The options for image import source.</p>"""
    infrastructure_configuration_arn: "capo_workspaces.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The infrastructure configuration ARN that specifies how the WorkSpace image is built.</p>"""
    platform: "capo_workspaces.types.platform.Platform"
    """<p>The platform for the WorkSpace image source.</p>"""
    os_version: "capo_workspaces.types.os_version.OSVersion"
    """<p>The OS version for the WorkSpace image source.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The resource tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>"""
    image_validation_mode: NotRequired[
        "capo_workspaces.types.image_validation_mode.ImageValidationMode"
    ]
    """<p>The image validation mode for the WorkSpace image import.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCustomWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["ImageName"] = value["image_name"]
    out["ImageDescription"] = value["image_description"]
    import capo_workspaces.types.image_compute_type

    out["ComputeType"] = (
        capo_workspaces.types.image_compute_type.serialize_aws_json_1_1(
            value["compute_type"]
        )
    )
    import capo_workspaces.types.custom_image_protocol

    out["Protocol"] = (
        capo_workspaces.types.custom_image_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    )
    import capo_workspaces.types.image_source_identifier

    out["ImageSource"] = (
        capo_workspaces.types.image_source_identifier.serialize_aws_json_1_1(
            value["image_source"]
        )
    )
    out["InfrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    import capo_workspaces.types.platform

    out["Platform"] = capo_workspaces.types.platform.serialize_aws_json_1_1(
        value["platform"]
    )
    import capo_workspaces.types.os_version

    out["OsVersion"] = capo_workspaces.types.os_version.serialize_aws_json_1_1(
        value["os_version"]
    )
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "image_validation_mode" in value:
        import capo_workspaces.types.image_validation_mode

        out["ImageValidationMode"] = (
            capo_workspaces.types.image_validation_mode.serialize_aws_json_1_1(
                value["image_validation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCustomWorkspaceImageRequest:
    out: ImportCustomWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    else:
        out["image_name"] = ""
    if data.get("ImageDescription") is not None:
        out["image_description"] = data["ImageDescription"]
    else:
        out["image_description"] = ""
    if data.get("ComputeType") is not None:
        import capo_workspaces.types.image_compute_type

        out["compute_type"] = (
            capo_workspaces.types.image_compute_type.deserialize_aws_json_1_1(
                data["ComputeType"]
            )
        )
    else:
        import typing

        out["compute_type"] = typing.cast(
            "capo_workspaces.types.image_compute_type.ImageComputeType", ""
        )
    if data.get("Protocol") is not None:
        import capo_workspaces.types.custom_image_protocol

        out["protocol"] = (
            capo_workspaces.types.custom_image_protocol.deserialize_aws_json_1_1(
                data["Protocol"]
            )
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_workspaces.types.custom_image_protocol.CustomImageProtocol", ""
        )
    if data.get("ImageSource") is not None:
        import capo_workspaces.types.image_source_identifier

        out["image_source"] = (
            capo_workspaces.types.image_source_identifier.deserialize_aws_json_1_1(
                data["ImageSource"]
            )
        )
    else:
        import capo_workspaces.types._unknown

        out["image_source"] = capo_workspaces.types._unknown.UnknownUnionMember("")
    if data.get("InfrastructureConfigurationArn") is not None:
        out["infrastructure_configuration_arn"] = data["InfrastructureConfigurationArn"]
    else:
        out["infrastructure_configuration_arn"] = ""
    if data.get("Platform") is not None:
        import capo_workspaces.types.platform

        out["platform"] = capo_workspaces.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    else:
        import typing

        out["platform"] = typing.cast("capo_workspaces.types.platform.Platform", "")
    if data.get("OsVersion") is not None:
        import capo_workspaces.types.os_version

        out["os_version"] = capo_workspaces.types.os_version.deserialize_aws_json_1_1(
            data["OsVersion"]
        )
    else:
        import typing

        out["os_version"] = typing.cast(
            "capo_workspaces.types.os_version.OSVersion", ""
        )
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ImageValidationMode") is not None:
        import capo_workspaces.types.image_validation_mode

        out["image_validation_mode"] = (
            capo_workspaces.types.image_validation_mode.deserialize_aws_json_1_1(
                data["ImageValidationMode"]
            )
        )
    return out
