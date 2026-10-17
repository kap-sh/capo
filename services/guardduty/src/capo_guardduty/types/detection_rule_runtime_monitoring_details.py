"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleRuntimeMonitoringDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_runtime_platforms


class DetectionRuleRuntimeMonitoringDetails(TypedDict, closed=True):
    platforms: NotRequired[
        "capo_guardduty.types.detection_rule_runtime_platforms.DetectionRuleRuntimePlatforms"
    ]
    """<p>The platforms on which the rule can run. The presence of a platform member indicates that the rule is supported on that platform; the absence of a member indicates that the rule cannot run on that platform at any agent version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleRuntimeMonitoringDetails) -> dict:
    out: dict = {}
    if "platforms" in value:
        import capo_guardduty.types.detection_rule_runtime_platforms

        out["platforms"] = (
            capo_guardduty.types.detection_rule_runtime_platforms.serialize_json(
                value["platforms"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectionRuleRuntimeMonitoringDetails:
    out: DetectionRuleRuntimeMonitoringDetails = {}  # type: ignore[typeddict-item]
    if data.get("platforms") is not None:
        import capo_guardduty.types.detection_rule_runtime_platforms

        out["platforms"] = (
            capo_guardduty.types.detection_rule_runtime_platforms.deserialize_json(
                data["platforms"]
            )
        )
    return out
