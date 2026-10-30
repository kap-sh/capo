"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiConfigurationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_configuration_status
    import capo_inspector2.types.ami_scan_duration
    import capo_inspector2.types.ami_scan_mode_configuration
    import capo_inspector2.types.date_time_timestamp


class AmiConfigurationState(TypedDict, closed=True):
    last_launched_within: NotRequired[
        "capo_inspector2.types.ami_scan_duration.AmiScanDuration"
    ]
    """<p>Restricts scanning to AMIs that were last launched within the specified duration.</p>"""
    created_within: NotRequired[
        "capo_inspector2.types.ami_scan_duration.AmiScanDuration"
    ]
    """<p>Restricts scanning to AMIs that were created within the specified duration.</p>"""
    scan_mode_configuration: NotRequired[
        "capo_inspector2.types.ami_scan_mode_configuration.AmiScanModeConfiguration"
    ]
    """<p>The scan mode configuration that determines which AMIs are scanned.</p>"""
    status: NotRequired[
        "capo_inspector2.types.ami_configuration_status.AmiConfigurationStatus"
    ]
    """<p>The status of the AMI scan configuration.</p>"""
    updated_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time when the AMI scan configuration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiConfigurationState) -> dict:
    out: dict = {}
    if "last_launched_within" in value:
        out["lastLaunchedWithin"] = value["last_launched_within"]
    if "created_within" in value:
        out["createdWithin"] = value["created_within"]
    if "scan_mode_configuration" in value:
        import capo_inspector2.types.ami_scan_mode_configuration

        out["scanModeConfiguration"] = (
            capo_inspector2.types.ami_scan_mode_configuration.serialize_json(
                value["scan_mode_configuration"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "updated_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["updatedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> AmiConfigurationState:
    out: AmiConfigurationState = {}  # type: ignore[typeddict-item]
    if data.get("lastLaunchedWithin") is not None:
        out["last_launched_within"] = data["lastLaunchedWithin"]
    if data.get("createdWithin") is not None:
        out["created_within"] = data["createdWithin"]
    if data.get("scanModeConfiguration") is not None:
        import capo_inspector2.types.ami_scan_mode_configuration

        out["scan_mode_configuration"] = (
            capo_inspector2.types.ami_scan_mode_configuration.deserialize_json(
                data["scanModeConfiguration"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("updatedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["updated_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
