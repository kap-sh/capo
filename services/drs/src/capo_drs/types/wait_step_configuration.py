"""Generated from Smithy shape ``com.amazonaws.drs#WaitStepConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.wait_duration_minutes


class WaitStepConfiguration(TypedDict, closed=True):
    wait_duration_minutes: "capo_drs.types.wait_duration_minutes.WaitDurationMinutes"


# --- restJson1 ser/de ---
def serialize_json(value: WaitStepConfiguration) -> dict:
    out: dict = {}
    out["waitDurationMinutes"] = value["wait_duration_minutes"]
    return out


def deserialize_json(data: dict) -> WaitStepConfiguration:
    out: WaitStepConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("waitDurationMinutes") is not None:
        out["wait_duration_minutes"] = data["waitDurationMinutes"]
    else:
        out["wait_duration_minutes"] = 0
    return out
