"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.join_key_properties
    import capo_quicksight.types.join_type
    import capo_quicksight.types.logical_table_id
    import capo_quicksight.types.on_clause


class JoinInstruction(TypedDict, closed=True):
    left_operand: "capo_quicksight.types.logical_table_id.LogicalTableId"
    """<p>The operand on the left side of a join.</p>"""
    right_operand: "capo_quicksight.types.logical_table_id.LogicalTableId"
    """<p>The operand on the right side of a join.</p>"""
    left_join_key_properties: NotRequired[
        "capo_quicksight.types.join_key_properties.JoinKeyProperties"
    ]
    """<p>Join key properties of the left operand.</p>"""
    right_join_key_properties: NotRequired[
        "capo_quicksight.types.join_key_properties.JoinKeyProperties"
    ]
    """<p>Join key properties of the right operand.</p>"""
    type: "capo_quicksight.types.join_type.JoinType"
    """<p>The type of join that it is.</p>"""
    on_clause: "capo_quicksight.types.on_clause.OnClause"
    """<p>The join instructions provided in the <code>ON</code> clause of a join.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinInstruction) -> dict:
    out: dict = {}
    out["LeftOperand"] = value["left_operand"]
    out["RightOperand"] = value["right_operand"]
    if "left_join_key_properties" in value:
        import capo_quicksight.types.join_key_properties

        out["LeftJoinKeyProperties"] = (
            capo_quicksight.types.join_key_properties.serialize_json(
                value["left_join_key_properties"]
            )
        )
    if "right_join_key_properties" in value:
        import capo_quicksight.types.join_key_properties

        out["RightJoinKeyProperties"] = (
            capo_quicksight.types.join_key_properties.serialize_json(
                value["right_join_key_properties"]
            )
        )
    import capo_quicksight.types.join_type

    out["Type"] = capo_quicksight.types.join_type.serialize_json(value["type"])
    out["OnClause"] = value["on_clause"]
    return out


def deserialize_json(data: dict) -> JoinInstruction:
    out: JoinInstruction = {}  # type: ignore[typeddict-item]
    if data.get("LeftOperand") is not None:
        out["left_operand"] = data["LeftOperand"]
    else:
        out["left_operand"] = ""
    if data.get("RightOperand") is not None:
        out["right_operand"] = data["RightOperand"]
    else:
        out["right_operand"] = ""
    if data.get("LeftJoinKeyProperties") is not None:
        import capo_quicksight.types.join_key_properties

        out["left_join_key_properties"] = (
            capo_quicksight.types.join_key_properties.deserialize_json(
                data["LeftJoinKeyProperties"]
            )
        )
    if data.get("RightJoinKeyProperties") is not None:
        import capo_quicksight.types.join_key_properties

        out["right_join_key_properties"] = (
            capo_quicksight.types.join_key_properties.deserialize_json(
                data["RightJoinKeyProperties"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.join_type

        out["type"] = capo_quicksight.types.join_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_quicksight.types.join_type.JoinType", "")
    if data.get("OnClause") is not None:
        out["on_clause"] = data["OnClause"]
    else:
        out["on_clause"] = ""
    return out
