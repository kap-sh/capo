"""Generated from Smithy shape ``com.amazonaws.glue#UpdateGlossaryTermRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_long_description
    import capo_glue.types.glossary_short_description
    import capo_glue.types.glossary_term_id
    import capo_glue.types.glossary_term_name
    import capo_glue.types.hash_string


class UpdateGlossaryTermRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.glossary_term_id.GlossaryTermId"
    """<p>The unique identifier of the glossary term to update.</p>"""
    name: NotRequired["capo_glue.types.glossary_term_name.GlossaryTermName"]
    """<p>The updated name of the glossary term.</p>"""
    short_description: NotRequired[
        "capo_glue.types.glossary_short_description.GlossaryShortDescription"
    ]
    """<p>The updated short description of the glossary term.</p>"""
    long_description: NotRequired[
        "capo_glue.types.glossary_long_description.GlossaryLongDescription"
    ]
    """<p>The updated long description of the glossary term.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGlossaryTermRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    if "name" in value:
        out["Name"] = value["name"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGlossaryTermRequest:
    out: UpdateGlossaryTermRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ShortDescription") is not None:
        out["short_description"] = data["ShortDescription"]
    if data.get("LongDescription") is not None:
        out["long_description"] = data["LongDescription"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
