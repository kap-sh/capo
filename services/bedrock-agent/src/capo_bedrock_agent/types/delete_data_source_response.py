"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data_source_status
    import capo_bedrock_agent.types.id


class DeleteDataSourceResponse(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to which the data source that was deleted belonged.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source that was deleted.</p>"""
    status: "capo_bedrock_agent.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceResponse) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    import capo_bedrock_agent.types.data_source_status

    out["status"] = capo_bedrock_agent.types.data_source_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDataSourceResponse:
    out: DeleteDataSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agent.types.data_source_status

        out["status"] = capo_bedrock_agent.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent.types.data_source_status.DataSourceStatus", ""
        )
    return out
