"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.facet_attribute_update_list
    import capo_clouddirectory.types.facet_name
    import capo_clouddirectory.types.object_type


class UpdateFacetRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>"""
    name: "capo_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet.</p>"""
    attribute_updates: NotRequired[
        "capo_clouddirectory.types.facet_attribute_update_list.FacetAttributeUpdateList"
    ]
    """<p>List of attributes that need to be updated in a given schema <a>Facet</a>. Each attribute is followed by <code>AttributeAction</code>, which specifies the type of update operation to perform. </p>"""
    object_type: NotRequired["capo_clouddirectory.types.object_type.ObjectType"]
    """<p>The object type that is associated with the facet. See <a>CreateFacetRequest$ObjectType</a> for more details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "attribute_updates" in value:
        import capo_clouddirectory.types.facet_attribute_update_list

        out["AttributeUpdates"] = (
            capo_clouddirectory.types.facet_attribute_update_list.serialize_json(
                value["attribute_updates"]
            )
        )
    if "object_type" in value:
        import capo_clouddirectory.types.object_type

        out["ObjectType"] = capo_clouddirectory.types.object_type.serialize_json(
            value["object_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFacetRequest:
    out: UpdateFacetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("AttributeUpdates") is not None:
        import capo_clouddirectory.types.facet_attribute_update_list

        out["attribute_updates"] = (
            capo_clouddirectory.types.facet_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    if data.get("ObjectType") is not None:
        import capo_clouddirectory.types.object_type

        out["object_type"] = capo_clouddirectory.types.object_type.deserialize_json(
            data["ObjectType"]
        )
    return out
