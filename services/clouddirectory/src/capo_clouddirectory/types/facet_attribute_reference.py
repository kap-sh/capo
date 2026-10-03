"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name
    import capo_clouddirectory.types.facet_name


class FacetAttributeReference(TypedDict, closed=True):
    target_facet_name: "capo_clouddirectory.types.facet_name.FacetName"
    """<p>The target facet name that is associated with the facet reference. See <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html">Attribute References</a> for more information.</p>"""
    target_attribute_name: "capo_clouddirectory.types.attribute_name.AttributeName"
    """<p>The target attribute name that is associated with the facet reference. See <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html">Attribute References</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeReference) -> dict:
    out: dict = {}
    out["TargetFacetName"] = value["target_facet_name"]
    out["TargetAttributeName"] = value["target_attribute_name"]
    return out


def deserialize_json(data: dict) -> FacetAttributeReference:
    out: FacetAttributeReference = {}  # type: ignore[typeddict-item]
    if data.get("TargetFacetName") is not None:
        out["target_facet_name"] = data["TargetFacetName"]
    else:
        raise DeserializationError("FacetAttributeReference.target_facet_name required")
    if data.get("TargetAttributeName") is not None:
        out["target_attribute_name"] = data["TargetAttributeName"]
    else:
        raise DeserializationError(
            "FacetAttributeReference.target_attribute_name required"
        )
    return out
