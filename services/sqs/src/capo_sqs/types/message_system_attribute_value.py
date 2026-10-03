"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sqs.types.binary
    import capo_sqs.types.binary_list
    import capo_sqs.types.string
    import capo_sqs.types.string_list


class MessageSystemAttributeValue(TypedDict, closed=True):
    string_value: NotRequired["capo_sqs.types.string.String"]
    """<p>Strings are Unicode with UTF-8 binary encoding. For a list of code values, see <a href="http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters">ASCII Printable Characters</a>.</p>"""
    binary_value: NotRequired["capo_sqs.types.binary.Binary"]
    """<p>Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.</p>"""
    string_list_values: NotRequired["capo_sqs.types.string_list.StringList"]
    """<p>Not implemented. Reserved for future use.</p>"""
    binary_list_values: NotRequired["capo_sqs.types.binary_list.BinaryList"]
    """<p>Not implemented. Reserved for future use.</p>"""
    data_type: "capo_sqs.types.string.String"
    """<p>Amazon SQS supports the following logical data types: <code>String</code>, <code>Number</code>, and <code>Binary</code>. For the <code>Number</code> data type, you must use <code>StringValue</code>.</p> <p>You can also append custom labels. For more information, see <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes">Amazon SQS Message Attributes</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageSystemAttributeValue) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    if "binary_value" in value:
        import capo_sqs.types.binary

        out["BinaryValue"] = capo_sqs.types.binary.serialize_aws_json_1_0(
            value["binary_value"]
        )
    if "string_list_values" in value:
        import capo_sqs.types.string_list

        out["StringListValues"] = capo_sqs.types.string_list.serialize_aws_json_1_0(
            value["string_list_values"]
        )
    if "binary_list_values" in value:
        import capo_sqs.types.binary_list

        out["BinaryListValues"] = capo_sqs.types.binary_list.serialize_aws_json_1_0(
            value["binary_list_values"]
        )
    out["DataType"] = value["data_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageSystemAttributeValue:
    out: MessageSystemAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("StringValue") is not None:
        out["string_value"] = data["StringValue"]
    if data.get("BinaryValue") is not None:
        import capo_sqs.types.binary

        out["binary_value"] = capo_sqs.types.binary.deserialize_aws_json_1_0(
            data["BinaryValue"]
        )
    if data.get("StringListValues") is not None:
        import capo_sqs.types.string_list

        out["string_list_values"] = capo_sqs.types.string_list.deserialize_aws_json_1_0(
            data["StringListValues"]
        )
    if data.get("BinaryListValues") is not None:
        import capo_sqs.types.binary_list

        out["binary_list_values"] = capo_sqs.types.binary_list.deserialize_aws_json_1_0(
            data["BinaryListValues"]
        )
    if data.get("DataType") is not None:
        out["data_type"] = data["DataType"]
    else:
        raise DeserializationError("MessageSystemAttributeValue.data_type required")
    return out
