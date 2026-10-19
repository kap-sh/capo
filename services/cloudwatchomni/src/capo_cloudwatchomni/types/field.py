"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Field``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.field_list


class Field(TypedDict, closed=True):
    name: "str"
    """The name of the field. Field names are case-sensitive and must be used exactly as returned when referencing them in query expressions."""
    children: NotRequired["capo_cloudwatchomni.types.field_list.FieldList"]
    """Child fields nested under this field."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Field) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "children" in value:
        import capo_cloudwatchomni.types.field_list

        out["children"] = capo_cloudwatchomni.types.field_list.serialize_cbor(
            value["children"]
        )
    return out


def deserialize_cbor(data: dict) -> Field:
    out: Field = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("children") is not None:
        import capo_cloudwatchomni.types.field_list

        out["children"] = capo_cloudwatchomni.types.field_list.deserialize_cbor(
            data["children"]
        )
    return out
