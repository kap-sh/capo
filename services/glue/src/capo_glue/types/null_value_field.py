"""Generated from Smithy shape ``com.amazonaws.glue#NullValueField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.datatype
    import capo_glue.types.enclosed_in_string_property


class NullValueField(TypedDict, closed=True):
    value: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The value of the null placeholder.</p>"""
    datatype: "capo_glue.types.datatype.Datatype"
    """<p>The datatype of the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NullValueField) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_glue.types.datatype

    out["Datatype"] = capo_glue.types.datatype.serialize_aws_json_1_1(value["datatype"])
    return out


def deserialize_aws_json_1_1(data: dict) -> NullValueField:
    out: NullValueField = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Datatype") is not None:
        import capo_glue.types.datatype

        out["datatype"] = capo_glue.types.datatype.deserialize_aws_json_1_1(
            data["Datatype"]
        )
    else:
        raise DeserializationError("NullValueField.datatype required")
    return out
