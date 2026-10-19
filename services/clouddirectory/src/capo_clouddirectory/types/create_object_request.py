"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_key_and_value_list
    import capo_clouddirectory.types.link_name
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet_list


class CreateObjectRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> in which the object will be created. For more information, see <a>arns</a>.</p>"""
    schema_facets: "capo_clouddirectory.types.schema_facet_list.SchemaFacetList"
    """<p>A list of schema facets to be associated with the object. Do not provide minor version components. See <a>SchemaFacet</a> for details.</p>"""
    object_attribute_list: NotRequired[
        "capo_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>The attribute map whose attribute ARN contains the key and attribute value as the map value.</p>"""
    parent_reference: NotRequired[
        "capo_clouddirectory.types.object_reference.ObjectReference"
    ]
    """<p>If specified, the parent reference to which this object will be attached.</p>"""
    link_name: NotRequired["capo_clouddirectory.types.link_name.LinkName"]
    """<p>The name of link that is used to attach this object to a parent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateObjectRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.schema_facet_list

    out["SchemaFacets"] = capo_clouddirectory.types.schema_facet_list.serialize_json(
        value["schema_facets"]
    )
    if "object_attribute_list" in value:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["ObjectAttributeList"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["object_attribute_list"]
            )
        )
    if "parent_reference" in value:
        import capo_clouddirectory.types.object_reference

        out["ParentReference"] = (
            capo_clouddirectory.types.object_reference.serialize_json(
                value["parent_reference"]
            )
        )
    if "link_name" in value:
        out["LinkName"] = value["link_name"]
    return out


def deserialize_json(data: dict) -> CreateObjectRequest:
    out: CreateObjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("SchemaFacets") is not None:
        import capo_clouddirectory.types.schema_facet_list

        out["schema_facets"] = (
            capo_clouddirectory.types.schema_facet_list.deserialize_json(
                data["SchemaFacets"]
            )
        )
    else:
        out["schema_facets"] = []
    if data.get("ObjectAttributeList") is not None:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["object_attribute_list"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["ObjectAttributeList"]
            )
        )
    if data.get("ParentReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["parent_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    if data.get("LinkName") is not None:
        out["link_name"] = data["LinkName"]
    return out
