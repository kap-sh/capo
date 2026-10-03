"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SearchRegistryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.metadata_filter_expression
    import capo_bedrock_agentcore.types.registry_id_list


class SearchRegistryRecordsRequest(TypedDict, closed=True):
    search_query: "str"
    """<p> The search query to find matching registry records.</p>"""
    registry_ids: "capo_bedrock_agentcore.types.registry_id_list.RegistryIdList"
    """<p> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.</p>"""
    max_results: "int"
    """<p> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.</p>"""
    filters: NotRequired[
        "capo_bedrock_agentcore.types.metadata_filter_expression.MetadataFilterExpression"
    ]
    """<p> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>). For example, to filter by descriptor type: <code>{"descriptorType": {"$eq": "MCP"}}</code>. To combine filters: <code>{"$and": [{"descriptorType": {"$eq": "MCP"}}, {"name": {"$eq": "my-tool"}}]}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRegistryRecordsRequest) -> dict:
    out: dict = {}
    out["searchQuery"] = value["search_query"]
    import capo_bedrock_agentcore.types.registry_id_list

    out["registryIds"] = capo_bedrock_agentcore.types.registry_id_list.serialize_json(
        value["registry_ids"]
    )
    out["maxResults"] = value.get("max_results", 10)
    if "filters" in value:
        out["filters"] = value["filters"]
    return out


def deserialize_json(data: dict) -> SearchRegistryRecordsRequest:
    out: SearchRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("searchQuery") is not None:
        out["search_query"] = data["searchQuery"]
    else:
        raise DeserializationError("SearchRegistryRecordsRequest.search_query required")
    if data.get("registryIds") is not None:
        import capo_bedrock_agentcore.types.registry_id_list

        out["registry_ids"] = (
            capo_bedrock_agentcore.types.registry_id_list.deserialize_json(
                data["registryIds"]
            )
        )
    else:
        raise DeserializationError("SearchRegistryRecordsRequest.registry_ids required")
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    if data.get("filters") is not None:
        out["filters"] = data["filters"]
    return out
