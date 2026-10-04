"""Generated from Smithy shape ``com.amazonaws.lambdaweb#TelemetryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.logging_config


class TelemetryConfig(TypedDict, closed=True):
    logging_config: NotRequired["capo_lambda_web.types.logging_config.LoggingConfig"]
    """<p>The logging configuration for the web function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfig) -> dict:
    out: dict = {}
    if "logging_config" in value:
        import capo_lambda_web.types.logging_config

        out["loggingConfig"] = capo_lambda_web.types.logging_config.serialize_json(
            value["logging_config"]
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfig:
    out: TelemetryConfig = {}  # type: ignore[typeddict-item]
    if data.get("loggingConfig") is not None:
        import capo_lambda_web.types.logging_config

        out["logging_config"] = capo_lambda_web.types.logging_config.deserialize_json(
            data["loggingConfig"]
        )
    return out
