"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ecr_pull_date_rescan_duration
    import capo_inspector2.types.ecr_pull_date_rescan_mode
    import capo_inspector2.types.ecr_rescan_duration


class EcrConfiguration(TypedDict, closed=True):
    rescan_duration: "capo_inspector2.types.ecr_rescan_duration.EcrRescanDuration"
    """<p>The rescan duration configured for image push date.</p>"""
    pull_date_rescan_duration: NotRequired[
        "capo_inspector2.types.ecr_pull_date_rescan_duration.EcrPullDateRescanDuration"
    ]
    """<p>The rescan duration configured for image pull date.</p>"""
    pull_date_rescan_mode: NotRequired[
        "capo_inspector2.types.ecr_pull_date_rescan_mode.EcrPullDateRescanMode"
    ]
    """<p>The pull date for the re-scan mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrConfiguration) -> dict:
    out: dict = {}
    out["rescanDuration"] = value["rescan_duration"]
    if "pull_date_rescan_duration" in value:
        out["pullDateRescanDuration"] = value["pull_date_rescan_duration"]
    if "pull_date_rescan_mode" in value:
        out["pullDateRescanMode"] = value["pull_date_rescan_mode"]
    return out


def deserialize_json(data: dict) -> EcrConfiguration:
    out: EcrConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("rescanDuration") is not None:
        out["rescan_duration"] = data["rescanDuration"]
    else:
        out["rescan_duration"] = ""
    if data.get("pullDateRescanDuration") is not None:
        out["pull_date_rescan_duration"] = data["pullDateRescanDuration"]
    if data.get("pullDateRescanMode") is not None:
        out["pull_date_rescan_mode"] = data["pullDateRescanMode"]
    return out
