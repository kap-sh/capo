"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryInputData``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.case_summarization_input_data
    import capo_qconnect.types.intent_input_data
    import capo_qconnect.types.query_text_input_data


class _QueryInputData_queryTextInputData(TypedDict, closed=True):
    queryTextInputData: "capo_qconnect.types.query_text_input_data.QueryTextInputData"


class _QueryInputData_intentInputData(TypedDict, closed=True):
    intentInputData: "capo_qconnect.types.intent_input_data.IntentInputData"


class _QueryInputData_caseSummarizationInputData(TypedDict, closed=True):
    caseSummarizationInputData: (
        "capo_qconnect.types.case_summarization_input_data.CaseSummarizationInputData"
    )


QueryInputData: TypeAlias = (
    _QueryInputData_queryTextInputData
    | _QueryInputData_intentInputData
    | _QueryInputData_caseSummarizationInputData
)


# --- restJson1 ser/de ---
def serialize_json(value: QueryInputData) -> dict:
    if "queryTextInputData" in value:
        import capo_qconnect.types.query_text_input_data

        return {
            "queryTextInputData": capo_qconnect.types.query_text_input_data.serialize_json(
                value["queryTextInputData"]
            )
        }
    elif "intentInputData" in value:
        import capo_qconnect.types.intent_input_data

        return {
            "intentInputData": capo_qconnect.types.intent_input_data.serialize_json(
                value["intentInputData"]
            )
        }
    elif "caseSummarizationInputData" in value:
        import capo_qconnect.types.case_summarization_input_data

        return {
            "caseSummarizationInputData": capo_qconnect.types.case_summarization_input_data.serialize_json(
                value["caseSummarizationInputData"]
            )
        }
    else:
        raise SerializationError("QueryInputData: no variant present")


def deserialize_json(data: dict) -> QueryInputData:
    if data.get("queryTextInputData") is not None:
        import capo_qconnect.types.query_text_input_data

        return {
            "queryTextInputData": capo_qconnect.types.query_text_input_data.deserialize_json(
                data["queryTextInputData"]
            )
        }
    elif data.get("intentInputData") is not None:
        import capo_qconnect.types.intent_input_data

        return {
            "intentInputData": capo_qconnect.types.intent_input_data.deserialize_json(
                data["intentInputData"]
            )
        }
    elif data.get("caseSummarizationInputData") is not None:
        import capo_qconnect.types.case_summarization_input_data

        return {
            "caseSummarizationInputData": capo_qconnect.types.case_summarization_input_data.deserialize_json(
                data["caseSummarizationInputData"]
            )
        }
    else:
        raise DeserializationError("QueryInputData: no recognized variant key")


def redact_sensitive(value: QueryInputData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "queryTextInputData" in value:
        import capo_qconnect.types.query_text_input_data

        out["queryTextInputData"] = (
            capo_qconnect.types.query_text_input_data.redact_sensitive(
                value["queryTextInputData"]
            )
        )
    return out
