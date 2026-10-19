"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AddDatasetExamplesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_arn
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_status
    import capo_bedrock_agentcore_control.types.example_id_list


class AddDatasetExamplesResponse(TypedDict, closed=True):
    dataset_arn: "capo_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    status: "capo_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    added_count: "int"
    """<p> The number of examples added. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the examples were added. </p>"""
    example_ids: "capo_bedrock_agentcore_control.types.example_id_list.ExampleIdList"
    """<p> IDs of all added examples (auto-generated UUIDs). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDatasetExamplesResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import capo_bedrock_agentcore_control.types.dataset_status

    out["status"] = capo_bedrock_agentcore_control.types.dataset_status.serialize_json(
        value["status"]
    )
    out["addedCount"] = value["added_count"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.example_id_list

    out["exampleIds"] = (
        capo_bedrock_agentcore_control.types.example_id_list.serialize_json(
            value["example_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddDatasetExamplesResponse:
    out: AddDatasetExamplesResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.dataset_status.DatasetStatus", ""
        )
    if data.get("addedCount") is not None:
        out["added_count"] = data["addedCount"]
    else:
        out["added_count"] = 0
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("exampleIds") is not None:
        import capo_bedrock_agentcore_control.types.example_id_list

        out["example_ids"] = (
            capo_bedrock_agentcore_control.types.example_id_list.deserialize_json(
                data["exampleIds"]
            )
        )
    else:
        out["example_ids"] = []
    return out
