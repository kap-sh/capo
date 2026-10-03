"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateDatasetExamplesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.dataset_example_list
    import capo_bedrock_agentcore_control.types.dataset_id


class UpdateDatasetExamplesRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    examples: (
        "capo_bedrock_agentcore_control.types.dataset_example_list.DatasetExampleList"
    )
    """<p> Examples to update. Each element is a JSON object containing a required <code>exampleId</code> field identifying the existing example, plus the replacement fields. Maximum 1000 examples per call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetExamplesRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_agentcore_control.types.dataset_example_list

    out["examples"] = (
        capo_bedrock_agentcore_control.types.dataset_example_list.serialize_json(
            value["examples"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDatasetExamplesRequest:
    out: UpdateDatasetExamplesRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("examples") is not None:
        import capo_bedrock_agentcore_control.types.dataset_example_list

        out["examples"] = (
            capo_bedrock_agentcore_control.types.dataset_example_list.deserialize_json(
                data["examples"]
            )
        )
    else:
        raise DeserializationError("UpdateDatasetExamplesRequest.examples required")
    return out
