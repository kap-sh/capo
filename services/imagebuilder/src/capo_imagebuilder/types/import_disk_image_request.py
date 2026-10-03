"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportDiskImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.infrastructure_configuration_arn
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.os_version
    import capo_imagebuilder.types.register_image_options
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.uri
    import capo_imagebuilder.types.version_number
    import capo_imagebuilder.types.windows_configuration


class ImportDiskImageRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the image resource that's created from the import. Image Builder generates the image ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If an image with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the import creates a new build version for it.</p>"""
    semantic_version: "capo_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version to attach to the image that's created during the import process. This version follows the semantic version syntax.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description for your disk image import.</p>"""
    platform: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The operating system platform for the imported image. Allowed values include the following: <code>Windows</code>.</p>"""
    os_version: "capo_imagebuilder.types.os_version.OsVersion"
    """<p>The operating system version for the imported image. The only supported value is <code>Microsoft Windows 11</code>.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions to import an image from a Microsoft ISO file. If you don't provide a role, Image Builder uses the Image Builder service-linked role in your account, and creates it if it doesn't exist.</p>"""
    infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration resource that's used for launching the EC2 instance on which the ISO image is built.</p>"""
    uri: "capo_imagebuilder.types.uri.Uri"
    """<p>The <code>uri</code> of the ISO disk file that's stored in Amazon S3, in <code>s3://bucket/key</code> format. The key must end with the <code>.iso</code>, <code>.ISO</code>, or <code>.Iso</code> extension, and the bucket must be owned by the account that makes the request.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The CloudWatch Logs log group where Image Builder sends the import logs. If you specify a log group name outside of the <code>/aws/imagebuilder/</code> namespace, you must also provide an <code>executionRole</code> that has permission to write to that log group.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to image resources created from the import.</p>"""
    register_image_options: NotRequired[
        "capo_imagebuilder.types.register_image_options.RegisterImageOptions"
    ]
    """<p>Configures Secure Boot and UEFI settings for the imported image.</p>"""
    windows_configuration: NotRequired[
        "capo_imagebuilder.types.windows_configuration.WindowsConfiguration"
    ]
    """<p>Specifies Windows settings for ISO imports.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDiskImageRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    out["platform"] = value["platform"]
    out["osVersion"] = value["os_version"]
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    out["uri"] = value["uri"]
    if "logging_configuration" in value:
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "register_image_options" in value:
        import capo_imagebuilder.types.register_image_options

        out["registerImageOptions"] = (
            capo_imagebuilder.types.register_image_options.serialize_json(
                value["register_image_options"]
            )
        )
    if "windows_configuration" in value:
        import capo_imagebuilder.types.windows_configuration

        out["windowsConfiguration"] = (
            capo_imagebuilder.types.windows_configuration.serialize_json(
                value["windows_configuration"]
            )
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportDiskImageRequest:
    out: ImportDiskImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportDiskImageRequest.name required")
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("ImportDiskImageRequest.semantic_version required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    else:
        raise DeserializationError("ImportDiskImageRequest.platform required")
    if data.get("osVersion") is not None:
        out["os_version"] = data["osVersion"]
    else:
        raise DeserializationError("ImportDiskImageRequest.os_version required")
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("infrastructureConfigurationArn") is not None:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "ImportDiskImageRequest.infrastructure_configuration_arn required"
        )
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("ImportDiskImageRequest.uri required")
    if data.get("loggingConfiguration") is not None:
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("registerImageOptions") is not None:
        import capo_imagebuilder.types.register_image_options

        out["register_image_options"] = (
            capo_imagebuilder.types.register_image_options.deserialize_json(
                data["registerImageOptions"]
            )
        )
    if data.get("windowsConfiguration") is not None:
        import capo_imagebuilder.types.windows_configuration

        out["windows_configuration"] = (
            capo_imagebuilder.types.windows_configuration.deserialize_json(
                data["windowsConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("ImportDiskImageRequest.client_token required")
    return out
