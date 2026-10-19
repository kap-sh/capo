"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ActiveContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.active_context_name


class ActiveContext(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.active_context_name.ActiveContextName"
    """<p>The name of active context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ActiveContext:
    out: ActiveContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
