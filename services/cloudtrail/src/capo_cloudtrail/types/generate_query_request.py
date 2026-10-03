"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GenerateQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_list
    import capo_cloudtrail.types.prompt


class GenerateQueryRequest(TypedDict, closed=True):
    event_data_stores: "capo_cloudtrail.types.event_data_store_list.EventDataStoreList"
    """<p> The ARN (or ID suffix of the ARN) of the event data store that you want to query. You can only specify one event data store. </p>"""
    prompt: "capo_cloudtrail.types.prompt.Prompt"
    """<p> The prompt that you want to use to generate the query. The prompt must be in English. For example prompts, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html#lake-query-generator-examples">Example prompts</a> in the <i>CloudTrail </i> user guide. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateQueryRequest) -> dict:
    out: dict = {}
    import capo_cloudtrail.types.event_data_store_list

    out["EventDataStores"] = (
        capo_cloudtrail.types.event_data_store_list.serialize_aws_json_1_1(
            value["event_data_stores"]
        )
    )
    out["Prompt"] = value["prompt"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateQueryRequest:
    out: GenerateQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStores") is not None:
        import capo_cloudtrail.types.event_data_store_list

        out["event_data_stores"] = (
            capo_cloudtrail.types.event_data_store_list.deserialize_aws_json_1_1(
                data["EventDataStores"]
            )
        )
    else:
        raise DeserializationError("GenerateQueryRequest.event_data_stores required")
    if data.get("Prompt") is not None:
        out["prompt"] = data["Prompt"]
    else:
        raise DeserializationError("GenerateQueryRequest.prompt required")
    return out
