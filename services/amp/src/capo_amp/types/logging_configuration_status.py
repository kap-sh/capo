"""Generated from Smithy shape ``com.amazonaws.amp#LoggingConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.logging_configuration_status_code


class LoggingConfigurationStatus(TypedDict, closed=True):
    status_code: "capo_amp.types.logging_configuration_status_code.LoggingConfigurationStatusCode"
    """<p>The current status of the current rules and alerting logging configuration.</p> <note> <p>These logging configurations are only for rules and alerting logs.</p> </note>"""
    status_reason: NotRequired["str"]
    """<p>If failed, the reason for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> LoggingConfigurationStatus:
    out: LoggingConfigurationStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        out["status_code"] = ""
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
