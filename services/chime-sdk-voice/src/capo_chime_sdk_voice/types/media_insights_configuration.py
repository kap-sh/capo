"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#MediaInsightsConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.boolean


class MediaInsightsConfiguration(TypedDict, closed=True):
    disabled: NotRequired["capo_chime_sdk_voice.types.boolean.Boolean"]
    """<p>Denotes the configuration as enabled or disabled.</p>"""
    configuration_arn: NotRequired["capo_chime_sdk_voice.types.arn.Arn"]
    """<p>The configuration's ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsConfiguration) -> dict:
    out: dict = {}
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "configuration_arn" in value:
        out["ConfigurationArn"] = value["configuration_arn"]
    return out


def deserialize_json(data: dict) -> MediaInsightsConfiguration:
    out: MediaInsightsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    if data.get("ConfigurationArn") is not None:
        out["configuration_arn"] = data["ConfigurationArn"]
    return out


def redact_sensitive(value: MediaInsightsConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_arn" in value:
        out["configuration_arn"] = "*** Sensitive Data Redacted ***"
    return out
