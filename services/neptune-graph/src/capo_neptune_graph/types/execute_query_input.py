"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExecuteQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.document_valued_map
    import capo_neptune_graph.types.explain_mode
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.plan_cache_type
    import capo_neptune_graph.types.query_language


class ExecuteQueryInput(TypedDict, closed=True):
    graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    query_string: "str"
    """<p>The query string to be executed.</p>"""
    language: "capo_neptune_graph.types.query_language.QueryLanguage"
    """<p>The query language the query is written in. Currently only openCypher is supported.</p>"""
    parameters: NotRequired[
        "capo_neptune_graph.types.document_valued_map.DocumentValuedMap"
    ]
    """<p>The data parameters the query can use in JSON format. For example: {"name": "john", "age": 20}. (optional) </p>"""
    plan_cache: NotRequired["capo_neptune_graph.types.plan_cache_type.PlanCacheType"]
    """<p>Query plan cache is a feature that saves the query plan and reuses it on successive executions of the same query. This reduces query latency, and works for both <code>READ</code> and <code>UPDATE</code> queries. The plan cache is an LRU cache with a 5 minute TTL and a capacity of 1000.</p>"""
    explain_mode: NotRequired["capo_neptune_graph.types.explain_mode.ExplainMode"]
    """<p>The explain mode parameter returns a query explain instead of the actual query results. A query explain can be used to gather insights about the query execution such as planning decisions, time spent on each operator, solutions flowing etc.</p>"""
    query_timeout_milliseconds: NotRequired["int"]
    """<p>Specifies the query timeout duration, in milliseconds. (optional)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteQueryInput) -> dict:
    out: dict = {}
    out["query"] = value["query_string"]
    import capo_neptune_graph.types.query_language

    out["language"] = capo_neptune_graph.types.query_language.serialize_json(
        value["language"]
    )
    if "parameters" in value:
        import capo_neptune_graph.types.document_valued_map

        out["parameters"] = capo_neptune_graph.types.document_valued_map.serialize_json(
            value["parameters"]
        )
    if "plan_cache" in value:
        import capo_neptune_graph.types.plan_cache_type

        out["planCache"] = capo_neptune_graph.types.plan_cache_type.serialize_json(
            value["plan_cache"]
        )
    if "explain_mode" in value:
        import capo_neptune_graph.types.explain_mode

        out["explain"] = capo_neptune_graph.types.explain_mode.serialize_json(
            value["explain_mode"]
        )
    if "query_timeout_milliseconds" in value:
        out["queryTimeoutMilliseconds"] = value["query_timeout_milliseconds"]
    return out


def deserialize_json(data: dict) -> ExecuteQueryInput:
    out: ExecuteQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        out["query_string"] = data["query"]
    else:
        raise DeserializationError("ExecuteQueryInput.query_string required")
    if data.get("language") is not None:
        import capo_neptune_graph.types.query_language

        out["language"] = capo_neptune_graph.types.query_language.deserialize_json(
            data["language"]
        )
    else:
        raise DeserializationError("ExecuteQueryInput.language required")
    if data.get("parameters") is not None:
        import capo_neptune_graph.types.document_valued_map

        out["parameters"] = (
            capo_neptune_graph.types.document_valued_map.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("planCache") is not None:
        import capo_neptune_graph.types.plan_cache_type

        out["plan_cache"] = capo_neptune_graph.types.plan_cache_type.deserialize_json(
            data["planCache"]
        )
    if data.get("explain") is not None:
        import capo_neptune_graph.types.explain_mode

        out["explain_mode"] = capo_neptune_graph.types.explain_mode.deserialize_json(
            data["explain"]
        )
    if data.get("queryTimeoutMilliseconds") is not None:
        out["query_timeout_milliseconds"] = data["queryTimeoutMilliseconds"]
    return out
