"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetReputationMetricsEnabledRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.enabled


class UpdateConfigurationSetReputationMetricsEnabledRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set to update.</p>"""
    enabled: "capo_ses.types.enabled.Enabled"
    """<p>Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetReputationMetricsEnabledRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
    )
    pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_query(
    el: Element,
) -> UpdateConfigurationSetReputationMetricsEnabledRequest:
    out: UpdateConfigurationSetReputationMetricsEnabledRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        out["configuration_set_name"] = ""
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    return out
