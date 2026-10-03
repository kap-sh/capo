"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AddDatasetExamplesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.data_source_type
    import capo_bedrock_agentcore_control.types.dataset_id


class AddDatasetExamplesRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset to add examples to. </p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    source: "capo_bedrock_agentcore_control.types.data_source_type.DataSourceType"
    """<p> Source of examples to add. Provide either inline examples or an S3 URI pointing to a JSONL file. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDatasetExamplesRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agentcore_control.types.data_source_type

    out["source"] = (
        capo_bedrock_agentcore_control.types.data_source_type.serialize_json(
            value["source"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddDatasetExamplesRequest:
    out: AddDatasetExamplesRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("source") is not None:
        import capo_bedrock_agentcore_control.types.data_source_type

        out["source"] = (
            capo_bedrock_agentcore_control.types.data_source_type.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("AddDatasetExamplesRequest.source required")
    return out
