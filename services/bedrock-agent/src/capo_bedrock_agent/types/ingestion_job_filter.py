"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.ingestion_job_filter_attribute
    import capo_bedrock_agent.types.ingestion_job_filter_operator
    import capo_bedrock_agent.types.ingestion_job_filter_values


class IngestionJobFilter(TypedDict, closed=True):
    attribute: "capo_bedrock_agent.types.ingestion_job_filter_attribute.IngestionJobFilterAttribute"
    """<p>The name of field or attribute to apply the filter.</p>"""
    operator: "capo_bedrock_agent.types.ingestion_job_filter_operator.IngestionJobFilterOperator"
    """<p>The operation to apply to the field or attribute.</p>"""
    values: (
        "capo_bedrock_agent.types.ingestion_job_filter_values.IngestionJobFilterValues"
    )
    """<p>A list of values that belong to the field or attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobFilter) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.ingestion_job_filter_attribute

    out["attribute"] = (
        capo_bedrock_agent.types.ingestion_job_filter_attribute.serialize_json(
            value["attribute"]
        )
    )
    import capo_bedrock_agent.types.ingestion_job_filter_operator

    out["operator"] = (
        capo_bedrock_agent.types.ingestion_job_filter_operator.serialize_json(
            value["operator"]
        )
    )
    import capo_bedrock_agent.types.ingestion_job_filter_values

    out["values"] = capo_bedrock_agent.types.ingestion_job_filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> IngestionJobFilter:
    out: IngestionJobFilter = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_bedrock_agent.types.ingestion_job_filter_attribute

        out["attribute"] = (
            capo_bedrock_agent.types.ingestion_job_filter_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        import typing

        out["attribute"] = typing.cast(
            "capo_bedrock_agent.types.ingestion_job_filter_attribute.IngestionJobFilterAttribute",
            "",
        )
    if data.get("operator") is not None:
        import capo_bedrock_agent.types.ingestion_job_filter_operator

        out["operator"] = (
            capo_bedrock_agent.types.ingestion_job_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_bedrock_agent.types.ingestion_job_filter_operator.IngestionJobFilterOperator",
            "",
        )
    if data.get("values") is not None:
        import capo_bedrock_agent.types.ingestion_job_filter_values

        out["values"] = (
            capo_bedrock_agent.types.ingestion_job_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
