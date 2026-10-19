"""Generated from Smithy shape ``com.amazonaws.inspector2#CisStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_string_comparison


class CisStringFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.cis_string_comparison.CisStringComparison"
    """<p>The comparison value of the CIS string filter.</p>"""
    value: "str"
    """<p>The value of the CIS string filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisStringFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_string_comparison

    out["comparison"] = capo_inspector2.types.cis_string_comparison.serialize_json(
        value["comparison"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CisStringFilter:
    out: CisStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.cis_string_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_string_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.cis_string_comparison.CisStringComparison", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
