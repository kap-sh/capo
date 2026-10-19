"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateLFTagExpressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.description_string
    import capo_lakeformation.types.expression
    import capo_lakeformation.types.name_string


class UpdateLFTagExpressionRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name for the LF-Tag expression.</p>"""
    description: NotRequired[
        "capo_lakeformation.types.description_string.DescriptionString"
    ]
    """<p>The description with information about the saved LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. </p>"""
    expression: "capo_lakeformation.types.expression.Expression"
    """<p>The LF-Tag expression body composed of one more LF-Tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLFTagExpressionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.expression

    out["Expression"] = capo_lakeformation.types.expression.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLFTagExpressionRequest:
    out: UpdateLFTagExpressionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Expression") is not None:
        import capo_lakeformation.types.expression

        out["expression"] = capo_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    else:
        out["expression"] = []
    return out
