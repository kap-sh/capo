"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteDatasetExamplesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.example_id_list


class DeleteDatasetExamplesRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    example_ids: "capo_bedrock_agentcore_control.types.example_id_list.ExampleIdList"
    """<p> The IDs of the examples to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetExamplesRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agentcore_control.types.example_id_list

    out["exampleIds"] = (
        capo_bedrock_agentcore_control.types.example_id_list.serialize_json(
            value["example_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteDatasetExamplesRequest:
    out: DeleteDatasetExamplesRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("exampleIds") is not None:
        import capo_bedrock_agentcore_control.types.example_id_list

        out["example_ids"] = (
            capo_bedrock_agentcore_control.types.example_id_list.deserialize_json(
                data["exampleIds"]
            )
        )
    else:
        raise DeserializationError("DeleteDatasetExamplesRequest.example_ids required")
    return out
