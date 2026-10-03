"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinProfileQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.report_as_text


class ExecuteGremlinProfileQueryOutput(TypedDict, closed=True):
    output: NotRequired["capo_neptunedata.types.report_as_text.ReportAsText"]
    """<p>A text blob containing the Gremlin Profile result. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html">Gremlin profile API in Neptune</a> for details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinProfileQueryOutput) -> dict:
    out: dict = {}
    if "output" in value:
        import capo_neptunedata.types.report_as_text

        out["output"] = capo_neptunedata.types.report_as_text.serialize_json(
            value["output"]
        )
    return out


def deserialize_json(data: dict) -> ExecuteGremlinProfileQueryOutput:
    out: ExecuteGremlinProfileQueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("output") is not None:
        import capo_neptunedata.types.report_as_text

        out["output"] = capo_neptunedata.types.report_as_text.deserialize_json(
            data["output"]
        )
    return out
