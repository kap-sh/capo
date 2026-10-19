"""Generated from Smithy shape ``com.amazonaws.glue#CreateGlossaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glossary_name
    import capo_glue.types.hash_string
    import capo_glue.types.metadata_description


class CreateGlossaryRequest(TypedDict, closed=True):
    name: "capo_glue.types.glossary_name.GlossaryName"
    """<p>The name of the glossary.</p>"""
    description: NotRequired["capo_glue.types.metadata_description.MetadataDescription"]
    """<p>The description of the glossary.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGlossaryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGlossaryRequest:
    out: CreateGlossaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
