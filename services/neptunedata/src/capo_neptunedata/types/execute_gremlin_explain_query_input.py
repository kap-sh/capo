"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinExplainQueryInput``."""

from typing_extensions import TypedDict


class ExecuteGremlinExplainQueryInput(TypedDict, closed=True):
    gremlin_query: "str"
    """<p>The Gremlin explain query string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinExplainQueryInput) -> dict:
    out: dict = {}
    out["gremlin"] = value["gremlin_query"]
    return out


def deserialize_json(data: dict) -> ExecuteGremlinExplainQueryInput:
    out: ExecuteGremlinExplainQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("gremlin") is not None:
        out["gremlin_query"] = data["gremlin"]
    else:
        out["gremlin_query"] = ""
    return out
