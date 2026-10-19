"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TextInputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.time_in_milli_seconds


class TextInputSpecification(TypedDict, closed=True):
    start_timeout_ms: (
        "capo_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>Time for which a bot waits before re-prompting a customer for text input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputSpecification) -> dict:
    out: dict = {}
    out["startTimeoutMs"] = value["start_timeout_ms"]
    return out


def deserialize_json(data: dict) -> TextInputSpecification:
    out: TextInputSpecification = {}  # type: ignore[typeddict-item]
    if data.get("startTimeoutMs") is not None:
        out["start_timeout_ms"] = data["startTimeoutMs"]
    else:
        out["start_timeout_ms"] = 0
    return out
