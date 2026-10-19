"""Generated from Smithy shape ``com.amazonaws.glue#PutFormTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_type_name
    import capo_glue.types.form_type_schema
    import capo_glue.types.hash_string


class PutFormTypeRequest(TypedDict, closed=True):
    name: "capo_glue.types.form_type_name.FormTypeName"
    """<p>The name of the form type. Must start with an uppercase letter.</p>"""
    schema: "capo_glue.types.form_type_schema.FormTypeSchema"
    """<p>The Smithy IDL schema definition for the form type.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFormTypeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Schema"] = value["schema"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFormTypeRequest:
    out: PutFormTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    else:
        out["schema"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
