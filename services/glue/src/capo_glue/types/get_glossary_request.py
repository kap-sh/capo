"""Generated from Smithy shape ``com.amazonaws.glue#GetGlossaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_id


class GetGlossaryRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.glossary_id.GlossaryId"
    """<p>The unique identifier of the glossary to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGlossaryRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGlossaryRequest:
    out: GetGlossaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
