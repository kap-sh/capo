"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_get_field_error_list
    import capo_connectcases.types.batch_get_field_list


class BatchGetFieldResponse(TypedDict, closed=True):
    fields: "capo_connectcases.types.batch_get_field_list.BatchGetFieldList"
    """<p>A list of detailed field information. </p>"""
    errors: "capo_connectcases.types.batch_get_field_error_list.BatchGetFieldErrorList"
    """<p>A list of field errors. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.batch_get_field_list

    out["fields"] = capo_connectcases.types.batch_get_field_list.serialize_json(
        value["fields"]
    )
    import capo_connectcases.types.batch_get_field_error_list

    out["errors"] = capo_connectcases.types.batch_get_field_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetFieldResponse:
    out: BatchGetFieldResponse = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.batch_get_field_list

        out["fields"] = capo_connectcases.types.batch_get_field_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("errors") is not None:
        import capo_connectcases.types.batch_get_field_error_list

        out["errors"] = (
            capo_connectcases.types.batch_get_field_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
