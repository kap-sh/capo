"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListQueriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.query_summary_list


class ListQueriesOutput(TypedDict, closed=True):
    queries: "capo_neptune_graph.types.query_summary_list.QuerySummaryList"
    """<p>A list of current openCypher queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueriesOutput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.query_summary_list

    out["queries"] = capo_neptune_graph.types.query_summary_list.serialize_json(
        value["queries"]
    )
    return out


def deserialize_json(data: dict) -> ListQueriesOutput:
    out: ListQueriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("queries") is not None:
        import capo_neptune_graph.types.query_summary_list

        out["queries"] = capo_neptune_graph.types.query_summary_list.deserialize_json(
            data["queries"]
        )
    else:
        out["queries"] = []
    return out
