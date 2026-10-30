"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.ami_scan_duration
    import capo_inspector2.types.ami_scan_mode_configuration


class AmiConfiguration(TypedDict, closed=True):
    last_launched_within: NotRequired[
        "capo_inspector2.types.ami_scan_duration.AmiScanDuration"
    ]
    """<p>Restricts scanning to AMIs that were last launched within the specified duration.</p>"""
    created_within: NotRequired[
        "capo_inspector2.types.ami_scan_duration.AmiScanDuration"
    ]
    """<p>Restricts scanning to AMIs that were created within the specified duration.</p>"""
    scan_mode_configuration: (
        "capo_inspector2.types.ami_scan_mode_configuration.AmiScanModeConfiguration"
    )
    """<p>The scan mode configuration that determines which AMIs are scanned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiConfiguration) -> dict:
    out: dict = {}
    if "last_launched_within" in value:
        out["lastLaunchedWithin"] = value["last_launched_within"]
    if "created_within" in value:
        out["createdWithin"] = value["created_within"]
    import capo_inspector2.types.ami_scan_mode_configuration

    out["scanModeConfiguration"] = (
        capo_inspector2.types.ami_scan_mode_configuration.serialize_json(
            value["scan_mode_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> AmiConfiguration:
    out: AmiConfiguration = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError("AmiConfiguration.scan_mode_configuration required")
    return out
