"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_status
    import capo_inspector2.types.cis_scan_status_comparison


class CisScanStatusFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.cis_scan_status_comparison.CisScanStatusComparison"
    )
    """<p>The filter comparison value.</p>"""
    value: "capo_inspector2.types.cis_scan_status.CisScanStatus"
    """<p>The filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanStatusFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_scan_status_comparison

    out["comparison"] = capo_inspector2.types.cis_scan_status_comparison.serialize_json(
        value["comparison"]
    )
    import capo_inspector2.types.cis_scan_status

    out["value"] = capo_inspector2.types.cis_scan_status.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> CisScanStatusFilter:
    out: CisScanStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.cis_scan_status_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_scan_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.cis_scan_status_comparison.CisScanStatusComparison",
            "",
        )
    if data.get("value") is not None:
        import capo_inspector2.types.cis_scan_status

        out["value"] = capo_inspector2.types.cis_scan_status.deserialize_json(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_inspector2.types.cis_scan_status.CisScanStatus", ""
        )
    return out
