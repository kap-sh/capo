"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessageListDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.non_negative_integer
    import capo_iotfleetwise.types.structure_message_name
    import capo_iotfleetwise.types.structured_message
    import capo_iotfleetwise.types.structured_message_list_type


class StructuredMessageListDefinition(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.structure_message_name.StructureMessageName"
    """<p>The name of the structured message list definition. </p>"""
    member_type: "capo_iotfleetwise.types.structured_message.StructuredMessage"
    """<p>The member type of the structured message list definition.</p>"""
    list_type: (
        "capo_iotfleetwise.types.structured_message_list_type.StructuredMessageListType"
    )
    """<p>The type of list of the structured message list definition.</p>"""
    capacity: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The capacity of the structured message list definition when the list type is <code>FIXED_CAPACITY</code> or <code>DYNAMIC_BOUNDED_CAPACITY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessageListDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_iotfleetwise.types.structured_message

    out["memberType"] = (
        capo_iotfleetwise.types.structured_message.serialize_aws_json_1_0(
            value["member_type"]
        )
    )
    import capo_iotfleetwise.types.structured_message_list_type

    out["listType"] = (
        capo_iotfleetwise.types.structured_message_list_type.serialize_aws_json_1_0(
            value["list_type"]
        )
    )
    out["capacity"] = value.get("capacity", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> StructuredMessageListDefinition:
    out: StructuredMessageListDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("memberType") is not None:
        import capo_iotfleetwise.types.structured_message

        out["member_type"] = (
            capo_iotfleetwise.types.structured_message.deserialize_aws_json_1_0(
                data["memberType"]
            )
        )
    else:
        out["member_type"] = {"$unknown": {"name": ""}}
    if data.get("listType") is not None:
        import capo_iotfleetwise.types.structured_message_list_type

        out["list_type"] = (
            capo_iotfleetwise.types.structured_message_list_type.deserialize_aws_json_1_0(
                data["listType"]
            )
        )
    else:
        import typing

        out["list_type"] = typing.cast(
            "capo_iotfleetwise.types.structured_message_list_type.StructuredMessageListType",
            "",
        )
    if data.get("capacity") is not None:
        out["capacity"] = data["capacity"]
    else:
        out["capacity"] = 0
    return out
