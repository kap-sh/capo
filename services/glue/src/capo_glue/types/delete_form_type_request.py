"""Generated from Smithy shape ``com.amazonaws.glue#DeleteFormTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_type_id


class DeleteFormTypeRequest(TypedDict, closed=True):
    identifier: "capo_glue.types.form_type_id.FormTypeId"
    """<p>The identifier of the form type to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFormTypeRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFormTypeRequest:
    out: DeleteFormTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
