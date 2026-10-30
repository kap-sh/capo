"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeScanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.scan_run_id


class GetCodeScanInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """Environment that owns the scan."""
    scan_run_id: "capo_continuum.types.scan_run_id.ScanRunId"
    """Scan to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeScanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeScanInput:
    out: GetCodeScanInput = {}  # type: ignore[typeddict-item]
    return out
