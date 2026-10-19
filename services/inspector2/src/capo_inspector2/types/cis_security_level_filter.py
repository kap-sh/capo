"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevelFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_security_level
    import capo_inspector2.types.cis_security_level_comparison


class CisSecurityLevelFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.cis_security_level_comparison.CisSecurityLevelComparison"
    )
    """<p>The CIS security filter comparison value.</p>"""
    value: "capo_inspector2.types.cis_security_level.CisSecurityLevel"
    """<p>The CIS security filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisSecurityLevelFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_security_level_comparison

    out["comparison"] = (
        capo_inspector2.types.cis_security_level_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_inspector2.types.cis_security_level

    out["value"] = capo_inspector2.types.cis_security_level.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisSecurityLevelFilter:
    out: CisSecurityLevelFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.cis_security_level_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_security_level_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.cis_security_level_comparison.CisSecurityLevelComparison",
            "",
        )
    if data.get("value") is not None:
        import capo_inspector2.types.cis_security_level

        out["value"] = capo_inspector2.types.cis_security_level.deserialize_json(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_inspector2.types.cis_security_level.CisSecurityLevel", ""
        )
    return out
