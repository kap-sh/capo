"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.continuous_integration_scan_configuration
    import capo_inspector2.types.periodic_scan_configuration
    import capo_inspector2.types.rule_set_categories


class CodeSecurityScanConfiguration(TypedDict, closed=True):
    periodic_scan_configuration: NotRequired[
        "capo_inspector2.types.periodic_scan_configuration.PeriodicScanConfiguration"
    ]
    """<p>Configuration settings for periodic scans that run on a scheduled basis.</p>"""
    continuous_integration_scan_configuration: NotRequired[
        "capo_inspector2.types.continuous_integration_scan_configuration.ContinuousIntegrationScanConfiguration"
    ]
    """<p>Configuration settings for continuous integration scans that run automatically when code changes are made.</p>"""
    rule_set_categories: "capo_inspector2.types.rule_set_categories.RuleSetCategories"
    """<p>The categories of security rules to be applied during the scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityScanConfiguration) -> dict:
    out: dict = {}
    if "periodic_scan_configuration" in value:
        import capo_inspector2.types.periodic_scan_configuration

        out["periodicScanConfiguration"] = (
            capo_inspector2.types.periodic_scan_configuration.serialize_json(
                value["periodic_scan_configuration"]
            )
        )
    if "continuous_integration_scan_configuration" in value:
        import capo_inspector2.types.continuous_integration_scan_configuration

        out["continuousIntegrationScanConfiguration"] = (
            capo_inspector2.types.continuous_integration_scan_configuration.serialize_json(
                value["continuous_integration_scan_configuration"]
            )
        )
    import capo_inspector2.types.rule_set_categories

    out["ruleSetCategories"] = capo_inspector2.types.rule_set_categories.serialize_json(
        value["rule_set_categories"]
    )
    return out


def deserialize_json(data: dict) -> CodeSecurityScanConfiguration:
    out: CodeSecurityScanConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("periodicScanConfiguration") is not None:
        import capo_inspector2.types.periodic_scan_configuration

        out["periodic_scan_configuration"] = (
            capo_inspector2.types.periodic_scan_configuration.deserialize_json(
                data["periodicScanConfiguration"]
            )
        )
    if data.get("continuousIntegrationScanConfiguration") is not None:
        import capo_inspector2.types.continuous_integration_scan_configuration

        out["continuous_integration_scan_configuration"] = (
            capo_inspector2.types.continuous_integration_scan_configuration.deserialize_json(
                data["continuousIntegrationScanConfiguration"]
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
    return out
