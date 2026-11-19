"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartDatasetGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.dataset_generation_description
    import capo_bedrock_agentcore.types.dataset_generation_name
    import capo_bedrock_agentcore.types.dataset_id
    import capo_bedrock_agentcore.types.generation_source
    import capo_bedrock_agentcore.types.scenario_type


class StartDatasetGenerationRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset to add the generated examples to. The dataset must be <code>ACTIVE</code>.</p>"""
    name: "capo_bedrock_agentcore.types.dataset_generation_name.DatasetGenerationName"
    """<p>The name of the dataset generation. The generation ID starts with this name.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.dataset_generation_description.DatasetGenerationDescription"
    ]
    """<p>A description of the dataset generation.</p>"""
    scenario_type: NotRequired[
        "capo_bedrock_agentcore.types.scenario_type.ScenarioType"
    ]
    """<p>The type of scenario to generate. If you don't specify a value, the generation produces <code>DYNAMIC</code> scenarios.</p>"""
    source: "capo_bedrock_agentcore.types.generation_source.GenerationSource"
    """<p>Where the generation reads sessions from, and how it selects, samples, labels and redacts them.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDatasetGenerationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "scenario_type" in value:
        import capo_bedrock_agentcore.types.scenario_type

        out["scenarioType"] = capo_bedrock_agentcore.types.scenario_type.serialize_json(
            value["scenario_type"]
        )
    import capo_bedrock_agentcore.types.generation_source

    out["source"] = capo_bedrock_agentcore.types.generation_source.serialize_json(
        value["source"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartDatasetGenerationRequest:
    out: StartDatasetGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("scenarioType") is not None:
        import capo_bedrock_agentcore.types.scenario_type

        out["scenario_type"] = (
            capo_bedrock_agentcore.types.scenario_type.deserialize_json(
                data["scenarioType"]
            )
        )
    if data.get("source") is not None:
        import capo_bedrock_agentcore.types.generation_source

        out["source"] = capo_bedrock_agentcore.types.generation_source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
