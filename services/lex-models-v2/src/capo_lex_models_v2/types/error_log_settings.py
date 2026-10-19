"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ErrorLogSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean


class ErrorLogSettings(TypedDict, closed=True):
    enabled: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Settings parameters for the error logs, when it is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorLogSettings) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ErrorLogSettings:
    out: ErrorLogSettings = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
