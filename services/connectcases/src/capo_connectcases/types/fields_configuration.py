"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.field_identifier_list


class FieldsConfiguration(TypedDict, closed=True):
    field_ids: "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
    """<p>The fields whose values to take from the source case. Each field must exist on the source case and must be a field that can be merged. Don't list the same field more than once.</p>"""
    source_case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>The unique identifier of the case to take the field values from. This must be the secondary case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldsConfiguration) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_identifier_list

    out["fieldIds"] = capo_connectcases.types.field_identifier_list.serialize_json(
        value["field_ids"]
    )
    out["sourceCaseId"] = value["source_case_id"]
    return out


def deserialize_json(data: dict) -> FieldsConfiguration:
    out: FieldsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fieldIds") is not None:
        import capo_connectcases.types.field_identifier_list

        out["field_ids"] = (
            capo_connectcases.types.field_identifier_list.deserialize_json(
                data["fieldIds"]
            )
        )
    else:
        out["field_ids"] = []
    if data.get("sourceCaseId") is not None:
        out["source_case_id"] = data["sourceCaseId"]
    else:
        out["source_case_id"] = ""
    return out
