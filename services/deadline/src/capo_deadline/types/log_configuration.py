"""Generated from Smithy shape ``com.amazonaws.deadline#LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.log_driver
    import capo_deadline.types.log_error
    import capo_deadline.types.log_options
    import capo_deadline.types.log_parameters


class LogConfiguration(TypedDict, closed=True):
    log_driver: "capo_deadline.types.log_driver.LogDriver"
    """<p>The log drivers for worker related logs.</p>"""
    options: NotRequired["capo_deadline.types.log_options.LogOptions"]
    """<p>The options for a log driver.</p>"""
    parameters: NotRequired["capo_deadline.types.log_parameters.LogParameters"]
    """<p>The parameters for the log configuration.</p>"""
    error: NotRequired["capo_deadline.types.log_error.LogError"]
    """<p>The log configuration error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfiguration) -> dict:
    out: dict = {}
    out["logDriver"] = value["log_driver"]
    if "options" in value:
        import capo_deadline.types.log_options

        out["options"] = capo_deadline.types.log_options.serialize_json(
            value["options"]
        )
    if "parameters" in value:
        import capo_deadline.types.log_parameters

        out["parameters"] = capo_deadline.types.log_parameters.serialize_json(
            value["parameters"]
        )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logDriver") is not None:
        out["log_driver"] = data["logDriver"]
    else:
        out["log_driver"] = ""
    if data.get("options") is not None:
        import capo_deadline.types.log_options

        out["options"] = capo_deadline.types.log_options.deserialize_json(
            data["options"]
        )
    if data.get("parameters") is not None:
        import capo_deadline.types.log_parameters

        out["parameters"] = capo_deadline.types.log_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("error") is not None:
        out["error"] = data["error"]
    return out
