"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BurnRateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.burn_rate_look_back_window_minutes


class BurnRateConfiguration(TypedDict, closed=True):
    look_back_window_minutes: "capo_application_signals.types.burn_rate_look_back_window_minutes.BurnRateLookBackWindowMinutes"
    """<p>The number of minutes to use as the look-back window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BurnRateConfiguration) -> dict:
    out: dict = {}
    out["LookBackWindowMinutes"] = value["look_back_window_minutes"]
    return out


def deserialize_json(data: dict) -> BurnRateConfiguration:
    out: BurnRateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LookBackWindowMinutes") is not None:
        out["look_back_window_minutes"] = data["LookBackWindowMinutes"]
    else:
        out["look_back_window_minutes"] = 0
    return out
