"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkFacet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name_list
    import capo_clouddirectory.types.typed_link_attribute_definition_list
    import capo_clouddirectory.types.typed_link_name


class TypedLinkFacet(TypedDict, closed=True):
    name: "capo_clouddirectory.types.typed_link_name.TypedLinkName"
    """<p>The unique name of the typed link facet.</p>"""
    attributes: "capo_clouddirectory.types.typed_link_attribute_definition_list.TypedLinkAttributeDefinitionList"
    """<p>A set of key-value pairs associated with the typed link. Typed link attributes are used when you have data values that are related to the link itself, and not to one of the two objects being linked. Identity attributes also serve to distinguish the link from others of the same type between the same objects.</p>"""
    identity_attribute_order: (
        "capo_clouddirectory.types.attribute_name_list.AttributeNameList"
    )
    """<p>The set of attributes that distinguish links made from this facet from each other, in the order of significance. Listing typed links can filter on the values of these attributes. See <a>ListOutgoingTypedLinks</a> and <a>ListIncomingTypedLinks</a> for details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkFacet) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_clouddirectory.types.typed_link_attribute_definition_list

    out["Attributes"] = (
        capo_clouddirectory.types.typed_link_attribute_definition_list.serialize_json(
            value["attributes"]
        )
    )
    import capo_clouddirectory.types.attribute_name_list

    out["IdentityAttributeOrder"] = (
        capo_clouddirectory.types.attribute_name_list.serialize_json(
            value["identity_attribute_order"]
        )
    )
    return out


def deserialize_json(data: dict) -> TypedLinkFacet:
    out: TypedLinkFacet = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Attributes") is not None:
        import capo_clouddirectory.types.typed_link_attribute_definition_list

        out["attributes"] = (
            capo_clouddirectory.types.typed_link_attribute_definition_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        out["attributes"] = []
    if data.get("IdentityAttributeOrder") is not None:
        import capo_clouddirectory.types.attribute_name_list

        out["identity_attribute_order"] = (
            capo_clouddirectory.types.attribute_name_list.deserialize_json(
                data["IdentityAttributeOrder"]
            )
        )
    else:
        out["identity_attribute_order"] = []
    return out
