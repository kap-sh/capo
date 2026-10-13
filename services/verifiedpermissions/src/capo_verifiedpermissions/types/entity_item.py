"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_attributes
    import capo_verifiedpermissions.types.entity_cedar_tags
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.parent_list


class EntityItem(TypedDict, closed=True):
    identifier: "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the entity.</p>"""
    attributes: NotRequired[
        "capo_verifiedpermissions.types.entity_attributes.EntityAttributes"
    ]
    """<p>A list of attributes for the entity.</p>"""
    parents: NotRequired["capo_verifiedpermissions.types.parent_list.ParentList"]
    """<p>The parent entities in the hierarchy that contains the entity. A principal or resource entity can be defined with at most 99 <i>transitive parents</i> per authorization request. </p> <p>A transitive parent is an entity in the hierarchy of entities including all direct parents, and parents of parents. For example, a user can be a member of 91 groups if one of those groups is a member of eight groups, for a total of 100: one entity, 91 entity parents, and eight parents of parents. </p>"""
    tags: NotRequired[
        "capo_verifiedpermissions.types.entity_cedar_tags.EntityCedarTags"
    ]
    """<p>A list of cedar tags for the entity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityItem) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.entity_identifier

    out["identifier"] = (
        capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
            value["identifier"]
        )
    )
    if "attributes" in value:
        import capo_verifiedpermissions.types.entity_attributes

        out["attributes"] = (
            capo_verifiedpermissions.types.entity_attributes.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "parents" in value:
        import capo_verifiedpermissions.types.parent_list

        out["parents"] = (
            capo_verifiedpermissions.types.parent_list.serialize_aws_json_1_0(
                value["parents"]
            )
        )
    if "tags" in value:
        import capo_verifiedpermissions.types.entity_cedar_tags

        out["tags"] = (
            capo_verifiedpermissions.types.entity_cedar_tags.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EntityItem:
    out: EntityItem = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["identifier"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["identifier"]
            )
        )
    else:
        raise DeserializationError("EntityItem.identifier required")
    if data.get("attributes") is not None:
        import capo_verifiedpermissions.types.entity_attributes

        out["attributes"] = (
            capo_verifiedpermissions.types.entity_attributes.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    if data.get("parents") is not None:
        import capo_verifiedpermissions.types.parent_list

        out["parents"] = (
            capo_verifiedpermissions.types.parent_list.deserialize_aws_json_1_0(
                data["parents"]
            )
        )
    if data.get("tags") is not None:
        import capo_verifiedpermissions.types.entity_cedar_tags

        out["tags"] = (
            capo_verifiedpermissions.types.entity_cedar_tags.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out


def redact_sensitive(value: EntityItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["identifier"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["identifier"]
            )
        )
    if "attributes" in value:
        import capo_verifiedpermissions.types.entity_attributes

        out["attributes"] = (
            capo_verifiedpermissions.types.entity_attributes.redact_sensitive(
                value["attributes"]
            )
        )
    if "parents" in value:
        import capo_verifiedpermissions.types.parent_list

        out["parents"] = capo_verifiedpermissions.types.parent_list.redact_sensitive(
            value["parents"]
        )
    if "tags" in value:
        import capo_verifiedpermissions.types.entity_cedar_tags

        out["tags"] = capo_verifiedpermissions.types.entity_cedar_tags.redact_sensitive(
            value["tags"]
        )
    return out
