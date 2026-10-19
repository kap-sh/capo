"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExpressionVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.variable_name
    import capo_iotsitewise.types.variable_value


class ExpressionVariable(TypedDict, closed=True):
    name: "capo_iotsitewise.types.variable_name.VariableName"
    """<p>The friendly name of the variable to be used in the expression.</p>"""
    value: "capo_iotsitewise.types.variable_value.VariableValue"
    """<p>The variable that identifies an asset property from which to use values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressionVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_iotsitewise.types.variable_value

    out["value"] = capo_iotsitewise.types.variable_value.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> ExpressionVariable:
    out: ExpressionVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        import capo_iotsitewise.types.variable_value

        out["value"] = capo_iotsitewise.types.variable_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("ExpressionVariable.value required")
    return out
