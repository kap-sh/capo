"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineSourceDrift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_drift_status


class EnabledBaselineSourceDrift(TypedDict, closed=True):
    status: NotRequired[
        "capo_controltower.types.enabled_baseline_drift_status.EnabledBaselineDriftStatus"
    ]
    """<p>The source drift status for the enabled baseline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineSourceDrift) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_controltower.types.enabled_baseline_drift_status

        out["status"] = (
            capo_controltower.types.enabled_baseline_drift_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineSourceDrift:
    out: EnabledBaselineSourceDrift = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_controltower.types.enabled_baseline_drift_status

        out["status"] = (
            capo_controltower.types.enabled_baseline_drift_status.deserialize_json(
                data["status"]
            )
        )
    return out
