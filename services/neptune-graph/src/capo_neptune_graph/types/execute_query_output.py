"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExecuteQueryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.query_response_blob


class ExecuteQueryOutput(TypedDict, closed=True):
    payload: "capo_neptune_graph.types.query_response_blob.QueryResponseBlob"
    """<p>The query results.</p>"""


def redact_sensitive(value: ExecuteQueryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Streaming Data Redacted ***"
    return out
