"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.facet_name


class DeleteFacetRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>"""
    name: "capo_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteFacetRequest:
    out: DeleteFacetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
