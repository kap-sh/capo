"""Generated from Smithy shape ``com.amazonaws.continuum#ListCodeScansOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.code_scan_summaries
    import capo_continuum.types.next_token


class ListCodeScansOutput(TypedDict, closed=True):
    scans: "capo_continuum.types.code_scan_summaries.CodeScanSummaries"
    """Customer-visible scans ordered by scanRunId descending."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """Pagination token for the next page, if present."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeScansOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.code_scan_summaries

    out["scans"] = capo_continuum.types.code_scan_summaries.serialize_json(
        value["scans"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeScansOutput:
    out: ListCodeScansOutput = {}  # type: ignore[typeddict-item]
    if data.get("scans") is not None:
        import capo_continuum.types.code_scan_summaries

        out["scans"] = capo_continuum.types.code_scan_summaries.deserialize_json(
            data["scans"]
        )
    else:
        out["scans"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
