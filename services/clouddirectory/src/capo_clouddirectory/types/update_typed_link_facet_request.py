"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateTypedLinkFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_name_list
    import capo_clouddirectory.types.typed_link_facet_attribute_update_list
    import capo_clouddirectory.types.typed_link_name


class UpdateTypedLinkFacetRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    name: "capo_clouddirectory.types.typed_link_name.TypedLinkName"
    """<p>The unique name of the typed link facet.</p>"""
    attribute_updates: "capo_clouddirectory.types.typed_link_facet_attribute_update_list.TypedLinkFacetAttributeUpdateList"
    """<p>Attributes update structure.</p>"""
    identity_attribute_order: (
        "capo_clouddirectory.types.attribute_name_list.AttributeNameList"
    )
    """<p>The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to a typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTypedLinkFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_clouddirectory.types.typed_link_facet_attribute_update_list

    out["AttributeUpdates"] = (
        capo_clouddirectory.types.typed_link_facet_attribute_update_list.serialize_json(
            value["attribute_updates"]
        )
    )
    import capo_clouddirectory.types.attribute_name_list

    out["IdentityAttributeOrder"] = (
        capo_clouddirectory.types.attribute_name_list.serialize_json(
            value["identity_attribute_order"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTypedLinkFacetRequest:
    out: UpdateTypedLinkFacetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateTypedLinkFacetRequest.name required")
    if data.get("AttributeUpdates") is not None:
        import capo_clouddirectory.types.typed_link_facet_attribute_update_list

        out["attribute_updates"] = (
            capo_clouddirectory.types.typed_link_facet_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTypedLinkFacetRequest.attribute_updates required"
        )
    if data.get("IdentityAttributeOrder") is not None:
        import capo_clouddirectory.types.attribute_name_list

        out["identity_attribute_order"] = (
            capo_clouddirectory.types.attribute_name_list.deserialize_json(
                data["IdentityAttributeOrder"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTypedLinkFacetRequest.identity_attribute_order required"
        )
    return out
