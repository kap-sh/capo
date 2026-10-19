"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#InputContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.input_context_name


class InputContext(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.input_context_name.InputContextName"
    """<p>The name of the context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> InputContext:
    out: InputContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
