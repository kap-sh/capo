"""Generated from Smithy shape ``com.amazonaws.glue#DeleteGlossaryTermRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_term_id


class DeleteGlossaryTermRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.glossary_term_id.GlossaryTermId"
    """<p>The unique identifier of the glossary term to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGlossaryTermRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGlossaryTermRequest:
    out: DeleteGlossaryTermRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
