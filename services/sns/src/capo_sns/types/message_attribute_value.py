"""Generated from Smithy shape ``com.amazonaws.sns#MessageAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.binary
    import capo_sns.types.string


class MessageAttributeValue(TypedDict, closed=True):
    data_type: "capo_sns.types.string.String"
    """<p>Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes">Message Attribute Data Types</a>.</p>"""
    string_value: NotRequired["capo_sns.types.string.String"]
    """<p>Strings are Unicode with UTF8 binary encoding. For a list of code values, see <a href="https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters">ASCII Printable Characters</a>.</p>"""
    binary_value: NotRequired["capo_sns.types.binary.Binary"]
    """<p>Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageAttributeValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DataType", str(value["data_type"])))
    if "string_value" in value:
        pairs.append((f"{key_prefix}StringValue", str(value["string_value"])))
    if "binary_value" in value:
        import capo_sns.types.binary

        capo_sns.types.binary.serialize_query(
            value["binary_value"], pairs, f"{key_prefix}BinaryValue"
        )


def deserialize_query(el: Element) -> MessageAttributeValue:
    out: MessageAttributeValue = {}  # type: ignore[typeddict-item]
    child_data_type = el.find("DataType")
    if child_data_type is not None:
        out["data_type"] = str(child_data_type.text or "")
    else:
        raise DeserializationError("MessageAttributeValue.data_type required")
    child_string_value = el.find("StringValue")
    if child_string_value is not None:
        out["string_value"] = str(child_string_value.text or "")
    child_binary_value = el.find("BinaryValue")
    if child_binary_value is not None:
        import capo_sns.types.binary

        out["binary_value"] = capo_sns.types.binary.deserialize_query(
            child_binary_value
        )
    return out
