"""Generated from Smithy shape ``com.amazonaws.iot#EnableIoTLoggingParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.log_level
    import capo_iot.types.role_arn


class EnableIoTLoggingParams(TypedDict, closed=True):
    role_arn_for_logging: "capo_iot.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used for logging.</p>"""
    log_level: "capo_iot.types.log_level.LogLevel"
    """<p>Specifies the type of information to be logged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableIoTLoggingParams) -> dict:
    out: dict = {}
    out["roleArnForLogging"] = value["role_arn_for_logging"]
    import capo_iot.types.log_level

    out["logLevel"] = capo_iot.types.log_level.serialize_json(value["log_level"])
    return out


def deserialize_json(data: dict) -> EnableIoTLoggingParams:
    out: EnableIoTLoggingParams = {}  # type: ignore[typeddict-item]
    if data.get("roleArnForLogging") is not None:
        out["role_arn_for_logging"] = data["roleArnForLogging"]
    else:
        out["role_arn_for_logging"] = ""
    if data.get("logLevel") is not None:
        import capo_iot.types.log_level

        out["log_level"] = capo_iot.types.log_level.deserialize_json(data["logLevel"])
    else:
        import typing

        out["log_level"] = typing.cast("capo_iot.types.log_level.LogLevel", "")
    return out
