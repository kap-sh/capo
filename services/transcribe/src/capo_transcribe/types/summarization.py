"""Generated from Smithy shape ``com.amazonaws.transcribe#Summarization``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.boolean


class Summarization(TypedDict, closed=True):
    generate_abstractive_summary: "capo_transcribe.types.boolean.Boolean"
    """<p>Enables Generative call summarization in your Call Analytics request</p> <p>Generative call summarization provides a summary of the transcript including important components discussed in the conversation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tca-enable-summarization.html">Enabling generative call summarization</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Summarization) -> dict:
    out: dict = {}
    out["GenerateAbstractiveSummary"] = value["generate_abstractive_summary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Summarization:
    out: Summarization = {}  # type: ignore[typeddict-item]
    if data.get("GenerateAbstractiveSummary") is not None:
        out["generate_abstractive_summary"] = data["GenerateAbstractiveSummary"]
    else:
        raise DeserializationError(
            "Summarization.generate_abstractive_summary required"
        )
    return out
