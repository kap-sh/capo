"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentPostContactSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_post_contact_summary_content
    import capo_connect.types.real_time_contact_analysis_post_contact_summary_failure_code
    import capo_connect.types.real_time_contact_analysis_post_contact_summary_status


class RealTimeContactAnalysisSegmentPostContactSummary(TypedDict, closed=True):
    content: NotRequired[
        "capo_connect.types.real_time_contact_analysis_post_contact_summary_content.RealTimeContactAnalysisPostContactSummaryContent"
    ]
    """<p>The content of the summary.</p>"""
    status: "capo_connect.types.real_time_contact_analysis_post_contact_summary_status.RealTimeContactAnalysisPostContactSummaryStatus"
    """<p>Whether the summary was successfully COMPLETED or FAILED to be generated.</p>"""
    failure_code: NotRequired[
        "capo_connect.types.real_time_contact_analysis_post_contact_summary_failure_code.RealTimeContactAnalysisPostContactSummaryFailureCode"
    ]
    """<p>If the summary failed to be generated, one of the following failure codes occurs:</p> <ul> <li> <p> <code>QUOTA_EXCEEDED</code>: The number of concurrent analytics jobs reached your service quota.</p> </li> <li> <p> <code>INSUFFICIENT_CONVERSATION_CONTENT</code>: The conversation needs to have at least one turn from both the participants in order to generate the summary.</p> </li> <li> <p> <code>FAILED_SAFETY_GUIDELINES</code>: The generated summary cannot be provided because it failed to meet system safety guidelines.</p> </li> <li> <p> <code>INVALID_ANALYSIS_CONFIGURATION</code>: This code occurs when, for example, you're using a <a href="https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#supported-languages-contact-lens">language</a> that isn't supported by generative AI-powered post-contact summaries. </p> </li> <li> <p> <code>INTERNAL_ERROR</code>: Internal system error.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentPostContactSummary) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    import capo_connect.types.real_time_contact_analysis_post_contact_summary_status

    out["Status"] = (
        capo_connect.types.real_time_contact_analysis_post_contact_summary_status.serialize_json(
            value["status"]
        )
    )
    if "failure_code" in value:
        import capo_connect.types.real_time_contact_analysis_post_contact_summary_failure_code

        out["FailureCode"] = (
            capo_connect.types.real_time_contact_analysis_post_contact_summary_failure_code.serialize_json(
                value["failure_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentPostContactSummary:
    out: RealTimeContactAnalysisSegmentPostContactSummary = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Status") is not None:
        import capo_connect.types.real_time_contact_analysis_post_contact_summary_status

        out["status"] = (
            capo_connect.types.real_time_contact_analysis_post_contact_summary_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentPostContactSummary.status required"
        )
    if data.get("FailureCode") is not None:
        import capo_connect.types.real_time_contact_analysis_post_contact_summary_failure_code

        out["failure_code"] = (
            capo_connect.types.real_time_contact_analysis_post_contact_summary_failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    return out
