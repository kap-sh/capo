"""Generated from Smithy shape ``com.amazonaws.glue#GetGlossaryTermRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_term_id


class GetGlossaryTermRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.glossary_term_id.GlossaryTermId"
    """<p>The unique identifier of the glossary term to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGlossaryTermRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGlossaryTermRequest:
    out: GetGlossaryTermRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
