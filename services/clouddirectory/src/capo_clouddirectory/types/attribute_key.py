"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_name
    import capo_clouddirectory.types.facet_name


class AttributeKey(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.</p>"""
    facet_name: "capo_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet that the attribute exists within.</p>"""
    name: "capo_clouddirectory.types.attribute_name.AttributeName"
    """<p>The name of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeKey) -> dict:
    out: dict = {}
    out["SchemaArn"] = value["schema_arn"]
    out["FacetName"] = value["facet_name"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AttributeKey:
    out: AttributeKey = {}  # type: ignore[typeddict-item]
    if data.get("SchemaArn") is not None:
        out["schema_arn"] = data["SchemaArn"]
    else:
        out["schema_arn"] = ""
    if data.get("FacetName") is not None:
        out["facet_name"] = data["FacetName"]
    else:
        out["facet_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
