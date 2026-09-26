"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PolicyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.remediation_enabled
    import capo_network_security_manager.types.resources_clean_up
    import capo_network_security_manager.types.waf_config


class PolicyConfiguration(TypedDict, closed=True):
    remediation_enabled: (
        "capo_network_security_manager.types.remediation_enabled.RemediationEnabled"
    )
    """<p>Specifies whether AWS Network Security Manager automatically remediates noncompliant resources. Default: <code>false</code>.</p>"""
    resources_clean_up: (
        "capo_network_security_manager.types.resources_clean_up.ResourcesCleanUp"
    )
    """<p>Specifies whether AWS Network Security Manager automatically removes the resources it created when they are no longer needed. Default: <code>false</code>.</p>"""
    waf_config: NotRequired["capo_network_security_manager.types.waf_config.WafConfig"]
    """<p>AWS WAF-specific policy settings. This is populated only for AWS WAF policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyConfiguration) -> dict:
    out: dict = {}
    out["remediationEnabled"] = value.get("remediation_enabled", False)
    out["resourcesCleanUp"] = value.get("resources_clean_up", False)
    if "waf_config" in value:
        import capo_network_security_manager.types.waf_config

        out["wafConfig"] = (
            capo_network_security_manager.types.waf_config.serialize_json(
                value["waf_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> PolicyConfiguration:
    out: PolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("remediationEnabled") is not None:
        out["remediation_enabled"] = data["remediationEnabled"]
    else:
        out["remediation_enabled"] = False
    if data.get("resourcesCleanUp") is not None:
        out["resources_clean_up"] = data["resourcesCleanUp"]
    else:
        out["resources_clean_up"] = False
    if data.get("wafConfig") is not None:
        import capo_network_security_manager.types.waf_config

        out["waf_config"] = (
            capo_network_security_manager.types.waf_config.deserialize_json(
                data["wafConfig"]
            )
        )
    return out
