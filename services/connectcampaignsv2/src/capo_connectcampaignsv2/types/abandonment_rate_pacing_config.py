"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#AbandonmentRatePacingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.connection_start_point
    import capo_connectcampaignsv2.types.evaluation_window
    import capo_connectcampaignsv2.types.target_rate


class AbandonmentRatePacingConfig(TypedDict, closed=True):
    target_rate: "capo_connectcampaignsv2.types.target_rate.TargetRate"
    connection_start_point: (
        "capo_connectcampaignsv2.types.connection_start_point.ConnectionStartPoint"
    )
    """Event from which connectionThresholdSeconds is measured."""
    connection_threshold_seconds: "int"
    """Seconds after connectionStartPoint before a contact counts as abandoned."""
    evaluation_window: (
        "capo_connectcampaignsv2.types.evaluation_window.EvaluationWindow"
    )
    """Rolling window over which abandonmentRate is computed."""


# --- restJson1 ser/de ---
def serialize_json(value: AbandonmentRatePacingConfig) -> dict:
    out: dict = {}
    out["targetRate"] = (
        "NaN"
        if value["target_rate"] != value["target_rate"]
        else "Infinity"
        if value["target_rate"] == float("inf")
        else "-Infinity"
        if value["target_rate"] == float("-inf")
        else value["target_rate"]
    )
    out["connectionStartPoint"] = value["connection_start_point"]
    out["connectionThresholdSeconds"] = value["connection_threshold_seconds"]
    out["evaluationWindow"] = value["evaluation_window"]
    return out


def deserialize_json(data: dict) -> AbandonmentRatePacingConfig:
    out: AbandonmentRatePacingConfig = {}  # type: ignore[typeddict-item]
    if data.get("targetRate") is not None:
        out["target_rate"] = float(data["targetRate"])
    else:
        out["target_rate"] = 0.0
    if data.get("connectionStartPoint") is not None:
        out["connection_start_point"] = data["connectionStartPoint"]
    else:
        out["connection_start_point"] = ""
    if data.get("connectionThresholdSeconds") is not None:
        out["connection_threshold_seconds"] = data["connectionThresholdSeconds"]
    else:
        out["connection_threshold_seconds"] = 0
    if data.get("evaluationWindow") is not None:
        out["evaluation_window"] = data["evaluationWindow"]
    else:
        out["evaluation_window"] = ""
    return out
