"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAddFacetToObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_key_and_value_list
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet


class BatchAddFacetToObject(TypedDict, closed=True):
    schema_facet: "capo_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>Represents the facet being added to the object.</p>"""
    object_attribute_list: "capo_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    """<p>The attributes to set on the object.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object being mutated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAddFacetToObject) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.schema_facet

    out["SchemaFacet"] = capo_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
    import capo_clouddirectory.types.attribute_key_and_value_list

    out["ObjectAttributeList"] = (
        capo_clouddirectory.types.attribute_key_and_value_list.serialize_json(
            value["object_attribute_list"]
        )
    )
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    return out


def deserialize_json(data: dict) -> BatchAddFacetToObject:
    out: BatchAddFacetToObject = {}  # type: ignore[typeddict-item]
    if data.get("SchemaFacet") is not None:
        import capo_clouddirectory.types.schema_facet

        out["schema_facet"] = capo_clouddirectory.types.schema_facet.deserialize_json(
            data["SchemaFacet"]
        )
    else:
        raise DeserializationError("BatchAddFacetToObject.schema_facet required")
    if data.get("ObjectAttributeList") is not None:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["object_attribute_list"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["ObjectAttributeList"]
            )
        )
    else:
        out["object_attribute_list"] = []
    if data.get("ObjectReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("BatchAddFacetToObject.object_reference required")
    return out
