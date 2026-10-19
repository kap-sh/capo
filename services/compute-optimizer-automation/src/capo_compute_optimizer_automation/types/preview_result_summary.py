"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResultSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.rule_preview_total


class PreviewResultSummary(TypedDict, closed=True):
    key: "str"
    """<p>The key identifier for this preview result summary.</p>"""
    total: "capo_compute_optimizer_automation.types.rule_preview_total.RulePreviewTotal"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResultSummary) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_compute_optimizer_automation.types.rule_preview_total

    out["total"] = (
        capo_compute_optimizer_automation.types.rule_preview_total.serialize_aws_json_1_0(
            value["total"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PreviewResultSummary:
    out: PreviewResultSummary = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("total") is not None:
        import capo_compute_optimizer_automation.types.rule_preview_total

        out["total"] = (
            capo_compute_optimizer_automation.types.rule_preview_total.deserialize_aws_json_1_0(
                data["total"]
            )
        )
    else:
        raise DeserializationError("PreviewResultSummary.total required")
    return out
