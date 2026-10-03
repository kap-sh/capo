"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinQueryInput``."""

from typing_extensions import NotRequired, TypedDict

from capo_neptunedata.errors import DeserializationError


class ExecuteGremlinQueryInput(TypedDict, closed=True):
    gremlin_query: "str"
    """<p>Using this API, you can run Gremlin queries in string format much as you can using the HTTP endpoint. The interface is compatible with whatever Gremlin version your DB cluster is using (see the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-client.html#best-practices-gremlin-java-latest">Tinkerpop client section</a> to determine which Gremlin releases your engine version supports).</p>"""
    serializer: NotRequired["str"]
    """<p>If non-null, the query results are returned in a serialized response message in the format specified by this parameter. See the <a href="https://tinkerpop.apache.org/docs/current/reference/#_graphson">GraphSON</a> section in the TinkerPop documentation for a list of the formats that are currently supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinQueryInput) -> dict:
    out: dict = {}
    out["gremlin"] = value["gremlin_query"]
    return out


def deserialize_json(data: dict) -> ExecuteGremlinQueryInput:
    out: ExecuteGremlinQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("gremlin") is not None:
        out["gremlin_query"] = data["gremlin"]
    else:
        raise DeserializationError("ExecuteGremlinQueryInput.gremlin_query required")
    return out
