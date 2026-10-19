"""Generated from Smithy shape ``com.amazonaws.inspector2#ContinuousIntegrationScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.continuous_integration_scan_supported_events


class ContinuousIntegrationScanConfiguration(TypedDict, closed=True):
    supported_events: "capo_inspector2.types.continuous_integration_scan_supported_events.ContinuousIntegrationScanSupportedEvents"
    """<p>The repository events that trigger continuous integration scans, such as pull requests or commits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousIntegrationScanConfiguration) -> dict:
    out: dict = {}
    import capo_inspector2.types.continuous_integration_scan_supported_events

    out["supportedEvents"] = (
        capo_inspector2.types.continuous_integration_scan_supported_events.serialize_json(
            value["supported_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContinuousIntegrationScanConfiguration:
    out: ContinuousIntegrationScanConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("supportedEvents") is not None:
        import capo_inspector2.types.continuous_integration_scan_supported_events

        out["supported_events"] = (
            capo_inspector2.types.continuous_integration_scan_supported_events.deserialize_json(
                data["supportedEvents"]
            )
        )
    else:
        out["supported_events"] = []
    return out
