"""Generated from Smithy shape ``com.amazonaws.organizations#UpdateOrganizationalUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.organizational_unit_id
    import capo_organizations.types.organizational_unit_name


class UpdateOrganizationalUnitRequest(TypedDict, closed=True):
    organizational_unit_id: (
        "capo_organizations.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>ID for the OU that you want to rename. You can get the ID from the <a>ListOrganizationalUnitsForParent</a> operation.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an organizational unit ID string requires "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p>"""
    name: NotRequired[
        "capo_organizations.types.organizational_unit_name.OrganizationalUnitName"
    ]
    """<p>The new name that you want to assign to the OU.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOrganizationalUnitRequest) -> dict:
    out: dict = {}
    out["OrganizationalUnitId"] = value["organizational_unit_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOrganizationalUnitRequest:
    out: UpdateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationalUnitId") is not None:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    else:
        raise DeserializationError(
            "UpdateOrganizationalUnitRequest.organizational_unit_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
