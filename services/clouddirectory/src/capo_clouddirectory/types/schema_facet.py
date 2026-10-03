"""Generated from Smithy shape ``com.amazonaws.clouddirectory#SchemaFacet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.facet_name


class SchemaFacet(TypedDict, closed=True):
    schema_arn: NotRequired["capo_clouddirectory.types.arn.Arn"]
    """<p>The ARN of the schema that contains the facet with no minor component. See <a>arns</a> and <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html">In-Place Schema Upgrade</a> for a description of when to provide minor versions. If this value is set, FacetName must also be set.</p>"""
    facet_name: NotRequired["capo_clouddirectory.types.facet_name.FacetName"]
    """<p>The name of the facet. If this value is set, SchemaArn must also be set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaFacet) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["SchemaArn"] = value["schema_arn"]
    if "facet_name" in value:
        out["FacetName"] = value["facet_name"]
    return out


def deserialize_json(data: dict) -> SchemaFacet:
    out: SchemaFacet = {}  # type: ignore[typeddict-item]
    if data.get("SchemaArn") is not None:
        out["schema_arn"] = data["SchemaArn"]
    if data.get("FacetName") is not None:
        out["facet_name"] = data["FacetName"]
    return out
