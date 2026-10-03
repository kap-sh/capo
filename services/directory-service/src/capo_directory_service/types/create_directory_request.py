"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.description
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.directory_short_name
    import capo_directory_service.types.directory_size
    import capo_directory_service.types.directory_vpc_settings
    import capo_directory_service.types.network_type
    import capo_directory_service.types.password
    import capo_directory_service.types.tags


class CreateDirectoryRequest(TypedDict, closed=True):
    name: "capo_directory_service.types.directory_name.DirectoryName"
    """<p>The fully qualified name for the directory, such as <code>corp.example.com</code>.</p>"""
    short_name: NotRequired[
        "capo_directory_service.types.directory_short_name.DirectoryShortName"
    ]
    """<p>The NetBIOS name of the directory, such as <code>CORP</code>.</p>"""
    password: "capo_directory_service.types.password.Password"
    r"""<p>The password for the directory administrator. The directory creation process creates a directory administrator account with the user name <code>Administrator</code> and this password.</p> <p>If you need to change the password for the administrator account, you can use the <a>ResetUserPassword</a> API call.</p> <p>The regex pattern for this string is made up of the following conditions:</p> <ul> <li> <p>Length (?=^.{8,64}$) – Must be between 8 and 64 characters</p> </li> </ul> <p>AND any 3 of the following password complexity rules required by Active Directory:</p> <ul> <li> <p>Numbers and upper case and lowercase (?=.*\d)(?=.*[A-Z])(?=.*[a-z])</p> </li> <li> <p>Numbers and special characters and lower case (?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])</p> </li> <li> <p>Special characters and upper case and lower case (?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])</p> </li> <li> <p>Numbers and upper case and special characters (?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s])</p> </li> </ul> <p>For additional information about how Active Directory passwords are enforced, see <a href="https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements">Password must meet complexity requirements</a> on the Microsoft website.</p>"""
    description: NotRequired["capo_directory_service.types.description.Description"]
    """<p>A description for the directory.</p>"""
    size: "capo_directory_service.types.directory_size.DirectorySize"
    """<p>The size of the directory.</p>"""
    vpc_settings: NotRequired[
        "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    ]
    """<p>A <a>DirectoryVpcSettings</a> object that contains additional information for the operation.</p>"""
    tags: NotRequired["capo_directory_service.types.tags.Tags"]
    """<p>The tags to be assigned to the Simple AD directory.</p>"""
    network_type: NotRequired["capo_directory_service.types.network_type.NetworkType"]
    """<p>The network type for your directory. Simple AD supports IPv4 and Dual-stack only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectoryRequest) -> dict:
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
    if "vpc_settings" in value:
        import capo_directory_service.types.directory_vpc_settings

        out["VpcSettings"] = (
            capo_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
                value["vpc_settings"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateDirectoryRequest:
    out: CreateDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDirectoryRequest.name required")
    if data.get("ShortName") is not None:
        out["short_name"] = data["ShortName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateDirectoryRequest.password required")
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
        raise DeserializationError("CreateDirectoryRequest.size required")
    if data.get("VpcSettings") is not None:
        import capo_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            capo_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
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
