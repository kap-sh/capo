"""Generated from Smithy shape ``com.amazonaws.organizations#CreateOrganizationalUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.organizational_unit_name
    import capo_organizations.types.parent_id
    import capo_organizations.types.tags


class CreateOrganizationalUnitRequest(TypedDict, closed=True):
    parent_id: "capo_organizations.types.parent_id.ParentId"
    """<p>ID for the parent root or OU that you want to create the new OU in.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a parent ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""
    name: "capo_organizations.types.organizational_unit_name.OrganizationalUnitName"
    """<p>The friendly name to assign to the new OU.</p>"""
    tags: NotRequired["capo_organizations.types.tags.Tags"]
    """<p>A list of tags that you want to attach to the newly created OU. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to <code>null</code>. For more information about tagging, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html">Tagging Organizations resources</a> in the Organizations User Guide.</p> <note> <p>If any one of the tags is not valid or if you exceed the allowed number of tags for an OU, then the entire request fails and the OU is not created.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOrganizationalUnitRequest) -> dict:
    out: dict = {}
    out["ParentId"] = value["parent_id"]
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_organizations.types.tags

        out["Tags"] = capo_organizations.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOrganizationalUnitRequest:
    out: CreateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    else:
        raise DeserializationError("CreateOrganizationalUnitRequest.parent_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateOrganizationalUnitRequest.name required")
    if data.get("Tags") is not None:
        import capo_organizations.types.tags

        out["tags"] = capo_organizations.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
