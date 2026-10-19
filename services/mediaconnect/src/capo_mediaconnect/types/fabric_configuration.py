"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FabricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.fabric_latency_mode


class FabricConfiguration(TypedDict, closed=True):
    recovery_latency_mode: (
        "capo_mediaconnect.types.fabric_latency_mode.FabricLatencyMode"
    )
    """<p>The recovery latency mode for the router fabric connection. Valid values include the following:</p> <ul> <li> <p> <code>BALANCED</code> (default) – Optimizes for stream quality.</p> </li> <li> <p> <code>LOW_LATENCY</code> – Reduces latency at the potential cost of stream quality under adverse network conditions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FabricConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.fabric_latency_mode

    out["recoveryLatencyMode"] = (
        capo_mediaconnect.types.fabric_latency_mode.serialize_json(
            value["recovery_latency_mode"]
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
    return out
