"""Generated from Smithy shape ``com.amazonaws.qconnect#DataDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.case_summarization_chunk_data_details
    import capo_qconnect.types.content_data_details
    import capo_qconnect.types.email_generative_answer_chunk_data_details
    import capo_qconnect.types.email_overview_chunk_data_details
    import capo_qconnect.types.email_response_chunk_data_details
    import capo_qconnect.types.generative_chunk_data_details
    import capo_qconnect.types.generative_data_details
    import capo_qconnect.types.intent_detected_data_details
    import capo_qconnect.types.notes_chunk_data_details
    import capo_qconnect.types.notes_data_details
    import capo_qconnect.types.proactive_recommendation_data_details
    import capo_qconnect.types.source_content_data_details
    import capo_qconnect.types.suggested_message_data_details


class DataDetailsContentDataMember(TypedDict, closed=True):
    contentData: "capo_qconnect.types.content_data_details.ContentDataDetails"


class DataDetailsGenerativeDataMember(TypedDict, closed=True):
    generativeData: "capo_qconnect.types.generative_data_details.GenerativeDataDetails"


class DataDetailsIntentDetectedDataMember(TypedDict, closed=True):
    intentDetectedData: (
        "capo_qconnect.types.intent_detected_data_details.IntentDetectedDataDetails"
    )


class DataDetailsSourceContentDataMember(TypedDict, closed=True):
    sourceContentData: (
        "capo_qconnect.types.source_content_data_details.SourceContentDataDetails"
    )


class DataDetailsGenerativeChunkDataMember(TypedDict, closed=True):
    generativeChunkData: (
        "capo_qconnect.types.generative_chunk_data_details.GenerativeChunkDataDetails"
    )


class DataDetailsEmailResponseChunkDataMember(TypedDict, closed=True):
    emailResponseChunkData: "capo_qconnect.types.email_response_chunk_data_details.EmailResponseChunkDataDetails"


class DataDetailsEmailOverviewChunkDataMember(TypedDict, closed=True):
    emailOverviewChunkData: "capo_qconnect.types.email_overview_chunk_data_details.EmailOverviewChunkDataDetails"


class DataDetailsEmailGenerativeAnswerChunkDataMember(TypedDict, closed=True):
    emailGenerativeAnswerChunkData: "capo_qconnect.types.email_generative_answer_chunk_data_details.EmailGenerativeAnswerChunkDataDetails"


class DataDetailsCaseSummarizationChunkDataMember(TypedDict, closed=True):
    caseSummarizationChunkData: "capo_qconnect.types.case_summarization_chunk_data_details.CaseSummarizationChunkDataDetails"


class DataDetailsSuggestedMessageDataMember(TypedDict, closed=True):
    suggestedMessageData: (
        "capo_qconnect.types.suggested_message_data_details.SuggestedMessageDataDetails"
    )


class DataDetailsNotesDataMember(TypedDict, closed=True):
    notesData: "capo_qconnect.types.notes_data_details.NotesDataDetails"


class DataDetailsNotesChunkDataMember(TypedDict, closed=True):
    notesChunkData: "capo_qconnect.types.notes_chunk_data_details.NotesChunkDataDetails"


class DataDetailsProactiveRecommendationDataMember(TypedDict, closed=True):
    proactiveRecommendationData: "capo_qconnect.types.proactive_recommendation_data_details.ProactiveRecommendationDataDetails"


DataDetails: TypeAlias = (
    DataDetailsContentDataMember
    | DataDetailsGenerativeDataMember
    | DataDetailsIntentDetectedDataMember
    | DataDetailsSourceContentDataMember
    | DataDetailsGenerativeChunkDataMember
    | DataDetailsEmailResponseChunkDataMember
    | DataDetailsEmailOverviewChunkDataMember
    | DataDetailsEmailGenerativeAnswerChunkDataMember
    | DataDetailsCaseSummarizationChunkDataMember
    | DataDetailsSuggestedMessageDataMember
    | DataDetailsNotesDataMember
    | DataDetailsNotesChunkDataMember
    | DataDetailsProactiveRecommendationDataMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DataDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "contentData" in value:
        import capo_qconnect.types.content_data_details

        return {
            "contentData": capo_qconnect.types.content_data_details.serialize_json(
                value["contentData"]
            )
        }
    elif "generativeData" in value:
        import capo_qconnect.types.generative_data_details

        return {
            "generativeData": capo_qconnect.types.generative_data_details.serialize_json(
                value["generativeData"]
            )
        }
    elif "intentDetectedData" in value:
        import capo_qconnect.types.intent_detected_data_details

        return {
            "intentDetectedData": capo_qconnect.types.intent_detected_data_details.serialize_json(
                value["intentDetectedData"]
            )
        }
    elif "sourceContentData" in value:
        import capo_qconnect.types.source_content_data_details

        return {
            "sourceContentData": capo_qconnect.types.source_content_data_details.serialize_json(
                value["sourceContentData"]
            )
        }
    elif "generativeChunkData" in value:
        import capo_qconnect.types.generative_chunk_data_details

        return {
            "generativeChunkData": capo_qconnect.types.generative_chunk_data_details.serialize_json(
                value["generativeChunkData"]
            )
        }
    elif "emailResponseChunkData" in value:
        import capo_qconnect.types.email_response_chunk_data_details

        return {
            "emailResponseChunkData": capo_qconnect.types.email_response_chunk_data_details.serialize_json(
                value["emailResponseChunkData"]
            )
        }
    elif "emailOverviewChunkData" in value:
        import capo_qconnect.types.email_overview_chunk_data_details

        return {
            "emailOverviewChunkData": capo_qconnect.types.email_overview_chunk_data_details.serialize_json(
                value["emailOverviewChunkData"]
            )
        }
    elif "emailGenerativeAnswerChunkData" in value:
        import capo_qconnect.types.email_generative_answer_chunk_data_details

        return {
            "emailGenerativeAnswerChunkData": capo_qconnect.types.email_generative_answer_chunk_data_details.serialize_json(
                value["emailGenerativeAnswerChunkData"]
            )
        }
    elif "caseSummarizationChunkData" in value:
        import capo_qconnect.types.case_summarization_chunk_data_details

        return {
            "caseSummarizationChunkData": capo_qconnect.types.case_summarization_chunk_data_details.serialize_json(
                value["caseSummarizationChunkData"]
            )
        }
    elif "suggestedMessageData" in value:
        import capo_qconnect.types.suggested_message_data_details

        return {
            "suggestedMessageData": capo_qconnect.types.suggested_message_data_details.serialize_json(
                value["suggestedMessageData"]
            )
        }
    elif "notesData" in value:
        import capo_qconnect.types.notes_data_details

        return {
            "notesData": capo_qconnect.types.notes_data_details.serialize_json(
                value["notesData"]
            )
        }
    elif "notesChunkData" in value:
        import capo_qconnect.types.notes_chunk_data_details

        return {
            "notesChunkData": capo_qconnect.types.notes_chunk_data_details.serialize_json(
                value["notesChunkData"]
            )
        }
    elif "proactiveRecommendationData" in value:
        import capo_qconnect.types.proactive_recommendation_data_details

        return {
            "proactiveRecommendationData": capo_qconnect.types.proactive_recommendation_data_details.serialize_json(
                value["proactiveRecommendationData"]
            )
        }
    else:
        raise SerializationError("DataDetails: no variant present")


def deserialize_json(data: dict) -> DataDetails:
    if data.get("contentData") is not None:
        import capo_qconnect.types.content_data_details

        return {
            "contentData": capo_qconnect.types.content_data_details.deserialize_json(
                data["contentData"]
            )
        }
    elif data.get("generativeData") is not None:
        import capo_qconnect.types.generative_data_details

        return {
            "generativeData": capo_qconnect.types.generative_data_details.deserialize_json(
                data["generativeData"]
            )
        }
    elif data.get("intentDetectedData") is not None:
        import capo_qconnect.types.intent_detected_data_details

        return {
            "intentDetectedData": capo_qconnect.types.intent_detected_data_details.deserialize_json(
                data["intentDetectedData"]
            )
        }
    elif data.get("sourceContentData") is not None:
        import capo_qconnect.types.source_content_data_details

        return {
            "sourceContentData": capo_qconnect.types.source_content_data_details.deserialize_json(
                data["sourceContentData"]
            )
        }
    elif data.get("generativeChunkData") is not None:
        import capo_qconnect.types.generative_chunk_data_details

        return {
            "generativeChunkData": capo_qconnect.types.generative_chunk_data_details.deserialize_json(
                data["generativeChunkData"]
            )
        }
    elif data.get("emailResponseChunkData") is not None:
        import capo_qconnect.types.email_response_chunk_data_details

        return {
            "emailResponseChunkData": capo_qconnect.types.email_response_chunk_data_details.deserialize_json(
                data["emailResponseChunkData"]
            )
        }
    elif data.get("emailOverviewChunkData") is not None:
        import capo_qconnect.types.email_overview_chunk_data_details

        return {
            "emailOverviewChunkData": capo_qconnect.types.email_overview_chunk_data_details.deserialize_json(
                data["emailOverviewChunkData"]
            )
        }
    elif data.get("emailGenerativeAnswerChunkData") is not None:
        import capo_qconnect.types.email_generative_answer_chunk_data_details

        return {
            "emailGenerativeAnswerChunkData": capo_qconnect.types.email_generative_answer_chunk_data_details.deserialize_json(
                data["emailGenerativeAnswerChunkData"]
            )
        }
    elif data.get("caseSummarizationChunkData") is not None:
        import capo_qconnect.types.case_summarization_chunk_data_details

        return {
            "caseSummarizationChunkData": capo_qconnect.types.case_summarization_chunk_data_details.deserialize_json(
                data["caseSummarizationChunkData"]
            )
        }
    elif data.get("suggestedMessageData") is not None:
        import capo_qconnect.types.suggested_message_data_details

        return {
            "suggestedMessageData": capo_qconnect.types.suggested_message_data_details.deserialize_json(
                data["suggestedMessageData"]
            )
        }
    elif data.get("notesData") is not None:
        import capo_qconnect.types.notes_data_details

        return {
            "notesData": capo_qconnect.types.notes_data_details.deserialize_json(
                data["notesData"]
            )
        }
    elif data.get("notesChunkData") is not None:
        import capo_qconnect.types.notes_chunk_data_details

        return {
            "notesChunkData": capo_qconnect.types.notes_chunk_data_details.deserialize_json(
                data["notesChunkData"]
            )
        }
    elif data.get("proactiveRecommendationData") is not None:
        import capo_qconnect.types.proactive_recommendation_data_details

        return {
            "proactiveRecommendationData": capo_qconnect.types.proactive_recommendation_data_details.deserialize_json(
                data["proactiveRecommendationData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DataDetails: no recognized variant key")


def redact_sensitive(value: DataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contentData" in value:
        import capo_qconnect.types.content_data_details

        out["contentData"] = capo_qconnect.types.content_data_details.redact_sensitive(
            value["contentData"]
        )
    if "generativeData" in value:
        import capo_qconnect.types.generative_data_details

        out["generativeData"] = (
            capo_qconnect.types.generative_data_details.redact_sensitive(
                value["generativeData"]
            )
        )
    if "intentDetectedData" in value:
        import capo_qconnect.types.intent_detected_data_details

        out["intentDetectedData"] = (
            capo_qconnect.types.intent_detected_data_details.redact_sensitive(
                value["intentDetectedData"]
            )
        )
    if "sourceContentData" in value:
        import capo_qconnect.types.source_content_data_details

        out["sourceContentData"] = (
            capo_qconnect.types.source_content_data_details.redact_sensitive(
                value["sourceContentData"]
            )
        )
    if "generativeChunkData" in value:
        import capo_qconnect.types.generative_chunk_data_details

        out["generativeChunkData"] = (
            capo_qconnect.types.generative_chunk_data_details.redact_sensitive(
                value["generativeChunkData"]
            )
        )
    if "emailResponseChunkData" in value:
        import capo_qconnect.types.email_response_chunk_data_details

        out["emailResponseChunkData"] = (
            capo_qconnect.types.email_response_chunk_data_details.redact_sensitive(
                value["emailResponseChunkData"]
            )
        )
    if "emailOverviewChunkData" in value:
        import capo_qconnect.types.email_overview_chunk_data_details

        out["emailOverviewChunkData"] = (
            capo_qconnect.types.email_overview_chunk_data_details.redact_sensitive(
                value["emailOverviewChunkData"]
            )
        )
    if "emailGenerativeAnswerChunkData" in value:
        import capo_qconnect.types.email_generative_answer_chunk_data_details

        out["emailGenerativeAnswerChunkData"] = (
            capo_qconnect.types.email_generative_answer_chunk_data_details.redact_sensitive(
                value["emailGenerativeAnswerChunkData"]
            )
        )
    if "caseSummarizationChunkData" in value:
        import capo_qconnect.types.case_summarization_chunk_data_details

        out["caseSummarizationChunkData"] = (
            capo_qconnect.types.case_summarization_chunk_data_details.redact_sensitive(
                value["caseSummarizationChunkData"]
            )
        )
    if "suggestedMessageData" in value:
        import capo_qconnect.types.suggested_message_data_details

        out["suggestedMessageData"] = (
            capo_qconnect.types.suggested_message_data_details.redact_sensitive(
                value["suggestedMessageData"]
            )
        )
    if "notesData" in value:
        import capo_qconnect.types.notes_data_details

        out["notesData"] = capo_qconnect.types.notes_data_details.redact_sensitive(
            value["notesData"]
        )
    if "notesChunkData" in value:
        import capo_qconnect.types.notes_chunk_data_details

        out["notesChunkData"] = (
            capo_qconnect.types.notes_chunk_data_details.redact_sensitive(
                value["notesChunkData"]
            )
        )
    return out
