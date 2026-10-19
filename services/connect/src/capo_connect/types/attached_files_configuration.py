"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFilesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attachment_scope
    import capo_connect.types.extension_configuration
    import capo_connect.types.instance_id
    import capo_connect.types.maximum_size_limit_in_bytes
    import capo_connect.types.timestamp


class AttachedFilesConfiguration(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    attachment_scope: "capo_connect.types.attachment_scope.AttachmentScope"
    """<p>The scope of the attachment. Valid values are <code>EMAIL</code>, <code>CHAT</code>, <code>CASE</code>, and <code>TASK</code>.</p>"""
    maximum_size_limit_in_bytes: NotRequired[
        "capo_connect.types.maximum_size_limit_in_bytes.MaximumSizeLimitInBytes"
    ]
    """<p>The maximum size limit for attached files in bytes.</p>"""
    extension_configuration: NotRequired[
        "capo_connect.types.extension_configuration.ExtensionConfiguration"
    ]
    """<p>The configuration for allowed file extensions.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFilesConfiguration) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.attachment_scope

    out["AttachmentScope"] = capo_connect.types.attachment_scope.serialize_json(
        value["attachment_scope"]
    )
    if "maximum_size_limit_in_bytes" in value:
        out["MaximumSizeLimitInBytes"] = value["maximum_size_limit_in_bytes"]
    if "extension_configuration" in value:
        import capo_connect.types.extension_configuration

        out["ExtensionConfiguration"] = (
            capo_connect.types.extension_configuration.serialize_json(
                value["extension_configuration"]
            )
        )
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> AttachedFilesConfiguration:
    out: AttachedFilesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("AttachmentScope") is not None:
        import capo_connect.types.attachment_scope

        out["attachment_scope"] = capo_connect.types.attachment_scope.deserialize_json(
            data["AttachmentScope"]
        )
    else:
        import typing

        out["attachment_scope"] = typing.cast(
            "capo_connect.types.attachment_scope.AttachmentScope", ""
        )
    if data.get("MaximumSizeLimitInBytes") is not None:
        out["maximum_size_limit_in_bytes"] = data["MaximumSizeLimitInBytes"]
    if data.get("ExtensionConfiguration") is not None:
        import capo_connect.types.extension_configuration

        out["extension_configuration"] = (
            capo_connect.types.extension_configuration.deserialize_json(
                data["ExtensionConfiguration"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
