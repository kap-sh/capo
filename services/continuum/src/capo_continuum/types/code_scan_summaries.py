"""Generated from Smithy shape ``com.amazonaws.continuum#CodeScanSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.code_scan_summary

CodeScanSummaries: TypeAlias = list[
    "capo_continuum.types.code_scan_summary.CodeScanSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeScanSummaries) -> list:
    import capo_continuum.types.code_scan_summary

    out: list = []
    for item in value:
        out.append(capo_continuum.types.code_scan_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeScanSummaries:
    import capo_continuum.types.code_scan_summary

    out: CodeScanSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.code_scan_summary.deserialize_json(item))
    return out
