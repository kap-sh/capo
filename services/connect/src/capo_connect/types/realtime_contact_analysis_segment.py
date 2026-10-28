"""Generated from Smithy shape ``com.amazonaws.connect#RealtimeContactAnalysisSegment``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_segment_attachments
    import capo_connect.types.real_time_contact_analysis_segment_categories
    import capo_connect.types.real_time_contact_analysis_segment_event
    import capo_connect.types.real_time_contact_analysis_segment_extracted_information
    import capo_connect.types.real_time_contact_analysis_segment_issues
    import capo_connect.types.real_time_contact_analysis_segment_post_contact_summary
    import capo_connect.types.real_time_contact_analysis_segment_transcript


class RealtimeContactAnalysisSegmentTranscriptMember(TypedDict, closed=True):
    Transcript: "capo_connect.types.real_time_contact_analysis_segment_transcript.RealTimeContactAnalysisSegmentTranscript"


class RealtimeContactAnalysisSegmentCategoriesMember(TypedDict, closed=True):
    Categories: "capo_connect.types.real_time_contact_analysis_segment_categories.RealTimeContactAnalysisSegmentCategories"


class RealtimeContactAnalysisSegmentIssuesMember(TypedDict, closed=True):
    Issues: "capo_connect.types.real_time_contact_analysis_segment_issues.RealTimeContactAnalysisSegmentIssues"


class RealtimeContactAnalysisSegmentEventMember(TypedDict, closed=True):
    Event: "capo_connect.types.real_time_contact_analysis_segment_event.RealTimeContactAnalysisSegmentEvent"


class RealtimeContactAnalysisSegmentAttachmentsMember(TypedDict, closed=True):
    Attachments: "capo_connect.types.real_time_contact_analysis_segment_attachments.RealTimeContactAnalysisSegmentAttachments"


class RealtimeContactAnalysisSegmentPostContactSummaryMember(TypedDict, closed=True):
    PostContactSummary: "capo_connect.types.real_time_contact_analysis_segment_post_contact_summary.RealTimeContactAnalysisSegmentPostContactSummary"


class RealtimeContactAnalysisSegmentExtractedInformationMember(TypedDict, closed=True):
    ExtractedInformation: "capo_connect.types.real_time_contact_analysis_segment_extracted_information.RealTimeContactAnalysisSegmentExtractedInformation"


RealtimeContactAnalysisSegment: TypeAlias = (
    RealtimeContactAnalysisSegmentTranscriptMember
    | RealtimeContactAnalysisSegmentCategoriesMember
    | RealtimeContactAnalysisSegmentIssuesMember
    | RealtimeContactAnalysisSegmentEventMember
    | RealtimeContactAnalysisSegmentAttachmentsMember
    | RealtimeContactAnalysisSegmentPostContactSummaryMember
    | RealtimeContactAnalysisSegmentExtractedInformationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RealtimeContactAnalysisSegment) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RealtimeContactAnalysisSegment: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Transcript" in value:
        import capo_connect.types.real_time_contact_analysis_segment_transcript

        return {
            "Transcript": capo_connect.types.real_time_contact_analysis_segment_transcript.serialize_json(
                value["Transcript"]
            )
        }
    elif "Categories" in value:
        import capo_connect.types.real_time_contact_analysis_segment_categories

        return {
            "Categories": capo_connect.types.real_time_contact_analysis_segment_categories.serialize_json(
                value["Categories"]
            )
        }
    elif "Issues" in value:
        import capo_connect.types.real_time_contact_analysis_segment_issues

        return {
            "Issues": capo_connect.types.real_time_contact_analysis_segment_issues.serialize_json(
                value["Issues"]
            )
        }
    elif "Event" in value:
        import capo_connect.types.real_time_contact_analysis_segment_event

        return {
            "Event": capo_connect.types.real_time_contact_analysis_segment_event.serialize_json(
                value["Event"]
            )
        }
    elif "Attachments" in value:
        import capo_connect.types.real_time_contact_analysis_segment_attachments

        return {
            "Attachments": capo_connect.types.real_time_contact_analysis_segment_attachments.serialize_json(
                value["Attachments"]
            )
        }
    elif "PostContactSummary" in value:
        import capo_connect.types.real_time_contact_analysis_segment_post_contact_summary

        return {
            "PostContactSummary": capo_connect.types.real_time_contact_analysis_segment_post_contact_summary.serialize_json(
                value["PostContactSummary"]
            )
        }
    elif "ExtractedInformation" in value:
        import capo_connect.types.real_time_contact_analysis_segment_extracted_information

        return {
            "ExtractedInformation": capo_connect.types.real_time_contact_analysis_segment_extracted_information.serialize_json(
                value["ExtractedInformation"]
            )
        }
    else:
        raise SerializationError("RealtimeContactAnalysisSegment: no variant present")


def deserialize_json(data: dict) -> RealtimeContactAnalysisSegment:
    if data.get("Transcript") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_transcript

        return {
            "Transcript": capo_connect.types.real_time_contact_analysis_segment_transcript.deserialize_json(
                data["Transcript"]
            )
        }
    elif data.get("Categories") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_categories

        return {
            "Categories": capo_connect.types.real_time_contact_analysis_segment_categories.deserialize_json(
                data["Categories"]
            )
        }
    elif data.get("Issues") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_issues

        return {
            "Issues": capo_connect.types.real_time_contact_analysis_segment_issues.deserialize_json(
                data["Issues"]
            )
        }
    elif data.get("Event") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_event

        return {
            "Event": capo_connect.types.real_time_contact_analysis_segment_event.deserialize_json(
                data["Event"]
            )
        }
    elif data.get("Attachments") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_attachments

        return {
            "Attachments": capo_connect.types.real_time_contact_analysis_segment_attachments.deserialize_json(
                data["Attachments"]
            )
        }
    elif data.get("PostContactSummary") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_post_contact_summary

        return {
            "PostContactSummary": capo_connect.types.real_time_contact_analysis_segment_post_contact_summary.deserialize_json(
                data["PostContactSummary"]
            )
        }
    elif data.get("ExtractedInformation") is not None:
        import capo_connect.types.real_time_contact_analysis_segment_extracted_information

        return {
            "ExtractedInformation": capo_connect.types.real_time_contact_analysis_segment_extracted_information.deserialize_json(
                data["ExtractedInformation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RealtimeContactAnalysisSegment: no recognized variant key"
        )
