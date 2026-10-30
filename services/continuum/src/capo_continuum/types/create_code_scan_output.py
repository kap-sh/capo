"""Generated from Smithy shape ``com.amazonaws.continuum#CreateCodeScanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_continuum.types.code_scan_summary


class CreateCodeScanOutput(TypedDict, closed=True):
    scan: "capo_continuum.types.code_scan_summary.CodeScanSummary"
    """The scan run this request created, or the scan run a previous request with the same clientToken already accepted."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeScanOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.code_scan_summary

    out["scan"] = capo_continuum.types.code_scan_summary.serialize_json(value["scan"])
    return out


def deserialize_json(data: dict) -> CreateCodeScanOutput:
    out: CreateCodeScanOutput = {}  # type: ignore[typeddict-item]
    if data.get("scan") is not None:
        import capo_continuum.types.code_scan_summary

        out["scan"] = capo_continuum.types.code_scan_summary.deserialize_json(
            data["scan"]
        )
    else:
        raise DeserializationError("CreateCodeScanOutput.scan required")
    return out
