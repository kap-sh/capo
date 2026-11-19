"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_inheritance_drift
    import capo_controltower.types.enabled_baseline_source_drift


class EnabledBaselineDriftTypes(TypedDict, closed=True):
    inheritance: NotRequired[
        "capo_controltower.types.enabled_baseline_inheritance_drift.EnabledBaselineInheritanceDrift"
    ]
    """<p>At least one account within the target OU does not match the baseline configuration defined on that OU. An account is in inheritance drift when it does not match the configuration of a parent OU, possibly a new parent OU, if the account is moved. </p>"""
    source: NotRequired[
        "capo_controltower.types.enabled_baseline_source_drift.EnabledBaselineSourceDrift"
    ]
    """<p>Source drift occurs when an enabled baseline no longer matches the landing zone's configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDriftTypes) -> dict:
    out: dict = {}
    if "inheritance" in value:
        import capo_controltower.types.enabled_baseline_inheritance_drift

        out["inheritance"] = (
            capo_controltower.types.enabled_baseline_inheritance_drift.serialize_json(
                value["inheritance"]
            )
        )
    if "source" in value:
        import capo_controltower.types.enabled_baseline_source_drift

        out["source"] = (
            capo_controltower.types.enabled_baseline_source_drift.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineDriftTypes:
    out: EnabledBaselineDriftTypes = {}  # type: ignore[typeddict-item]
    if data.get("inheritance") is not None:
        import capo_controltower.types.enabled_baseline_inheritance_drift

        out["inheritance"] = (
            capo_controltower.types.enabled_baseline_inheritance_drift.deserialize_json(
                data["inheritance"]
            )
        )
    if data.get("source") is not None:
        import capo_controltower.types.enabled_baseline_source_drift

        out["source"] = (
            capo_controltower.types.enabled_baseline_source_drift.deserialize_json(
                data["source"]
            )
        )
    return out
