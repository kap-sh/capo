"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateComputerRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.attributes
    import capo_directory_service.types.computer_name
    import capo_directory_service.types.computer_password
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.organizational_unit_dn


class CreateComputerRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory in which to create the computer account.</p>"""
    computer_name: "capo_directory_service.types.computer_name.ComputerName"
    """<p>The name of the computer account.</p>"""
    password: "capo_directory_service.types.computer_password.ComputerPassword"
    """<p>A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "capo_directory_service.types.organizational_unit_dn.OrganizationalUnitDN"
    ]
    """<p>The fully-qualified distinguished name of the organizational unit to place the computer account in.</p>"""
    computer_attributes: NotRequired[
        "capo_directory_service.types.attributes.Attributes"
    ]
    """<p>An array of <a>Attribute</a> objects that contain any LDAP attributes to apply to the computer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateComputerRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["ComputerName"] = value["computer_name"]
    out["Password"] = value["password"]
    if "organizational_unit_distinguished_name" in value:
        out["OrganizationalUnitDistinguishedName"] = value[
            "organizational_unit_distinguished_name"
        ]
    if "computer_attributes" in value:
        import capo_directory_service.types.attributes

        out["ComputerAttributes"] = (
            capo_directory_service.types.attributes.serialize_aws_json_1_1(
                value["computer_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateComputerRequest:
    out: CreateComputerRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateComputerRequest.directory_id required")
    if data.get("ComputerName") is not None:
        out["computer_name"] = data["ComputerName"]
    else:
        raise DeserializationError("CreateComputerRequest.computer_name required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateComputerRequest.password required")
    if data.get("OrganizationalUnitDistinguishedName") is not None:
        out["organizational_unit_distinguished_name"] = data[
            "OrganizationalUnitDistinguishedName"
        ]
    if data.get("ComputerAttributes") is not None:
        import capo_directory_service.types.attributes

        out["computer_attributes"] = (
            capo_directory_service.types.attributes.deserialize_aws_json_1_1(
                data["ComputerAttributes"]
            )
        )
    return out


def redact_sensitive(value: CreateComputerRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
