"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalReview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_review_reason
    import capo_connecthealth.types.periodontal_site_name_list
    import capo_connecthealth.types.periodontal_tooth_number


class PeriodontalReview(TypedDict, closed=True):
    reason: "capo_connecthealth.types.periodontal_review_reason.PeriodontalReviewReason"
    """<p>The reason for review. The following values are valid:</p> <ul> <li> <p> <code>SITE_NOT_CHARTED</code>: One or more sites have no reading.</p> </li> <li> <p> <code>VALUE_NOT_CHARTED</code>: A dictated value or charting instruction was not charted, for example because the value was out of range or not valid at its position.</p> </li> <li> <p> <code>READING_COUNT_MISMATCH</code>: The number of dictated values did not match the number of open sites. The values were charted as dictated.</p> </li> <li> <p> <code>LINE_UNCLEAR</code>: A line of dictation could not be interpreted and was not charted.</p> </li> <li> <p> <code>TOOTH_UNCLEAR</code>: A line of dictation did not identify the tooth and was not charted.</p> </li> <li> <p> <code>MISSING_TOOTH_CONFLICT</code>: The dictation conflicts with a tooth marked as missing.</p> </li> <li> <p> <code>MEASUREMENT_NOT_CHARTED</code>: The dictation included a measurement that the chart does not record, such as plaque, calculus, or the mucogingival junction.</p> </li> <li> <p> <code>SESSION_ISSUE</code>: The exam setup could not be used and all teeth were assumed to be present, or the earlier chart could not be restored and charting restarted.</p> </li> </ul>"""
    tooth_number: NotRequired[
        "capo_connecthealth.types.periodontal_tooth_number.PeriodontalToothNumber"
    ]
    """<p>The tooth that the item refers to.</p>"""
    sites: NotRequired[
        "capo_connecthealth.types.periodontal_site_name_list.PeriodontalSiteNameList"
    ]
    """<p>The probing sites of that tooth that the item refers to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalReview) -> dict:
    out: dict = {}
    import capo_connecthealth.types.periodontal_review_reason

    out["reason"] = capo_connecthealth.types.periodontal_review_reason.serialize_json(
        value["reason"]
    )
    if "tooth_number" in value:
        out["toothNumber"] = value["tooth_number"]
    if "sites" in value:
        import capo_connecthealth.types.periodontal_site_name_list

        out["sites"] = (
            capo_connecthealth.types.periodontal_site_name_list.serialize_json(
                value["sites"]
            )
        )
    return out


def deserialize_json(data: dict) -> PeriodontalReview:
    out: PeriodontalReview = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        import capo_connecthealth.types.periodontal_review_reason

        out["reason"] = (
            capo_connecthealth.types.periodontal_review_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_connecthealth.types.periodontal_review_reason.PeriodontalReviewReason",
            "",
        )
    if data.get("toothNumber") is not None:
        out["tooth_number"] = data["toothNumber"]
    if data.get("sites") is not None:
        import capo_connecthealth.types.periodontal_site_name_list

        out["sites"] = (
            capo_connecthealth.types.periodontal_site_name_list.deserialize_json(
                data["sites"]
            )
        )
    return out
