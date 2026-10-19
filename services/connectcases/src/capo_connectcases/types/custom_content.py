"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_value_list


class CustomContent(TypedDict, closed=True):
    fields: "capo_connectcases.types.field_value_list.FieldValueList"
    """<p>List of field values for the <code>Custom</code> related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomContent) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_value_list

    out["fields"] = capo_connectcases.types.field_value_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> CustomContent:
    out: CustomContent = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_value_list

        out["fields"] = capo_connectcases.types.field_value_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    return out
