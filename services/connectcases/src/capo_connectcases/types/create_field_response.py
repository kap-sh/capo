"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_arn
    import capo_connectcases.types.field_id


class CreateFieldResponse(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    field_arn: "capo_connectcases.types.field_arn.FieldArn"
    """<p>The Amazon Resource Name (ARN) of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFieldResponse) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["fieldArn"] = value["field_arn"]
    return out


def deserialize_json(data: dict) -> CreateFieldResponse:
    out: CreateFieldResponse = {}  # type: ignore[typeddict-item]
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    else:
        out["field_id"] = ""
    if data.get("fieldArn") is not None:
        out["field_arn"] = data["fieldArn"]
    else:
        out["field_arn"] = ""
    return out
