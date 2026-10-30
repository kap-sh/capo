"""Generated from Smithy shape ``com.amazonaws.continuum#CodeConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.code_scan_summary
    import capo_continuum.types.collector_details
    import capo_continuum.types.environment_configuration
    import capo_continuum.types.environment_source_configuration


class CodeConfigurationDetails(TypedDict, closed=True):
    collector_details: NotRequired[
        "capo_continuum.types.collector_details.CollectorDetails"
    ]
    """Collector data access configuration. Omitted when no Collector data access role is configured."""
    source_configuration: NotRequired[
        "capo_continuum.types.environment_source_configuration.EnvironmentSourceConfiguration"
    ]
    """Sources in the shape accepted by CreateEnvironment and UpdateEnvironment."""
    environment_configuration: NotRequired[
        "capo_continuum.types.environment_configuration.EnvironmentConfiguration"
    ]
    """Operating policy in the shape accepted by CreateEnvironment and UpdateEnvironment."""
    latest_scan: NotRequired["capo_continuum.types.code_scan_summary.CodeScanSummary"]
    """The newest scan requested for this environment, if one exists."""


# --- restJson1 ser/de ---
def serialize_json(value: CodeConfigurationDetails) -> dict:
    out: dict = {}
    if "collector_details" in value:
        import capo_continuum.types.collector_details

        out["collectorDetails"] = capo_continuum.types.collector_details.serialize_json(
            value["collector_details"]
        )
    if "source_configuration" in value:
        import capo_continuum.types.environment_source_configuration

        out["sourceConfiguration"] = (
            capo_continuum.types.environment_source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "environment_configuration" in value:
        import capo_continuum.types.environment_configuration

        out["environmentConfiguration"] = (
            capo_continuum.types.environment_configuration.serialize_json(
                value["environment_configuration"]
            )
        )
    if "latest_scan" in value:
        import capo_continuum.types.code_scan_summary

        out["latestScan"] = capo_continuum.types.code_scan_summary.serialize_json(
            value["latest_scan"]
        )
    return out


def deserialize_json(data: dict) -> CodeConfigurationDetails:
    out: CodeConfigurationDetails = {}  # type: ignore[typeddict-item]
    if data.get("collectorDetails") is not None:
        import capo_continuum.types.collector_details

        out["collector_details"] = (
            capo_continuum.types.collector_details.deserialize_json(
                data["collectorDetails"]
            )
        )
    if data.get("sourceConfiguration") is not None:
        import capo_continuum.types.environment_source_configuration

        out["source_configuration"] = (
            capo_continuum.types.environment_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if data.get("environmentConfiguration") is not None:
        import capo_continuum.types.environment_configuration

        out["environment_configuration"] = (
            capo_continuum.types.environment_configuration.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if data.get("latestScan") is not None:
        import capo_continuum.types.code_scan_summary

        out["latest_scan"] = capo_continuum.types.code_scan_summary.deserialize_json(
            data["latestScan"]
        )
    return out
