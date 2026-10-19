"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusReasonFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_target_status_comparison
    import capo_inspector2.types.cis_target_status_reason


class CisTargetStatusReasonFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.cis_target_status_comparison.CisTargetStatusComparison"
    )
    """<p>The comparison value of the CIS target status reason filter.</p>"""
    value: "capo_inspector2.types.cis_target_status_reason.CisTargetStatusReason"
    """<p>The value of the CIS target status reason filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatusReasonFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_target_status_comparison

    out["comparison"] = (
        capo_inspector2.types.cis_target_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_inspector2.types.cis_target_status_reason

    out["value"] = capo_inspector2.types.cis_target_status_reason.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisTargetStatusReasonFilter:
    out: CisTargetStatusReasonFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.cis_target_status_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_target_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.cis_target_status_comparison.CisTargetStatusComparison",
            "",
        )
    if data.get("value") is not None:
        import capo_inspector2.types.cis_target_status_reason

        out["value"] = capo_inspector2.types.cis_target_status_reason.deserialize_json(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_inspector2.types.cis_target_status_reason.CisTargetStatusReason", ""
        )
    return out
