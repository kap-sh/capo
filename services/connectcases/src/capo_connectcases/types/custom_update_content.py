"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomUpdateContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_value_list


class CustomUpdateContent(TypedDict, closed=True):
    fields: "capo_connectcases.types.field_value_list.FieldValueList"
    """<p>List of updated field values for the <code>Custom</code> related item. All existing and new fields, and their associated values should be included. Fields not included as part of this request will be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomUpdateContent) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_value_list

    out["fields"] = capo_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> CustomUpdateContent:
    out: CustomUpdateContent = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_value_list

        out["fields"] = capo_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    return out
