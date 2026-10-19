"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.command_parameter_value_comparison_operand
    import capo_iot.types.command_parameter_value_comparison_operator


class CommandParameterValueCondition(TypedDict, closed=True):
    comparison_operator: "capo_iot.types.command_parameter_value_comparison_operator.CommandParameterValueComparisonOperator"
    """<p>The comparison operator for the command parameter.</p> <note> <p>IN_RANGE, and NOT_IN_RANGE operators include boundary values.</p> </note>"""
    operand: "capo_iot.types.command_parameter_value_comparison_operand.CommandParameterValueComparisonOperand"
    """<p>The comparison operand for the command parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueCondition) -> dict:
    out: dict = {}
    import capo_iot.types.command_parameter_value_comparison_operator

    out["comparisonOperator"] = (
        capo_iot.types.command_parameter_value_comparison_operator.serialize_json(
            value["comparison_operator"]
        )
    )
    import capo_iot.types.command_parameter_value_comparison_operand

    out["operand"] = (
        capo_iot.types.command_parameter_value_comparison_operand.serialize_json(
            value["operand"]
        )
    )
    return out


def deserialize_json(data: dict) -> CommandParameterValueCondition:
    out: CommandParameterValueCondition = {}  # type: ignore[typeddict-item]
    if data.get("comparisonOperator") is not None:
        import capo_iot.types.command_parameter_value_comparison_operator

        out["comparison_operator"] = (
            capo_iot.types.command_parameter_value_comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    else:
        import typing

        out["comparison_operator"] = typing.cast(
            "capo_iot.types.command_parameter_value_comparison_operator.CommandParameterValueComparisonOperator",
            "",
        )
    if data.get("operand") is not None:
        import capo_iot.types.command_parameter_value_comparison_operand

        out["operand"] = (
            capo_iot.types.command_parameter_value_comparison_operand.deserialize_json(
                data["operand"]
            )
        )
    else:
        raise DeserializationError("CommandParameterValueCondition.operand required")
    return out
