"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_identifier
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.role_arn
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.tag_map


class CreateConfiguredTableAssociationInput(TypedDict, closed=True):
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the configured table association. This name is used to query the underlying configured table.</p>"""
    description: NotRequired["capo_cleanrooms.types.table_description.TableDescription"]
    """<p>A description for the configured table association.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The configured table is associated to the collaboration that this membership belongs to. Currently accepts a membership ID.</p>"""
    configured_table_identifier: (
        "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.</p>"""
    role_arn: "capo_cleanrooms.types.role_arn.RoleArn"
    """<p>The service will assume this role to access catalog metadata and query the table.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableAssociationInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["configuredTableIdentifier"] = value["configured_table_identifier"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableAssociationInput:
    out: CreateConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuredTableIdentifier") is not None:
        out["configured_table_identifier"] = data["configuredTableIdentifier"]
    else:
        out["configured_table_identifier"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    return out
