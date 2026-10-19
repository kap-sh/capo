"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.schema_status_reason_code


class SchemaStatusReason(TypedDict, closed=True):
    code: "capo_cleanrooms.types.schema_status_reason_code.SchemaStatusReasonCode"
    """<p>The schema status reason code.</p>"""
    message: "str"
    """<p>An explanation of the schema status reason code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusReason) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.schema_status_reason_code

    out["code"] = capo_cleanrooms.types.schema_status_reason_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SchemaStatusReason:
    out: SchemaStatusReason = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_cleanrooms.types.schema_status_reason_code

        out["code"] = capo_cleanrooms.types.schema_status_reason_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_cleanrooms.types.schema_status_reason_code.SchemaStatusReasonCode", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
