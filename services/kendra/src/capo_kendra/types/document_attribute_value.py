"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_string_list_value
    import capo_kendra.types.document_attribute_string_value
    import capo_kendra.types.long
    import capo_kendra.types.timestamp


class DocumentAttributeValue(TypedDict, closed=True):
    string_value: NotRequired[
        "capo_kendra.types.document_attribute_string_value.DocumentAttributeStringValue"
    ]
    """<p>A string, such as "department".</p>"""
    string_list_value: NotRequired[
        "capo_kendra.types.document_attribute_string_list_value.DocumentAttributeStringListValue"
    ]
    """<p>A list of strings. The default maximum length or number of strings is 10.</p>"""
    long_value: NotRequired["capo_kendra.types.long.Long"]
    """<p>A long integer value.</p>"""
    date_value: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>A date expressed as an ISO 8601 string.</p> <p>It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeValue) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    if "string_list_value" in value:
        import capo_kendra.types.document_attribute_string_list_value

        out["StringListValue"] = (
            capo_kendra.types.document_attribute_string_list_value.serialize_aws_json_1_1(
                value["string_list_value"]
            )
        )
    if "long_value" in value:
        out["LongValue"] = value["long_value"]
    if "date_value" in value:
        import capo_kendra.types.timestamp

        out["DateValue"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["date_value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttributeValue:
    out: DocumentAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("StringValue") is not None:
        out["string_value"] = data["StringValue"]
    if data.get("StringListValue") is not None:
        import capo_kendra.types.document_attribute_string_list_value

        out["string_list_value"] = (
            capo_kendra.types.document_attribute_string_list_value.deserialize_aws_json_1_1(
                data["StringListValue"]
            )
        )
    if data.get("LongValue") is not None:
        out["long_value"] = data["LongValue"]
    if data.get("DateValue") is not None:
        import capo_kendra.types.timestamp

        out["date_value"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["DateValue"]
        )
    return out
