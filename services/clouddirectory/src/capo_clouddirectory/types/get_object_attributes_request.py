"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetObjectAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_name_list
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet


class GetObjectAttributesRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the object whose attributes will be retrieved.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level at which to retrieve the attributes on an object.</p>"""
    schema_facet: "capo_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>Identifier for the facet whose attributes will be retrieved. See <a>SchemaFacet</a> for details.</p>"""
    attribute_names: "capo_clouddirectory.types.attribute_name_list.AttributeNameList"
    """<p>List of attribute names whose values will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectAttributesRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    import capo_clouddirectory.types.schema_facet

    out["SchemaFacet"] = capo_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
    import capo_clouddirectory.types.attribute_name_list

    out["AttributeNames"] = (
        capo_clouddirectory.types.attribute_name_list.serialize_json(
            value["attribute_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetObjectAttributesRequest:
    out: GetObjectAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ObjectReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectAttributesRequest.object_reference required"
        )
    if data.get("SchemaFacet") is not None:
        import capo_clouddirectory.types.schema_facet

        out["schema_facet"] = capo_clouddirectory.types.schema_facet.deserialize_json(
            data["SchemaFacet"]
        )
    else:
        raise DeserializationError("GetObjectAttributesRequest.schema_facet required")
    if data.get("AttributeNames") is not None:
        import capo_clouddirectory.types.attribute_name_list

        out["attribute_names"] = (
            capo_clouddirectory.types.attribute_name_list.deserialize_json(
                data["AttributeNames"]
            )
        )
    else:
        out["attribute_names"] = []
    return out
