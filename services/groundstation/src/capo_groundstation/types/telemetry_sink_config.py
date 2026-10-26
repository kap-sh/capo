"""Generated from Smithy shape ``com.amazonaws.groundstation#TelemetrySinkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.telemetry_sink_data
    import capo_groundstation.types.telemetry_sink_type


class TelemetrySinkConfig(TypedDict, closed=True):
    telemetry_sink_type: (
        "capo_groundstation.types.telemetry_sink_type.TelemetrySinkType"
    )
    """<p>The type of telemetry sink.</p>"""
    telemetry_sink_data: (
        "capo_groundstation.types.telemetry_sink_data.TelemetrySinkData"
    )
    """<p>Information about the telemetry sink specified by the <code>telemetrySinkType</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySinkConfig) -> dict:
    out: dict = {}
    import capo_groundstation.types.telemetry_sink_type

    out["telemetrySinkType"] = (
        capo_groundstation.types.telemetry_sink_type.serialize_json(
            value["telemetry_sink_type"]
        )
    )
    import capo_groundstation.types.telemetry_sink_data

    out["telemetrySinkData"] = (
        capo_groundstation.types.telemetry_sink_data.serialize_json(
            value["telemetry_sink_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> TelemetrySinkConfig:
    out: TelemetrySinkConfig = {}  # type: ignore[typeddict-item]
    if data.get("telemetrySinkType") is not None:
        import capo_groundstation.types.telemetry_sink_type

        out["telemetry_sink_type"] = (
            capo_groundstation.types.telemetry_sink_type.deserialize_json(
                data["telemetrySinkType"]
            )
        )
    else:
        import typing

        out["telemetry_sink_type"] = typing.cast(
            "capo_groundstation.types.telemetry_sink_type.TelemetrySinkType", ""
        )
    if data.get("telemetrySinkData") is not None:
        import capo_groundstation.types.telemetry_sink_data

        out["telemetry_sink_data"] = (
            capo_groundstation.types.telemetry_sink_data.deserialize_json(
                data["telemetrySinkData"]
            )
        )
    else:
        out["telemetry_sink_data"] = {"$unknown": {"name": ""}}
    return out
