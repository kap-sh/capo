"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateMicrosoftADRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.description
    import capo_directory_service.types.directory_edition
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.directory_short_name
    import capo_directory_service.types.directory_vpc_settings
    import capo_directory_service.types.network_type
    import capo_directory_service.types.password
    import capo_directory_service.types.tags


class CreateMicrosoftADRequest(TypedDict, closed=True):
    name: "capo_directory_service.types.directory_name.DirectoryName"
    """<p>The fully qualified domain name for the Managed Microsoft AD directory, such as <code>corp.example.com</code>. This name will resolve inside your VPC only. It does not need to be publicly resolvable.</p>"""
    short_name: NotRequired[
        "capo_directory_service.types.directory_short_name.DirectoryShortName"
    ]
    """<p>The NetBIOS name for your domain, such as <code>CORP</code>. If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, <code>CORP</code> for the directory DNS <code>corp.example.com</code>. </p>"""
    password: "capo_directory_service.types.password.Password"
    """<p>The password for the default administrative user named <code>Admin</code>.</p> <p>If you need to change the password for the administrator account, you can use the <a>ResetUserPassword</a> API call.</p>"""
    description: NotRequired["capo_directory_service.types.description.Description"]
    """<p>A description for the directory. This label will appear on the Amazon Web Services console <code>Directory Details</code> page after the directory is created.</p>"""
    vpc_settings: (
        "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    )
    """<p>Contains VPC information for the <a>CreateDirectory</a> or <a>CreateMicrosoftAD</a> operation.</p>"""
    edition: NotRequired[
        "capo_directory_service.types.directory_edition.DirectoryEdition"
    ]
    """<p>Managed Microsoft AD is available in two editions: <code>Standard</code> and <code>Enterprise</code>. <code>Enterprise</code> is the default.</p>"""
    tags: NotRequired["capo_directory_service.types.tags.Tags"]
    """<p>The tags to be assigned to the Managed Microsoft AD directory.</p>"""
    network_type: NotRequired["capo_directory_service.types.network_type.NetworkType"]
    """<p> The network type for your domain. The default value is <code>IPv4</code> or <code>IPv6</code> based on the provided subnet capabilities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMicrosoftADRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    out["Password"] = value["password"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_directory_service.types.directory_vpc_settings

    out["VpcSettings"] = (
        capo_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
            value["vpc_settings"]
        )
    )
    if "edition" in value:
        import capo_directory_service.types.directory_edition

        out["Edition"] = (
            capo_directory_service.types.directory_edition.serialize_aws_json_1_1(
                value["edition"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateMicrosoftADRequest:
    out: CreateMicrosoftADRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateMicrosoftADRequest.name required")
    if data.get("ShortName") is not None:
        out["short_name"] = data["ShortName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateMicrosoftADRequest.password required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcSettings") is not None:
        import capo_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            capo_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    else:
        raise DeserializationError("CreateMicrosoftADRequest.vpc_settings required")
    if data.get("Edition") is not None:
        import capo_directory_service.types.directory_edition

        out["edition"] = (
            capo_directory_service.types.directory_edition.deserialize_aws_json_1_1(
                data["Edition"]
            )
        )
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


def redact_sensitive(value: CreateMicrosoftADRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
