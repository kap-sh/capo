"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id
    import capo_connect.types.security_profile_description
    import capo_connect.types.security_profile_id
    import capo_connect.types.security_profile_name
    import capo_connect.types.tag_map


class SecurityProfileSearchSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.security_profile_id.SecurityProfileId"]
    """<p>The identifier of the security profile.</p>"""
    organization_resource_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The organization resource identifier.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the security profile.</p>"""
    security_profile_name: NotRequired[
        "capo_connect.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The name of the security profile.</p>"""
    description: NotRequired[
        "capo_connect.types.security_profile_description.SecurityProfileDescription"
    ]
    """<p>The description of the security profile.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileSearchSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "organization_resource_id" in value:
        out["OrganizationResourceId"] = value["organization_resource_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "security_profile_name" in value:
        out["SecurityProfileName"] = value["security_profile_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SecurityProfileSearchSummary:
    out: SecurityProfileSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("OrganizationResourceId") is not None:
        out["organization_resource_id"] = data["OrganizationResourceId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("SecurityProfileName") is not None:
        out["security_profile_name"] = data["SecurityProfileName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
