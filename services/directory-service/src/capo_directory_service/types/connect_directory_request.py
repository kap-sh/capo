"""Generated from Smithy shape ``com.amazonaws.directoryservice#ConnectDirectoryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.connect_password
    import capo_directory_service.types.description
    import capo_directory_service.types.directory_connect_settings
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.directory_short_name
    import capo_directory_service.types.directory_size
    import capo_directory_service.types.network_type
    import capo_directory_service.types.tags


class ConnectDirectoryRequest(TypedDict, closed=True):
    name: "capo_directory_service.types.directory_name.DirectoryName"
    """<p>The fully qualified name of your self-managed directory, such as <code>corp.example.com</code>.</p>"""
    short_name: NotRequired[
        "capo_directory_service.types.directory_short_name.DirectoryShortName"
    ]
    """<p>The NetBIOS name of your self-managed directory, such as <code>CORP</code>.</p>"""
    password: "capo_directory_service.types.connect_password.ConnectPassword"
    """<p>The password for your self-managed user account.</p>"""
    description: NotRequired["capo_directory_service.types.description.Description"]
    """<p>A description for the directory.</p>"""
    size: "capo_directory_service.types.directory_size.DirectorySize"
    """<p>The size of the directory.</p>"""
    connect_settings: "capo_directory_service.types.directory_connect_settings.DirectoryConnectSettings"
    """<p>A <a>DirectoryConnectSettings</a> object that contains additional information for the operation.</p>"""
    tags: NotRequired["capo_directory_service.types.tags.Tags"]
    """<p>The tags to be assigned to AD Connector.</p>"""
    network_type: NotRequired["capo_directory_service.types.network_type.NetworkType"]
    """<p>The network type for your directory. The default value is <code>IPv4</code> or <code>IPv6</code> based on the provided subnet capabilities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectDirectoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    out["Password"] = value["password"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_directory_service.types.directory_size

    out["Size"] = capo_directory_service.types.directory_size.serialize_aws_json_1_1(
        value["size"]
    )
    import capo_directory_service.types.directory_connect_settings

    out["ConnectSettings"] = (
        capo_directory_service.types.directory_connect_settings.serialize_aws_json_1_1(
            value["connect_settings"]
        )
    )
    if "tags" in value:
        import capo_directory_service.types.tags

        out["Tags"] = capo_directory_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "network_type" in value:
        import capo_directory_service.types.network_type

        out["NetworkType"] = (
            capo_directory_service.types.network_type.serialize_aws_json_1_1(
                value["network_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectDirectoryRequest:
    out: ConnectDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ShortName") is not None:
        out["short_name"] = data["ShortName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Size") is not None:
        import capo_directory_service.types.directory_size

        out["size"] = (
            capo_directory_service.types.directory_size.deserialize_aws_json_1_1(
                data["Size"]
            )
        )
    else:
        import typing

        out["size"] = typing.cast(
            "capo_directory_service.types.directory_size.DirectorySize", ""
        )
    if data.get("ConnectSettings") is not None:
        import capo_directory_service.types.directory_connect_settings

        out["connect_settings"] = (
            capo_directory_service.types.directory_connect_settings.deserialize_aws_json_1_1(
                data["ConnectSettings"]
            )
        )
    else:
        raise DeserializationError("ConnectDirectoryRequest.connect_settings required")
    if data.get("Tags") is not None:
        import capo_directory_service.types.tags

        out["tags"] = capo_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("NetworkType") is not None:
        import capo_directory_service.types.network_type

        out["network_type"] = (
            capo_directory_service.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    return out


def redact_sensitive(value: ConnectDirectoryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
