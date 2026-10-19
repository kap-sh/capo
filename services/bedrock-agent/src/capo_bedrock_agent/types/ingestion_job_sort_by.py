"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.ingestion_job_sort_by_attribute
    import capo_bedrock_agent.types.sort_order


class IngestionJobSortBy(TypedDict, closed=True):
    attribute: "capo_bedrock_agent.types.ingestion_job_sort_by_attribute.IngestionJobSortByAttribute"
    """<p>The name of field or attribute to apply sorting of data.</p>"""
    order: "capo_bedrock_agent.types.sort_order.SortOrder"
    """<p>The order for sorting the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobSortBy) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.ingestion_job_sort_by_attribute

    out["attribute"] = (
        capo_bedrock_agent.types.ingestion_job_sort_by_attribute.serialize_json(
            value["attribute"]
        )
    )
    import capo_bedrock_agent.types.sort_order

    out["order"] = capo_bedrock_agent.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> IngestionJobSortBy:
    out: IngestionJobSortBy = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_bedrock_agent.types.ingestion_job_sort_by_attribute

        out["attribute"] = (
            capo_bedrock_agent.types.ingestion_job_sort_by_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        import typing

        out["attribute"] = typing.cast(
            "capo_bedrock_agent.types.ingestion_job_sort_by_attribute.IngestionJobSortByAttribute",
            "",
        )
    if data.get("order") is not None:
        import capo_bedrock_agent.types.sort_order

        out["order"] = capo_bedrock_agent.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        import typing

        out["order"] = typing.cast("capo_bedrock_agent.types.sort_order.SortOrder", "")
    return out
