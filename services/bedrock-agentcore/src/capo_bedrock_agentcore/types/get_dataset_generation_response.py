"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetDatasetGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.dataset_generation_description
    import capo_bedrock_agentcore.types.dataset_generation_id
    import capo_bedrock_agentcore.types.dataset_generation_name
    import capo_bedrock_agentcore.types.dataset_generation_status
    import capo_bedrock_agentcore.types.dataset_id
    import capo_bedrock_agentcore.types.generation_error_details_list
    import capo_bedrock_agentcore.types.generation_results
    import capo_bedrock_agentcore.types.generation_source_record
    import capo_bedrock_agentcore.types.redaction_summary
    import capo_bedrock_agentcore.types.scenario_type


class GetDatasetGenerationResponse(TypedDict, closed=True):
    generation_id: (
        "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId"
    )
    """<p>The unique identifier of the dataset generation.</p>"""
    name: "capo_bedrock_agentcore.types.dataset_generation_name.DatasetGenerationName"
    """<p>The name of the dataset generation.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.dataset_generation_description.DatasetGenerationDescription"
    ]
    """<p>The description of the dataset generation.</p>"""
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    scenario_type: "capo_bedrock_agentcore.types.scenario_type.ScenarioType"
    """<p>The type of scenario the generation produces. This is the value from the request, or <code>DYNAMIC</code> if the request didn't specify one.</p>"""
    status: (
        "capo_bedrock_agentcore.types.dataset_generation_status.DatasetGenerationStatus"
    )
    """<p>The status of the dataset generation.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason the dataset generation failed. Present only when the status is <code>FAILED</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the dataset generation started.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time at which the dataset generation last changed status.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The time at which the dataset generation finished. Present only when the generation has finished.</p>"""
    source: NotRequired[
        "capo_bedrock_agentcore.types.generation_source_record.GenerationSourceRecord"
    ]
    """<p>The source the generation was started with, including the resolved time window. If you selected sessions and traces by ID, the response gives the number of IDs instead of the IDs.</p>"""
    generation_results: NotRequired[
        "capo_bedrock_agentcore.types.generation_results.GenerationResults"
    ]
    """<p>Counts of the sessions, scenarios and examples the generation has processed.</p>"""
    redaction_summary: NotRequired[
        "capo_bedrock_agentcore.types.redaction_summary.RedactionSummary"
    ]
    """<p>A summary of what redaction found. Present only when the generation was started with redaction.</p>"""
    error_details: NotRequired[
        "capo_bedrock_agentcore.types.generation_error_details_list.GenerationErrorDetailsList"
    ]
    """<p>The errors the generation hit, grouped by error code. The list holds the 10 most frequent error codes, most frequent first.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetGenerationResponse) -> dict:
    out: dict = {}
    out["generationId"] = value["generation_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["datasetId"] = value["dataset_id"]
    import capo_bedrock_agentcore.types.scenario_type

    out["scenarioType"] = capo_bedrock_agentcore.types.scenario_type.serialize_json(
        value["scenario_type"]
    )
    import capo_bedrock_agentcore.types.dataset_generation_status

    out["status"] = (
        capo_bedrock_agentcore.types.dataset_generation_status.serialize_json(
            value["status"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import capo_bedrock_agentcore._protocol.serialize

    out["createdAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["updatedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "completed_at" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["completedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    if "source" in value:
        import capo_bedrock_agentcore.types.generation_source_record

        out["source"] = (
            capo_bedrock_agentcore.types.generation_source_record.serialize_json(
                value["source"]
            )
        )
    if "generation_results" in value:
        import capo_bedrock_agentcore.types.generation_results

        out["generationResults"] = (
            capo_bedrock_agentcore.types.generation_results.serialize_json(
                value["generation_results"]
            )
        )
    if "redaction_summary" in value:
        import capo_bedrock_agentcore.types.redaction_summary

        out["redactionSummary"] = (
            capo_bedrock_agentcore.types.redaction_summary.serialize_json(
                value["redaction_summary"]
            )
        )
    if "error_details" in value:
        import capo_bedrock_agentcore.types.generation_error_details_list

        out["errorDetails"] = (
            capo_bedrock_agentcore.types.generation_error_details_list.serialize_json(
                value["error_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDatasetGenerationResponse:
    out: GetDatasetGenerationResponse = {}  # type: ignore[typeddict-item]
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    else:
        out["generation_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("scenarioType") is not None:
        import capo_bedrock_agentcore.types.scenario_type

        out["scenario_type"] = (
            capo_bedrock_agentcore.types.scenario_type.deserialize_json(
                data["scenarioType"]
            )
        )
    else:
        import typing

        out["scenario_type"] = typing.cast(
            "capo_bedrock_agentcore.types.scenario_type.ScenarioType", ""
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.dataset_generation_status

        out["status"] = (
            capo_bedrock_agentcore.types.dataset_generation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.dataset_generation_status.DatasetGenerationStatus",
            "",
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    if data.get("source") is not None:
        import capo_bedrock_agentcore.types.generation_source_record

        out["source"] = (
            capo_bedrock_agentcore.types.generation_source_record.deserialize_json(
                data["source"]
            )
        )
    if data.get("generationResults") is not None:
        import capo_bedrock_agentcore.types.generation_results

        out["generation_results"] = (
            capo_bedrock_agentcore.types.generation_results.deserialize_json(
                data["generationResults"]
            )
        )
    if data.get("redactionSummary") is not None:
        import capo_bedrock_agentcore.types.redaction_summary

        out["redaction_summary"] = (
            capo_bedrock_agentcore.types.redaction_summary.deserialize_json(
                data["redactionSummary"]
            )
        )
    if data.get("errorDetails") is not None:
        import capo_bedrock_agentcore.types.generation_error_details_list

        out["error_details"] = (
            capo_bedrock_agentcore.types.generation_error_details_list.deserialize_json(
                data["errorDetails"]
            )
        )
    return out
