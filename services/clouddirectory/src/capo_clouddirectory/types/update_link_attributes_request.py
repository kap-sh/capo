"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateLinkAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.link_attribute_update_list
    import capo_clouddirectory.types.typed_link_specifier


class UpdateLinkAttributesRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see <a>arns</a> or <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    typed_link_specifier: (
        "capo_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Allows a typed link specifier to be accepted as input.</p>"""
    attribute_updates: (
        "capo_clouddirectory.types.link_attribute_update_list.LinkAttributeUpdateList"
    )
    """<p>The attributes update structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkAttributesRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateLinkAttributesRequest:
    out: UpdateLinkAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TypedLinkSpecifier") is not None:
        import capo_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            capo_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLinkAttributesRequest.typed_link_specifier required"
        )
    if data.get("AttributeUpdates") is not None:
        import capo_clouddirectory.types.link_attribute_update_list

        out["attribute_updates"] = (
            capo_clouddirectory.types.link_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLinkAttributesRequest.attribute_updates required"
        )
    return out
