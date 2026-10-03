"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetLinkAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_name_list
    import capo_clouddirectory.types.consistency_level
    import capo_clouddirectory.types.typed_link_specifier


class GetLinkAttributesRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see <a>arns</a> or <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""
    typed_link_specifier: (
        "capo_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Allows a typed link specifier to be accepted as input.</p>"""
    attribute_names: "capo_clouddirectory.types.attribute_name_list.AttributeNameList"
    """<p>A list of attribute names whose values will be retrieved.</p>"""
    consistency_level: NotRequired[
        "capo_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level at which to retrieve the attributes on a typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkAttributesRequest) -> dict:
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
    if "consistency_level" in value:
        import capo_clouddirectory.types.consistency_level

        out["ConsistencyLevel"] = (
            capo_clouddirectory.types.consistency_level.serialize_json(
                value["consistency_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLinkAttributesRequest:
    out: GetLinkAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TypedLinkSpecifier") is not None:
        import capo_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            capo_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError(
            "GetLinkAttributesRequest.typed_link_specifier required"
        )
    if data.get("AttributeNames") is not None:
        import capo_clouddirectory.types.attribute_name_list

        out["attribute_names"] = (
            capo_clouddirectory.types.attribute_name_list.deserialize_json(
                data["AttributeNames"]
            )
        )
    else:
        raise DeserializationError("GetLinkAttributesRequest.attribute_names required")
    if data.get("ConsistencyLevel") is not None:
        import capo_clouddirectory.types.consistency_level

        out["consistency_level"] = (
            capo_clouddirectory.types.consistency_level.deserialize_json(
                data["ConsistencyLevel"]
            )
        )
    return out
