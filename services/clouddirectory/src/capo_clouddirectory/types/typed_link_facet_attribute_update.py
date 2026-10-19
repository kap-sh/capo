"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkFacetAttributeUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_link_attribute_definition
    import capo_clouddirectory.types.update_action_type


class TypedLinkFacetAttributeUpdate(TypedDict, closed=True):
    attribute: "capo_clouddirectory.types.typed_link_attribute_definition.TypedLinkAttributeDefinition"
    """<p>The attribute to update.</p>"""
    action: "capo_clouddirectory.types.update_action_type.UpdateActionType"
    """<p>The action to perform when updating the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkFacetAttributeUpdate) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.typed_link_attribute_definition

    out["Attribute"] = (
        capo_clouddirectory.types.typed_link_attribute_definition.serialize_json(
            value["attribute"]
        )
    )
    import capo_clouddirectory.types.update_action_type

    out["Action"] = capo_clouddirectory.types.update_action_type.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> TypedLinkFacetAttributeUpdate:
    out: TypedLinkFacetAttributeUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        import capo_clouddirectory.types.typed_link_attribute_definition

        out["attribute"] = (
            capo_clouddirectory.types.typed_link_attribute_definition.deserialize_json(
                data["Attribute"]
            )
        )
    else:
        raise DeserializationError("TypedLinkFacetAttributeUpdate.attribute required")
    if data.get("Action") is not None:
        import capo_clouddirectory.types.update_action_type

        out["action"] = capo_clouddirectory.types.update_action_type.deserialize_json(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_clouddirectory.types.update_action_type.UpdateActionType", ""
        )
    return out
