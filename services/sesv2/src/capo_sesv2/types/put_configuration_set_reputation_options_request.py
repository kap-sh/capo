"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetReputationOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.enabled


class PutConfigurationSetReputationOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    reputation_metrics_enabled: NotRequired["capo_sesv2.types.enabled.Enabled"]
    """<p>If <code>true</code>, tracking of reputation metrics is enabled for the configuration set. If <code>false</code>, tracking of reputation metrics is disabled for the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetReputationOptionsRequest) -> dict:
    out: dict = {}
    if "reputation_metrics_enabled" in value:
        out["ReputationMetricsEnabled"] = value["reputation_metrics_enabled"]
    return out


def deserialize_json(data: dict) -> PutConfigurationSetReputationOptionsRequest:
    out: PutConfigurationSetReputationOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReputationMetricsEnabled") is not None:
        out["reputation_metrics_enabled"] = data["ReputationMetricsEnabled"]
    return out
