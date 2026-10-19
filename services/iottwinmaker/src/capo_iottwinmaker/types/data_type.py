"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.data_type
    import capo_iottwinmaker.types.data_value_list
    import capo_iottwinmaker.types.relationship
    import capo_iottwinmaker.types.string
    import capo_iottwinmaker.types.type


class DataType(TypedDict, closed=True):
    type: "capo_iottwinmaker.types.type.Type"
    """<p>The underlying type of the data type.</p>"""
    nested_type: NotRequired["capo_iottwinmaker.types.data_type.DataType"]
    """<p>The nested type in the data type.</p>"""
    allowed_values: NotRequired["capo_iottwinmaker.types.data_value_list.DataValueList"]
    """<p>The allowed values for this data type.</p>"""
    unit_of_measure: NotRequired["capo_iottwinmaker.types.string.String"]
    """<p>The unit of measure used in this data type.</p>"""
    relationship: NotRequired["capo_iottwinmaker.types.relationship.Relationship"]
    """<p>A relationship that associates a component with another component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataType) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "nested_type" in value:
        import capo_iottwinmaker.types.data_type

        out["nestedType"] = capo_iottwinmaker.types.data_type.serialize_json(
            value["nested_type"]
        )
    if "allowed_values" in value:
        import capo_iottwinmaker.types.data_value_list

        out["allowedValues"] = capo_iottwinmaker.types.data_value_list.serialize_json(
            value["allowed_values"]
        )
    if "unit_of_measure" in value:
        out["unitOfMeasure"] = value["unit_of_measure"]
    if "relationship" in value:
        import capo_iottwinmaker.types.relationship

        out["relationship"] = capo_iottwinmaker.types.relationship.serialize_json(
            value["relationship"]
        )
    return out


def deserialize_json(data: dict) -> DataType:
    out: DataType = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("nestedType") is not None:
        import capo_iottwinmaker.types.data_type

        out["nested_type"] = capo_iottwinmaker.types.data_type.deserialize_json(
            data["nestedType"]
        )
    if data.get("allowedValues") is not None:
        import capo_iottwinmaker.types.data_value_list

        out["allowed_values"] = (
            capo_iottwinmaker.types.data_value_list.deserialize_json(
                data["allowedValues"]
            )
        )
    if data.get("unitOfMeasure") is not None:
        out["unit_of_measure"] = data["unitOfMeasure"]
    if data.get("relationship") is not None:
        import capo_iottwinmaker.types.relationship

        out["relationship"] = capo_iottwinmaker.types.relationship.deserialize_json(
            data["relationship"]
        )
    return out
