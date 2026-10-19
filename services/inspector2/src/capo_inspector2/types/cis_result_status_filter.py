"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_result_status
    import capo_inspector2.types.cis_result_status_comparison


class CisResultStatusFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.cis_result_status_comparison.CisResultStatusComparison"
    )
    """<p>The comparison value of the CIS result status filter.</p>"""
    value: "capo_inspector2.types.cis_result_status.CisResultStatus"
    """<p>The value of the CIS result status filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisResultStatusFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_result_status_comparison

    out["comparison"] = (
        capo_inspector2.types.cis_result_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_inspector2.types.cis_result_status

    out["value"] = capo_inspector2.types.cis_result_status.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisResultStatusFilter:
    out: CisResultStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.cis_result_status_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_result_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.cis_result_status_comparison.CisResultStatusComparison",
            "",
        )
    if data.get("value") is not None:
        import capo_inspector2.types.cis_result_status

        out["value"] = capo_inspector2.types.cis_result_status.deserialize_json(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_inspector2.types.cis_result_status.CisResultStatus", ""
        )
    return out
