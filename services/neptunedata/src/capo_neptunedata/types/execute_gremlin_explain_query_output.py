"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinExplainQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.report_as_text


class ExecuteGremlinExplainQueryOutput(TypedDict, closed=True):
    output: NotRequired["capo_neptunedata.types.report_as_text.ReportAsText"]
    """<p>A text blob containing the Gremlin explain result, as described in <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-traversal-tuning.html">Tuning Gremlin queries</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinExplainQueryOutput) -> dict:
    out: dict = {}
    if "output" in value:
        import capo_neptunedata.types.report_as_text

        out["output"] = capo_neptunedata.types.report_as_text.serialize_json(
            value["output"]
        )
    return out


def deserialize_json(data: dict) -> ExecuteGremlinExplainQueryOutput:
    out: ExecuteGremlinExplainQueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("output") is not None:
        import capo_neptunedata.types.report_as_text

        out["output"] = capo_neptunedata.types.report_as_text.deserialize_json(
            data["output"]
        )
    return out
