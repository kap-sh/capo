"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateInferenceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.inference_profile_description
    import capo_bedrock.types.inference_profile_model_source
    import capo_bedrock.types.inference_profile_name
    import capo_bedrock.types.tag_list


class CreateInferenceProfileRequest(TypedDict, closed=True):
    inference_profile_name: (
        "capo_bedrock.types.inference_profile_name.InferenceProfileName"
    )
    """<p>A name for the inference profile.</p>"""
    description: NotRequired[
        "capo_bedrock.types.inference_profile_description.InferenceProfileDescription"
    ]
    """<p>A description for the inference profile.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    model_source: (
        "capo_bedrock.types.inference_profile_model_source.InferenceProfileModelSource"
    )
    """<p>The foundation model or system-defined inference profile that the inference profile will track metrics and costs for.</p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>An array of objects, each of which contains a tag and its value. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInferenceProfileRequest) -> dict:
    out: dict = {}
    out["inferenceProfileName"] = value["inference_profile_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    import capo_bedrock.types.inference_profile_model_source

    out["modelSource"] = (
        capo_bedrock.types.inference_profile_model_source.serialize_json(
            value["model_source"]
        )
    )
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateInferenceProfileRequest:
    out: CreateInferenceProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("inferenceProfileName") is not None:
        out["inference_profile_name"] = data["inferenceProfileName"]
    else:
        raise DeserializationError(
            "CreateInferenceProfileRequest.inference_profile_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("modelSource") is not None:
        import capo_bedrock.types.inference_profile_model_source

        out["model_source"] = (
            capo_bedrock.types.inference_profile_model_source.deserialize_json(
                data["modelSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInferenceProfileRequest.model_source required"
        )
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
