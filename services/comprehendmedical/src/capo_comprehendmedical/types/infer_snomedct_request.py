"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#InferSNOMEDCTRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.ontology_linking_bounded_length_string


class InferSNOMEDCTRequest(TypedDict, closed=True):
    text: "capo_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString"
    """<p>The input text to be analyzed using InferSNOMEDCT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferSNOMEDCTRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferSNOMEDCTRequest:
    out: InferSNOMEDCTRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    return out
