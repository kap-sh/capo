"""Generated from Smithy shape ``com.amazonaws.connect#UpdateAttachedFilesConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attachment_scope
    import capo_connect.types.extension_configuration
    import capo_connect.types.instance_id
    import capo_connect.types.maximum_size_limit_in_bytes


class UpdateAttachedFilesConfigurationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    attachment_scope: "capo_connect.types.attachment_scope.AttachmentScope"
    """<p>The scope of the attachment. Valid values are <code>EMAIL</code>, <code>CHAT</code>, <code>CASE</code>, and <code>TASK</code>.</p>"""
    maximum_size_limit_in_bytes: NotRequired[
        "capo_connect.types.maximum_size_limit_in_bytes.MaximumSizeLimitInBytes"
    ]
    """<p>The maximum size limit for attached files in bytes. The minimum value is 1 and the maximum value is 104857600 (100 MB).</p>"""
    extension_configuration: NotRequired[
        "capo_connect.types.extension_configuration.ExtensionConfiguration"
    ]
    """<p>The configuration for allowed file extensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttachedFilesConfigurationRequest) -> dict:
    out: dict = {}
    if "maximum_size_limit_in_bytes" in value:
        out["MaximumSizeLimitInBytes"] = value["maximum_size_limit_in_bytes"]
    if "extension_configuration" in value:
        import capo_connect.types.extension_configuration

        out["ExtensionConfiguration"] = (
            capo_connect.types.extension_configuration.serialize_json(
                value["extension_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAttachedFilesConfigurationRequest:
    out: UpdateAttachedFilesConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaximumSizeLimitInBytes") is not None:
        out["maximum_size_limit_in_bytes"] = data["MaximumSizeLimitInBytes"]
    if data.get("ExtensionConfiguration") is not None:
        import capo_connect.types.extension_configuration

        out["extension_configuration"] = (
            capo_connect.types.extension_configuration.deserialize_json(
                data["ExtensionConfiguration"]
            )
        )
    return out
