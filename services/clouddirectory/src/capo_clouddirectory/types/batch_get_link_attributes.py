"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchGetLinkAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name_list
    import capo_clouddirectory.types.typed_link_specifier


class BatchGetLinkAttributes(TypedDict, closed=True):
    typed_link_specifier: (
        "capo_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Allows a typed link specifier to be accepted as input.</p>"""
    attribute_names: "capo_clouddirectory.types.attribute_name_list.AttributeNameList"
    """<p>A list of attribute names whose values will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetLinkAttributes) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.typed_link_specifier

    out["TypedLinkSpecifier"] = (
        capo_clouddirectory.types.typed_link_specifier.serialize_json(
            value["typed_link_specifier"]
        )
    )
    import capo_clouddirectory.types.attribute_name_list

    out["AttributeNames"] = (
        capo_clouddirectory.types.attribute_name_list.serialize_json(
            value["attribute_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetLinkAttributes:
    out: BatchGetLinkAttributes = {}  # type: ignore[typeddict-item]
    if data.get("TypedLinkSpecifier") is not None:
        import capo_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            capo_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetLinkAttributes.typed_link_specifier required"
        )
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
