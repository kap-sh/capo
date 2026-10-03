"""Generated from Smithy shape ``com.amazonaws.organizations#OrganizationalUnit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.organizational_unit_arn
    import capo_organizations.types.organizational_unit_id
    import capo_organizations.types.organizational_unit_name
    import capo_organizations.types.path


class OrganizationalUnit(TypedDict, closed=True):
    id: NotRequired[
        "capo_organizations.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The unique identifier (ID) associated with this OU. The ID is unique to the organization only.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an organizational unit ID string requires "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p>"""
    arn: NotRequired[
        "capo_organizations.types.organizational_unit_arn.OrganizationalUnitArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this OU.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    name: NotRequired[
        "capo_organizations.types.organizational_unit_name.OrganizationalUnitName"
    ]
    """<p>The friendly name of this OU.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    path: NotRequired["capo_organizations.types.path.Path"]
    """<p>The path in the organization where this OU exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnit) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationalUnit:
    out: OrganizationalUnit = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    return out
