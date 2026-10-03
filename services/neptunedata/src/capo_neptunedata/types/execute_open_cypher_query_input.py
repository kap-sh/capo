"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteOpenCypherQueryInput``."""

from typing_extensions import NotRequired, TypedDict

from capo_neptunedata.errors import DeserializationError


class ExecuteOpenCypherQueryInput(TypedDict, closed=True):
    open_cypher_query: "str"
    """<p>The openCypher query string to be executed.</p>"""
    parameters: NotRequired["str"]
    """<p>The openCypher query parameters for query execution. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-parameterized-queries.html">Examples of openCypher parameterized queries</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteOpenCypherQueryInput) -> dict:
    out: dict = {}
    out["query"] = value["open_cypher_query"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    return out


def deserialize_json(data: dict) -> ExecuteOpenCypherQueryInput:
    out: ExecuteOpenCypherQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        out["open_cypher_query"] = data["query"]
    else:
        raise DeserializationError(
            "ExecuteOpenCypherQueryInput.open_cypher_query required"
        )
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    return out
