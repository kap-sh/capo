"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.insight_field_type
    import capo_opensearch.types.string


class InsightField(TypedDict, closed=True):
    name: "capo_opensearch.types.string.String"
    """<p>The name of the insight field.</p>"""
    type: "capo_opensearch.types.insight_field_type.InsightFieldType"
    """<p>The type of the insight field. Possible values are <code>text</code> and <code>metric</code>.</p>"""
    value: "capo_opensearch.types.string.String"
    """<p>The value of the insight field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_opensearch.types.insight_field_type

    out["Type"] = capo_opensearch.types.insight_field_type.serialize_json(value["type"])
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> InsightField:
    out: InsightField = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_opensearch.types.insight_field_type

        out["type"] = capo_opensearch.types.insight_field_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_opensearch.types.insight_field_type.InsightFieldType", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
