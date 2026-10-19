"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteOpenCypherExplainQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.open_cypher_explain_mode


class ExecuteOpenCypherExplainQueryInput(TypedDict, closed=True):
    open_cypher_query: "str"
    """<p>The openCypher query string.</p>"""
    parameters: NotRequired["str"]
    """<p>The openCypher query parameters.</p>"""
    explain_mode: (
        "capo_neptunedata.types.open_cypher_explain_mode.OpenCypherExplainMode"
    )
    """<p>The openCypher <code>explain</code> mode. Can be one of: <code>static</code>, <code>dynamic</code>, or <code>details</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteOpenCypherExplainQueryInput) -> dict:
    out: dict = {}
    out["query"] = value["open_cypher_query"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    import capo_neptunedata.types.open_cypher_explain_mode

    out["explain"] = capo_neptunedata.types.open_cypher_explain_mode.serialize_json(
        value["explain_mode"]
    )
    return out


def deserialize_json(data: dict) -> ExecuteOpenCypherExplainQueryInput:
    out: ExecuteOpenCypherExplainQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        out["open_cypher_query"] = data["query"]
    else:
        out["open_cypher_query"] = ""
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    if data.get("explain") is not None:
        import capo_neptunedata.types.open_cypher_explain_mode

        out["explain_mode"] = (
            capo_neptunedata.types.open_cypher_explain_mode.deserialize_json(
                data["explain"]
            )
        )
    else:
        import typing

        out["explain_mode"] = typing.cast(
            "capo_neptunedata.types.open_cypher_explain_mode.OpenCypherExplainMode", ""
        )
    return out
