"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetExamplesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_arn
    import capo_bedrock_agentcore_control.types.dataset_example_list
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_version


class ListDatasetExamplesResponse(TypedDict, closed=True):
    dataset_arn: "capo_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    dataset_version: (
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    """<p> The version returned. </p>"""
    examples: (
        "capo_bedrock_agentcore_control.types.dataset_example_list.DatasetExampleList"
    )
    """<p> Paginated example content. Each element is a JSON object containing at least an <code>exampleId</code> field plus the schema-specific content fields. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetExamplesResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    out["datasetVersion"] = value["dataset_version"]
    import capo_bedrock_agentcore_control.types.dataset_example_list

    out["examples"] = (
        capo_bedrock_agentcore_control.types.dataset_example_list.serialize_json(
            value["examples"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetExamplesResponse:
    out: ListDatasetExamplesResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("ListDatasetExamplesResponse.dataset_arn required")
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("ListDatasetExamplesResponse.dataset_id required")
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    else:
        raise DeserializationError(
            "ListDatasetExamplesResponse.dataset_version required"
        )
    if data.get("examples") is not None:
        import capo_bedrock_agentcore_control.types.dataset_example_list

        out["examples"] = (
            capo_bedrock_agentcore_control.types.dataset_example_list.deserialize_json(
                data["examples"]
            )
        )
    else:
        raise DeserializationError("ListDatasetExamplesResponse.examples required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDatasetExamplesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "examples" in value:
        import capo_bedrock_agentcore_control.types.dataset_example_list

        out["examples"] = (
            capo_bedrock_agentcore_control.types.dataset_example_list.redact_sensitive(
                value["examples"]
            )
        )
    return out
