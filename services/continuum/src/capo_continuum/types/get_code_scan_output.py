"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeScanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_continuum.types.code_scan_data


class GetCodeScanOutput(TypedDict, closed=True):
    scan: "capo_continuum.types.code_scan_data.CodeScanData"
    """Complete customer-visible scan data."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeScanOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.code_scan_data

    out["scan"] = capo_continuum.types.code_scan_data.serialize_json(value["scan"])
    return out


def deserialize_json(data: dict) -> GetCodeScanOutput:
    out: GetCodeScanOutput = {}  # type: ignore[typeddict-item]
    if data.get("scan") is not None:
        import capo_continuum.types.code_scan_data

        out["scan"] = capo_continuum.types.code_scan_data.deserialize_json(data["scan"])
    else:
        raise DeserializationError("GetCodeScanOutput.scan required")
    return out
