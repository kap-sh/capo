"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.join_operand_properties
    import capo_quicksight.types.join_operation_on_clause
    import capo_quicksight.types.join_operation_type
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class JoinOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    left_operand: (
        "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The left operand for the join operation.</p>"""
    right_operand: (
        "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    )
    """<p>The right operand for the join operation.</p>"""
    type: "capo_quicksight.types.join_operation_type.JoinOperationType"
    """<p>The type of join to perform, such as <code>INNER</code>, <code>LEFT</code>, <code>RIGHT</code>, or <code>OUTER</code>.</p>"""
    on_clause: "capo_quicksight.types.join_operation_on_clause.JoinOperationOnClause"
    """<p>The join condition that specifies how to match rows between the left and right operands.</p>"""
    left_operand_properties: NotRequired[
        "capo_quicksight.types.join_operand_properties.JoinOperandProperties"
    ]
    """<p>Properties that control how the left operand's columns are handled in the join result.</p>"""
    right_operand_properties: NotRequired[
        "capo_quicksight.types.join_operand_properties.JoinOperandProperties"
    ]
    """<p>Properties that control how the right operand's columns are handled in the join result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.transform_operation_source

    out["LeftOperand"] = (
        capo_quicksight.types.transform_operation_source.serialize_json(
            value["left_operand"]
        )
    )
    import capo_quicksight.types.transform_operation_source

    out["RightOperand"] = (
        capo_quicksight.types.transform_operation_source.serialize_json(
            value["right_operand"]
        )
    )
    import capo_quicksight.types.join_operation_type

    out["Type"] = capo_quicksight.types.join_operation_type.serialize_json(
        value["type"]
    )
    out["OnClause"] = value["on_clause"]
    if "left_operand_properties" in value:
        import capo_quicksight.types.join_operand_properties

        out["LeftOperandProperties"] = (
            capo_quicksight.types.join_operand_properties.serialize_json(
                value["left_operand_properties"]
            )
        )
    if "right_operand_properties" in value:
        import capo_quicksight.types.join_operand_properties

        out["RightOperandProperties"] = (
            capo_quicksight.types.join_operand_properties.serialize_json(
                value["right_operand_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> JoinOperation:
    out: JoinOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("LeftOperand") is not None:
        import capo_quicksight.types.transform_operation_source

        out["left_operand"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["LeftOperand"]
            )
        )
    else:
        raise DeserializationError("JoinOperation.left_operand required")
    if data.get("RightOperand") is not None:
        import capo_quicksight.types.transform_operation_source

        out["right_operand"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["RightOperand"]
            )
        )
    else:
        raise DeserializationError("JoinOperation.right_operand required")
    if data.get("Type") is not None:
        import capo_quicksight.types.join_operation_type

        out["type"] = capo_quicksight.types.join_operation_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.join_operation_type.JoinOperationType", ""
        )
    if data.get("OnClause") is not None:
        out["on_clause"] = data["OnClause"]
    else:
        out["on_clause"] = ""
    if data.get("LeftOperandProperties") is not None:
        import capo_quicksight.types.join_operand_properties

        out["left_operand_properties"] = (
            capo_quicksight.types.join_operand_properties.deserialize_json(
                data["LeftOperandProperties"]
            )
        )
    if data.get("RightOperandProperties") is not None:
        import capo_quicksight.types.join_operand_properties

        out["right_operand_properties"] = (
            capo_quicksight.types.join_operand_properties.deserialize_json(
                data["RightOperandProperties"]
            )
        )
    return out


def redact_sensitive(value: JoinOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "on_clause" in value:
        out["on_clause"] = "*** Sensitive Data Redacted ***"
    return out
