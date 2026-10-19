"""Generated from Smithy shape ``com.amazonaws.glue#GetFormTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_type_id


class GetFormTypeRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.form_type_id.FormTypeId"
    """<p>The identifier of the form type to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFormTypeRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFormTypeRequest:
    out: GetFormTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
