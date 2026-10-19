"""Generated from Smithy shape ``com.amazonaws.glue#CreateGlossaryTermRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_id
    import capo_glue.types.glossary_long_description
    import capo_glue.types.glossary_short_description
    import capo_glue.types.glossary_term_name
    import capo_glue.types.hash_string


class CreateGlossaryTermRequest(TypedDict, closed=True):
    glossary_identifier: "capo_glue.types.glossary_id.GlossaryId"
    """<p>The unique identifier of the glossary in which to create the term.</p>"""
    name: "capo_glue.types.glossary_term_name.GlossaryTermName"
    """<p>The name of the glossary term.</p>"""
    short_description: NotRequired[
        "capo_glue.types.glossary_short_description.GlossaryShortDescription"
    ]
    """<p>A short description of the glossary term.</p>"""
    long_description: NotRequired[
        "capo_glue.types.glossary_long_description.GlossaryLongDescription"
    ]
    """<p>A long description of the glossary term.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGlossaryTermRequest) -> dict:
    out: dict = {}
    out["GlossaryIdentifier"] = value["glossary_identifier"]
    out["Name"] = value["name"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGlossaryTermRequest:
    out: CreateGlossaryTermRequest = {}  # type: ignore[typeddict-item]
    if data.get("GlossaryIdentifier") is not None:
        out["glossary_identifier"] = data["GlossaryIdentifier"]
    else:
        out["glossary_identifier"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    if data.get("LongDescription") is not None:
        out["long_description"] = data["LongDescription"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
