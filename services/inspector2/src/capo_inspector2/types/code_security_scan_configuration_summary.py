"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityScanConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.continuous_integration_scan_supported_events
    import capo_inspector2.types.frequency_expression
    import capo_inspector2.types.owner_id
    import capo_inspector2.types.periodic_scan_frequency
    import capo_inspector2.types.rule_set_categories
    import capo_inspector2.types.scan_configuration_arn
    import capo_inspector2.types.scan_configuration_name
    import capo_inspector2.types.scope_settings


class CodeSecurityScanConfigurationSummary(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration.</p>"""
    name: "capo_inspector2.types.scan_configuration_name.ScanConfigurationName"
    """<p>The name of the scan configuration.</p>"""
    owner_account_id: "capo_inspector2.types.owner_id.OwnerId"
    """<p>The Amazon Web Services account ID that owns the scan configuration.</p>"""
    periodic_scan_frequency: NotRequired[
        "capo_inspector2.types.periodic_scan_frequency.PeriodicScanFrequency"
    ]
    """<p>The frequency at which periodic scans are performed.</p>"""
    frequency_expression: NotRequired[
        "capo_inspector2.types.frequency_expression.FrequencyExpression"
    ]
    """<p>The schedule expression for periodic scans, in cron format.</p>"""
    continuous_integration_scan_supported_events: NotRequired[
        "capo_inspector2.types.continuous_integration_scan_supported_events.ContinuousIntegrationScanSupportedEvents"
    ]
    """<p>The repository events that trigger continuous integration scans.</p>"""
    rule_set_categories: "capo_inspector2.types.rule_set_categories.RuleSetCategories"
    """<p>The categories of security rules applied during the scan.</p>"""
    scope_settings: NotRequired["capo_inspector2.types.scope_settings.ScopeSettings"]
    """<p>The scope settings that define which repositories will be scanned. If the <code>ScopeSetting</code> parameter is <code>ALL</code> the scan configuration applies to all existing and future projects imported into Amazon Inspector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityScanConfigurationSummary) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    out["name"] = value["name"]
    out["ownerAccountId"] = value["owner_account_id"]
    if "periodic_scan_frequency" in value:
        import capo_inspector2.types.periodic_scan_frequency

        out["periodicScanFrequency"] = (
            capo_inspector2.types.periodic_scan_frequency.serialize_json(
                value["periodic_scan_frequency"]
            )
        )
    if "frequency_expression" in value:
        out["frequencyExpression"] = value["frequency_expression"]
    if "continuous_integration_scan_supported_events" in value:
        import capo_inspector2.types.continuous_integration_scan_supported_events

        out["continuousIntegrationScanSupportedEvents"] = (
            capo_inspector2.types.continuous_integration_scan_supported_events.serialize_json(
                value["continuous_integration_scan_supported_events"]
            )
        )
    import capo_inspector2.types.rule_set_categories

    out["ruleSetCategories"] = capo_inspector2.types.rule_set_categories.serialize_json(
        value["rule_set_categories"]
    )
    if "scope_settings" in value:
        import capo_inspector2.types.scope_settings

        out["scopeSettings"] = capo_inspector2.types.scope_settings.serialize_json(
            value["scope_settings"]
        )
    return out


def deserialize_json(data: dict) -> CodeSecurityScanConfigurationSummary:
    out: CodeSecurityScanConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    if data.get("periodicScanFrequency") is not None:
        import capo_inspector2.types.periodic_scan_frequency

        out["periodic_scan_frequency"] = (
            capo_inspector2.types.periodic_scan_frequency.deserialize_json(
                data["periodicScanFrequency"]
            )
        )
    if data.get("frequencyExpression") is not None:
        out["frequency_expression"] = data["frequencyExpression"]
    if data.get("continuousIntegrationScanSupportedEvents") is not None:
        import capo_inspector2.types.continuous_integration_scan_supported_events

        out["continuous_integration_scan_supported_events"] = (
            capo_inspector2.types.continuous_integration_scan_supported_events.deserialize_json(
                data["continuousIntegrationScanSupportedEvents"]
            )
        )
    if data.get("ruleSetCategories") is not None:
        import capo_inspector2.types.rule_set_categories

        out["rule_set_categories"] = (
            capo_inspector2.types.rule_set_categories.deserialize_json(
                data["ruleSetCategories"]
            )
        )
    else:
        out["rule_set_categories"] = []
    if data.get("scopeSettings") is not None:
        import capo_inspector2.types.scope_settings

        out["scope_settings"] = capo_inspector2.types.scope_settings.deserialize_json(
            data["scopeSettings"]
        )
    return out
