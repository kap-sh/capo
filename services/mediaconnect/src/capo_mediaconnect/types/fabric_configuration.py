"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FabricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.fabric_latency_mode
    import capo_mediaconnect.types.fabric_switching_configuration
    import capo_mediaconnect.types.fabric_switching_mode


class FabricConfiguration(TypedDict, closed=True):
    recovery_latency_mode: (
        "capo_mediaconnect.types.fabric_latency_mode.FabricLatencyMode"
    )
    """<p>The recovery latency mode for the router fabric connection. Valid values include the following:</p> <ul> <li> <p> <code>BALANCED</code> (default) – Optimizes for stream quality.</p> </li> <li> <p> <code>LOW_LATENCY</code> – Reduces latency at the potential cost of stream quality under adverse network conditions.</p> </li> </ul>"""
    switching_mode: NotRequired[
        "capo_mediaconnect.types.fabric_switching_mode.FabricSwitchingMode"
    ]
    """<p>The switching mode that the router output uses when it switches to a new router input. Valid values include the following:</p> <ul> <li> <p> <code>IMMEDIATE</code> (default) – Switches to the new router input immediately.</p> </li> <li> <p> <code>KEY_FRAME</code> – Waits for a key frame on the new router input before it switches.</p> </li> </ul> <p>If you specify it, it must match the switching configuration.</p>"""
    switching_configuration: NotRequired[
        "capo_mediaconnect.types.fabric_switching_configuration.FabricSwitchingConfiguration"
    ]
    """<p>The configuration settings for the switching mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FabricConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.fabric_latency_mode

    out["recoveryLatencyMode"] = (
        capo_mediaconnect.types.fabric_latency_mode.serialize_json(
            value["recovery_latency_mode"]
        )
    )
    if "switching_mode" in value:
        import capo_mediaconnect.types.fabric_switching_mode

        out["switchingMode"] = (
            capo_mediaconnect.types.fabric_switching_mode.serialize_json(
                value["switching_mode"]
            )
        )
    if "switching_configuration" in value:
        import capo_mediaconnect.types.fabric_switching_configuration

        out["switchingConfiguration"] = (
            capo_mediaconnect.types.fabric_switching_configuration.serialize_json(
                value["switching_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FabricConfiguration:
    out: FabricConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("recoveryLatencyMode") is not None:
        import capo_mediaconnect.types.fabric_latency_mode

        out["recovery_latency_mode"] = (
            capo_mediaconnect.types.fabric_latency_mode.deserialize_json(
                data["recoveryLatencyMode"]
            )
        )
    else:
        import typing

        out["recovery_latency_mode"] = typing.cast(
            "capo_mediaconnect.types.fabric_latency_mode.FabricLatencyMode", ""
        )
    if data.get("switchingMode") is not None:
        import capo_mediaconnect.types.fabric_switching_mode

        out["switching_mode"] = (
            capo_mediaconnect.types.fabric_switching_mode.deserialize_json(
                data["switchingMode"]
            )
        )
    if data.get("switchingConfiguration") is not None:
        import capo_mediaconnect.types.fabric_switching_configuration

        out["switching_configuration"] = (
            capo_mediaconnect.types.fabric_switching_configuration.deserialize_json(
                data["switchingConfiguration"]
            )
        )
    return out
