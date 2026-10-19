"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchUpdateLinkAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.link_attribute_update_list
    import capo_clouddirectory.types.typed_link_specifier


class BatchUpdateLinkAttributes(TypedDict, closed=True):
    typed_link_specifier: (
        "capo_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Allows a typed link specifier to be accepted as input.</p>"""
    attribute_updates: (
        "capo_clouddirectory.types.link_attribute_update_list.LinkAttributeUpdateList"
    )
    """<p>The attributes update structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateLinkAttributes) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.typed_link_specifier

    out["TypedLinkSpecifier"] = (
        capo_clouddirectory.types.typed_link_specifier.serialize_json(
            value["typed_link_specifier"]
        )
    )
    import capo_clouddirectory.types.link_attribute_update_list

    out["AttributeUpdates"] = (
        capo_clouddirectory.types.link_attribute_update_list.serialize_json(
            value["attribute_updates"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateLinkAttributes:
    out: BatchUpdateLinkAttributes = {}  # type: ignore[typeddict-item]
    if data.get("TypedLinkSpecifier") is not None:
        import capo_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            capo_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateLinkAttributes.typed_link_specifier required"
        )
    if data.get("AttributeUpdates") is not None:
        import capo_clouddirectory.types.link_attribute_update_list

        out["attribute_updates"] = (
            capo_clouddirectory.types.link_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    else:
        out["attribute_updates"] = []
    return out
