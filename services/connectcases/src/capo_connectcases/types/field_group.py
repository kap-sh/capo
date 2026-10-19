"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_list


class FieldGroup(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>Name of the field group.</p>"""
    fields: "capo_connectcases.types.field_list.FieldList"
    """<p>Represents an ordered list containing field related information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_connectcases.types.field_list

    out["fields"] = capo_connectcases.types.field_list.serialize_json(value["fields"])
    return out


def deserialize_json(data: dict) -> FieldGroup:
    out: FieldGroup = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_list

        out["fields"] = capo_connectcases.types.field_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    return out
