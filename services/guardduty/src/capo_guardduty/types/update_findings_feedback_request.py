"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateFindingsFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.feedback
    import capo_guardduty.types.finding_ids
    import capo_guardduty.types.sensitive_string


class UpdateFindingsFeedbackRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector that is associated with the findings for which you want to update the feedback.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    finding_ids: NotRequired["capo_guardduty.types.finding_ids.FindingIds"]
    """<p>The IDs of the findings that you want to mark as useful or not useful.</p>"""
    feedback: NotRequired["capo_guardduty.types.feedback.Feedback"]
    """<p>The feedback for the finding.</p>"""
    comments: NotRequired["capo_guardduty.types.sensitive_string.SensitiveString"]
    """<p>Additional feedback about the GuardDuty findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFindingsFeedbackRequest) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import capo_guardduty.types.finding_ids

        out["findingIds"] = capo_guardduty.types.finding_ids.serialize_json(
            value["finding_ids"]
        )
    if "feedback" in value:
        import capo_guardduty.types.feedback

        out["feedback"] = capo_guardduty.types.feedback.serialize_json(
            value["feedback"]
        )
    if "comments" in value:
        out["comments"] = value["comments"]
    return out


def deserialize_json(data: dict) -> UpdateFindingsFeedbackRequest:
    out: UpdateFindingsFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingIds") is not None:
        import capo_guardduty.types.finding_ids

        out["finding_ids"] = capo_guardduty.types.finding_ids.deserialize_json(
            data["findingIds"]
        )
    if data.get("feedback") is not None:
        import capo_guardduty.types.feedback

        out["feedback"] = capo_guardduty.types.feedback.deserialize_json(
            data["feedback"]
        )
    if data.get("comments") is not None:
        out["comments"] = data["comments"]
    return out
