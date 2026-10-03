"""Generated from Smithy shape ``com.amazonaws.organizations#DeleteOrganizationalUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.organizational_unit_id


class DeleteOrganizationalUnitRequest(TypedDict, closed=True):
    organizational_unit_id: (
        "capo_organizations.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>ID for the organizational unit that you want to delete. You can get the ID from the <a>ListOrganizationalUnitsForParent</a> operation.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an organizational unit ID string requires "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationalUnitRequest) -> dict:
    out: dict = {}
    out["OrganizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationalUnitRequest:
    out: DeleteOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationalUnitId") is not None:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    else:
        raise DeserializationError(
            "DeleteOrganizationalUnitRequest.organizational_unit_id required"
        )
    return out
