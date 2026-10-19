"""Generated from Smithy shape ``com.amazonaws.iot#SetV2LoggingLevelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.log_level
    import capo_iot.types.log_target


class SetV2LoggingLevelRequest(TypedDict, closed=True):
    log_target: "capo_iot.types.log_target.LogTarget"
    """<p>The log target.</p>"""
    log_level: "capo_iot.types.log_level.LogLevel"
    """<p>The log level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetV2LoggingLevelRequest) -> dict:
    out: dict = {}
    import capo_iot.types.log_target

    out["logTarget"] = capo_iot.types.log_target.serialize_json(value["log_target"])
    import capo_iot.types.log_level

    out["logLevel"] = capo_iot.types.log_level.serialize_json(value["log_level"])
    return out


def deserialize_json(data: dict) -> SetV2LoggingLevelRequest:
    out: SetV2LoggingLevelRequest = {}  # type: ignore[typeddict-item]
    if data.get("logTarget") is not None:
        import capo_iot.types.log_target

        out["log_target"] = capo_iot.types.log_target.deserialize_json(
            data["logTarget"]
        )
    else:
        raise DeserializationError("SetV2LoggingLevelRequest.log_target required")
    if data.get("logLevel") is not None:
        import capo_iot.types.log_level

        out["log_level"] = capo_iot.types.log_level.deserialize_json(data["logLevel"])
    else:
        import typing

        out["log_level"] = typing.cast("capo_iot.types.log_level.LogLevel", "")
    return out
