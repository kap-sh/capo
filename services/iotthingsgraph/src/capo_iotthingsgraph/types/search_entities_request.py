"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.entity_filters
    import capo_iotthingsgraph.types.entity_types
    import capo_iotthingsgraph.types.max_results
    import capo_iotthingsgraph.types.next_token
    import capo_iotthingsgraph.types.version


class SearchEntitiesRequest(TypedDict, closed=True):
    entity_types: "capo_iotthingsgraph.types.entity_types.EntityTypes"
    """<p>The entity types for which to search.</p>"""
    filters: NotRequired["capo_iotthingsgraph.types.entity_filters.EntityFilters"]
    """<p>Optional filter to apply to the search. Valid filters are <code>NAME</code> <code>NAMESPACE</code>, <code>SEMANTIC_TYPE_PATH</code> and <code>REFERENCED_ENTITY_ID</code>. <code>REFERENCED_ENTITY_ID</code> filters on entities that are used by the entity in the result set. For example, you can filter on the ID of a property that is used in a state.</p> <p>Multiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["capo_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchEntitiesRequest) -> dict:
    out: dict = {}
    import capo_iotthingsgraph.types.entity_types

    out["entityTypes"] = capo_iotthingsgraph.types.entity_types.serialize_aws_json_1_1(
        value["entity_types"]
    )
    if "filters" in value:
        import capo_iotthingsgraph.types.entity_filters

        out["filters"] = (
            capo_iotthingsgraph.types.entity_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchEntitiesRequest:
    out: SearchEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("entityTypes") is not None:
        import capo_iotthingsgraph.types.entity_types

        out["entity_types"] = (
            capo_iotthingsgraph.types.entity_types.deserialize_aws_json_1_1(
                data["entityTypes"]
            )
        )
    else:
        out["entity_types"] = []
    if data.get("filters") is not None:
        import capo_iotthingsgraph.types.entity_filters

        out["filters"] = (
            capo_iotthingsgraph.types.entity_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("namespaceVersion") is not None:
        out["namespace_version"] = data["namespaceVersion"]
    return out
