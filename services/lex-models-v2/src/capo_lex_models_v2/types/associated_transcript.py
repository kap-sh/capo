"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssociatedTranscript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.transcript


class AssociatedTranscript(TypedDict, closed=True):
    transcript: NotRequired["capo_lex_models_v2.types.transcript.Transcript"]
    """<p>The content of the transcript that meets the search filter criteria. For the JSON format of the transcript, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/designing-output-format.html">Output transcript format</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTranscript) -> dict:
    out: dict = {}
    if "transcript" in value:
        out["transcript"] = value["transcript"]
    return out


def deserialize_json(data: dict) -> AssociatedTranscript:
    out: AssociatedTranscript = {}  # type: ignore[typeddict-item]
    if data.get("transcript") is not None:
        out["transcript"] = data["transcript"]
    return out
