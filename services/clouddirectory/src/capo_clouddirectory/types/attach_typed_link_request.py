"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachTypedLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_name_and_value_list
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.typed_link_schema_and_facet_name


class AttachTypedLinkRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.</p>"""
    source_object_reference: (
        "capo_clouddirectory.types.object_reference.ObjectReference"
    )
    """<p>Identifies the source object that the typed link will attach to.</p>"""
    target_object_reference: (
        "capo_clouddirectory.types.object_reference.ObjectReference"
    )
    """<p>Identifies the target object that the typed link will attach to.</p>"""
    typed_link_facet: "capo_clouddirectory.types.typed_link_schema_and_facet_name.TypedLinkSchemaAndFacetName"
    """<p>Identifies the typed link facet that is associated with the typed link.</p>"""
    attributes: "capo_clouddirectory.types.attribute_name_and_value_list.AttributeNameAndValueList"
    """<p>A set of attributes that are associated with the typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachTypedLinkRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["SourceObjectReference"] = (
        capo_clouddirectory.types.object_reference.serialize_json(
            value["source_object_reference"]
        )
    )
    import capo_clouddirectory.types.object_reference

    out["TargetObjectReference"] = (
        capo_clouddirectory.types.object_reference.serialize_json(
            value["target_object_reference"]
        )
    )
    import capo_clouddirectory.types.typed_link_schema_and_facet_name

    out["TypedLinkFacet"] = (
        capo_clouddirectory.types.typed_link_schema_and_facet_name.serialize_json(
            value["typed_link_facet"]
        )
    )
    import capo_clouddirectory.types.attribute_name_and_value_list

    out["Attributes"] = (
        capo_clouddirectory.types.attribute_name_and_value_list.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> AttachTypedLinkRequest:
    out: AttachTypedLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceObjectReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["source_object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["SourceObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "AttachTypedLinkRequest.source_object_reference required"
        )
    if data.get("TargetObjectReference") is not None:
        import capo_clouddirectory.types.object_reference

        out["target_object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["TargetObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "AttachTypedLinkRequest.target_object_reference required"
        )
    if data.get("TypedLinkFacet") is not None:
        import capo_clouddirectory.types.typed_link_schema_and_facet_name

        out["typed_link_facet"] = (
            capo_clouddirectory.types.typed_link_schema_and_facet_name.deserialize_json(
                data["TypedLinkFacet"]
            )
        )
    else:
        raise DeserializationError("AttachTypedLinkRequest.typed_link_facet required")
    if data.get("Attributes") is not None:
        import capo_clouddirectory.types.attribute_name_and_value_list

        out["attributes"] = (
            capo_clouddirectory.types.attribute_name_and_value_list.deserialize_json(
                data["Attributes"]
            )
        )
    else:
        out["attributes"] = []
    return out
