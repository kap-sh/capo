"""Generated from Smithy shape ``com.amazonaws.agentregistry#SearchDiscoverableRegistryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.metadata_filter_expression
    import capo_agent_registry.types.registry_id_list
    import capo_agent_registry.types.search_query


class SearchDiscoverableRegistryRecordsRequest(TypedDict, closed=True):
    search_query: "capo_agent_registry.types.search_query.SearchQuery"
    """<p> The natural language query to search for matching registry records.</p>"""
    registry_ids: "capo_agent_registry.types.registry_id_list.RegistryIdList"
    """<p> The registry identifiers to search within. Currently, you must specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the registry ID.</p>"""
    max_results: "int"
    """<p> The maximum number of results to return. Valid values are 1 through 20. The default value is 10.</p>"""
    filters: NotRequired[
        "capo_agent_registry.types.metadata_filter_expression.MetadataFilterExpression"
    ]
    """<p> An optional structured JSON metadata filter that narrows the search results. Supports the field-level operators <code>$eq</code>, <code>$ne</code>, and <code>$in</code>, and the logical operators <code>$and</code> and <code>$or</code> on filterable fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDiscoverableRegistryRecordsRequest) -> dict:
    out: dict = {}
    out["searchQuery"] = value["search_query"]
    import capo_agent_registry.types.registry_id_list

    out["registryIds"] = capo_agent_registry.types.registry_id_list.serialize_json(
        value["registry_ids"]
    )
    out["maxResults"] = value.get("max_results", 10)
    if "filters" in value:
        out["filters"] = value["filters"]
    return out


def deserialize_json(data: dict) -> SearchDiscoverableRegistryRecordsRequest:
    out: SearchDiscoverableRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("searchQuery") is not None:
        out["search_query"] = data["searchQuery"]
    else:
        raise DeserializationError(
            "SearchDiscoverableRegistryRecordsRequest.search_query required"
        )
    if data.get("registryIds") is not None:
        import capo_agent_registry.types.registry_id_list

        out["registry_ids"] = (
            capo_agent_registry.types.registry_id_list.deserialize_json(
                data["registryIds"]
            )
        )
    else:
        raise DeserializationError(
            "SearchDiscoverableRegistryRecordsRequest.registry_ids required"
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    if data.get("filters") is not None:
        out["filters"] = data["filters"]
    return out
