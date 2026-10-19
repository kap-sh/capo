"""Generated from Smithy shape ``com.amazonaws.iotevents#InitializationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.disabled_on_initialization


class InitializationConfiguration(TypedDict, closed=True):
    disabled_on_initialization: (
        "capo_iot_events.types.disabled_on_initialization.DisabledOnInitialization"
    )
    """<p>The value must be <code>TRUE</code> or <code>FALSE</code>. If <code>FALSE</code>, all alarm instances created based on the alarm model are activated. The default value is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitializationConfiguration) -> dict:
    out: dict = {}
    out["disabledOnInitialization"] = value["disabled_on_initialization"]
    return out


def deserialize_json(data: dict) -> InitializationConfiguration:
    out: InitializationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("disabledOnInitialization") is not None:
        out["disabled_on_initialization"] = data["disabledOnInitialization"]
    else:
        out["disabled_on_initialization"] = False
    return out
