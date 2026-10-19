"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessageFieldNameAndDataTypePair``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.structure_message_name
    import capo_iotfleetwise.types.structured_message


class StructuredMessageFieldNameAndDataTypePair(TypedDict, closed=True):
    field_name: "capo_iotfleetwise.types.structure_message_name.StructureMessageName"
    """<p>The field name of the structured message. It determines how a data value is referenced in the target language. </p>"""
    data_type: "capo_iotfleetwise.types.structured_message.StructuredMessage"
    """<p>The data type. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessageFieldNameAndDataTypePair) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    import capo_iotfleetwise.types.structured_message

    out["dataType"] = capo_iotfleetwise.types.structured_message.serialize_aws_json_1_0(
        value["data_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StructuredMessageFieldNameAndDataTypePair:
    out: StructuredMessageFieldNameAndDataTypePair = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    else:
        out["field_name"] = ""
    if data.get("dataType") is not None:
        import capo_iotfleetwise.types.structured_message

        out["data_type"] = (
            capo_iotfleetwise.types.structured_message.deserialize_aws_json_1_0(
                data["dataType"]
            )
        )
    else:
        import capo_iotfleetwise.types._unknown

        out["data_type"] = capo_iotfleetwise.types._unknown.UnknownUnionMember("")
    return out
