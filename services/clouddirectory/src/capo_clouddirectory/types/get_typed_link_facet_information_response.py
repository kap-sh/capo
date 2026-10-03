"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetTypedLinkFacetInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name_list


class GetTypedLinkFacetInformationResponse(TypedDict, closed=True):
    identity_attribute_order: NotRequired[
        "capo_clouddirectory.types.attribute_name_list.AttributeNameList"
    ]
    """<p>The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink">Typed Links</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTypedLinkFacetInformationResponse) -> dict:
    out: dict = {}
    if "identity_attribute_order" in value:
        import capo_clouddirectory.types.attribute_name_list

        out["IdentityAttributeOrder"] = (
            capo_clouddirectory.types.attribute_name_list.serialize_json(
                value["identity_attribute_order"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTypedLinkFacetInformationResponse:
    out: GetTypedLinkFacetInformationResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityAttributeOrder") is not None:
        import capo_clouddirectory.types.attribute_name_list

        out["identity_attribute_order"] = (
            capo_clouddirectory.types.attribute_name_list.deserialize_json(
                data["IdentityAttributeOrder"]
            )
        )
    return out
