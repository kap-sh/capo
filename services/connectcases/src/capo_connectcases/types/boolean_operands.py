"""Generated from Smithy shape ``com.amazonaws.connectcases#BooleanOperands``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.operand_one
    import capo_connectcases.types.operand_two


class BooleanOperands(TypedDict, closed=True):
    operand_one: "capo_connectcases.types.operand_one.OperandOne"
    """<p>Represents the left hand operand in the condition.</p>"""
    operand_two: "capo_connectcases.types.operand_two.OperandTwo"
    """<p>Represents the right hand operand in the condition.</p>"""
    result: "bool"
    """<p>The value of the outer rule if the condition evaluates to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BooleanOperands) -> dict:
    out: dict = {}
    import capo_connectcases.types.operand_one

    out["operandOne"] = capo_connectcases.types.operand_one.serialize_json(
        value["operand_one"]
    )
    import capo_connectcases.types.operand_two

    out["operandTwo"] = capo_connectcases.types.operand_two.serialize_json(
        value["operand_two"]
    )
    out["result"] = value["result"]
    return out


def deserialize_json(data: dict) -> BooleanOperands:
    out: BooleanOperands = {}  # type: ignore[typeddict-item]
    if data.get("operandOne") is not None:
        import capo_connectcases.types.operand_one

        out["operand_one"] = capo_connectcases.types.operand_one.deserialize_json(
            data["operandOne"]
        )
    else:
        import capo_connectcases.types._unknown

        out["operand_one"] = capo_connectcases.types._unknown.UnknownUnionMember("")
    if data.get("operandTwo") is not None:
        import capo_connectcases.types.operand_two

        out["operand_two"] = capo_connectcases.types.operand_two.deserialize_json(
            data["operandTwo"]
        )
    else:
        import capo_connectcases.types._unknown

        out["operand_two"] = capo_connectcases.types._unknown.UnknownUnionMember("")
    if data.get("result") is not None:
        out["result"] = data["result"]
    else:
        out["result"] = False
    return out
