"""Generated from Smithy shape ``com.amazonaws.s3#CSVOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.field_delimiter
    import capo_s3.types.quote_character
    import capo_s3.types.quote_escape_character
    import capo_s3.types.quote_fields
    import capo_s3.types.record_delimiter


class CSVOutput(TypedDict, closed=True):
    quote_fields: NotRequired["capo_s3.types.quote_fields.QuoteFields"]
    """<p>Indicates whether to use quotation marks around output fields. </p> <ul> <li> <p> <code>ALWAYS</code>: Always use quotation marks for output fields.</p> </li> <li> <p> <code>ASNEEDED</code>: Use quotation marks for output fields when needed.</p> </li> </ul>"""
    quote_escape_character: NotRequired[
        "capo_s3.types.quote_escape_character.QuoteEscapeCharacter"
    ]
    """<p>The single character used for escaping the quote character inside an already escaped value.</p>"""
    record_delimiter: NotRequired["capo_s3.types.record_delimiter.RecordDelimiter"]
    """<p>A single character used to separate individual records in the output. Instead of the default value, you can specify an arbitrary delimiter.</p>"""
    field_delimiter: NotRequired["capo_s3.types.field_delimiter.FieldDelimiter"]
    """<p>The value used to separate individual fields in a record. You can specify an arbitrary delimiter.</p>"""
    quote_character: NotRequired["capo_s3.types.quote_character.QuoteCharacter"]
    """<p>A single character used for escaping when the field delimiter is part of the value. For example, if the value is <code>a, b</code>, Amazon S3 wraps this field value in quotation marks, as follows: <code>" a , b "</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CSVOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "quote_fields" in value:
        import capo_s3.types.quote_fields

        capo_s3.types.quote_fields.serialize_xml(
            value["quote_fields"], el, "QuoteFields"
        )
    if "quote_escape_character" in value:
        SubElement(el, "QuoteEscapeCharacter").text = str(
            value["quote_escape_character"]
        )
    if "record_delimiter" in value:
        SubElement(el, "RecordDelimiter").text = str(value["record_delimiter"])
    if "field_delimiter" in value:
        SubElement(el, "FieldDelimiter").text = str(value["field_delimiter"])
    if "quote_character" in value:
        SubElement(el, "QuoteCharacter").text = str(value["quote_character"])


def deserialize_xml(el: Element) -> CSVOutput:
    out: CSVOutput = {}  # type: ignore[typeddict-item]
    child_quote_fields = el.find("QuoteFields")
    if child_quote_fields is not None:
        import capo_s3.types.quote_fields

        out["quote_fields"] = capo_s3.types.quote_fields.deserialize_xml(
            child_quote_fields
        )
    child_quote_escape_character = el.find("QuoteEscapeCharacter")
    if child_quote_escape_character is not None:
        out["quote_escape_character"] = str(child_quote_escape_character.text or "")
    child_record_delimiter = el.find("RecordDelimiter")
    if child_record_delimiter is not None:
        out["record_delimiter"] = str(child_record_delimiter.text or "")
    child_field_delimiter = el.find("FieldDelimiter")
    if child_field_delimiter is not None:
        out["field_delimiter"] = str(child_field_delimiter.text or "")
    child_quote_character = el.find("QuoteCharacter")
    if child_quote_character is not None:
        out["quote_character"] = str(child_quote_character.text or "")
    return out
