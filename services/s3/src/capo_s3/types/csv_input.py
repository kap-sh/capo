"""Generated from Smithy shape ``com.amazonaws.s3#CSVInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.allow_quoted_record_delimiter
    import capo_s3.types.comments
    import capo_s3.types.field_delimiter
    import capo_s3.types.file_header_info
    import capo_s3.types.quote_character
    import capo_s3.types.quote_escape_character
    import capo_s3.types.record_delimiter


class CSVInput(TypedDict, closed=True):
    file_header_info: NotRequired["capo_s3.types.file_header_info.FileHeaderInfo"]
    """<p>Describes the first line of input. Valid values are:</p> <ul> <li> <p> <code>NONE</code>: First line is not a header.</p> </li> <li> <p> <code>IGNORE</code>: First line is a header, but you can't use the header values to indicate the column in an expression. You can use column position (such as _1, _2, …) to indicate the column (<code>SELECT s._1 FROM OBJECT s</code>).</p> </li> <li> <p> <code>Use</code>: First line is a header, and you can use the header value to identify a column in an expression (<code>SELECT "name" FROM OBJECT</code>). </p> </li> </ul>"""
    comments: NotRequired["capo_s3.types.comments.Comments"]
    """<p>A single character used to indicate that a row should be ignored when the character is present at the start of that row. You can specify any character to indicate a comment line. The default character is <code>#</code>.</p> <p>Default: <code>#</code> </p>"""
    quote_escape_character: NotRequired[
        "capo_s3.types.quote_escape_character.QuoteEscapeCharacter"
    ]
    """<p>A single character used for escaping the quotation mark character inside an already escaped value. For example, the value <code>\"\"\" a , b \"\"\"</code> is parsed as <code>\" a , b \"</code>.</p>"""
    record_delimiter: NotRequired["capo_s3.types.record_delimiter.RecordDelimiter"]
    """<p>A single character used to separate individual records in the input. Instead of the default value, you can specify an arbitrary delimiter.</p>"""
    field_delimiter: NotRequired["capo_s3.types.field_delimiter.FieldDelimiter"]
    """<p>A single character used to separate individual fields in a record. You can specify an arbitrary delimiter.</p>"""
    quote_character: NotRequired["capo_s3.types.quote_character.QuoteCharacter"]
    """<p>A single character used for escaping when the field delimiter is part of the value. For example, if the value is <code>a, b</code>, Amazon S3 wraps this field value in quotation marks, as follows: <code>" a , b "</code>.</p> <p>Type: String</p> <p>Default: <code>"</code> </p> <p>Ancestors: <code>CSV</code> </p>"""
    allow_quoted_record_delimiter: NotRequired[
        "capo_s3.types.allow_quoted_record_delimiter.AllowQuotedRecordDelimiter"
    ]
    """<p>Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CSVInput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "file_header_info" in value:
        import capo_s3.types.file_header_info

        capo_s3.types.file_header_info.serialize_xml(
            value["file_header_info"], el, "FileHeaderInfo"
        )
    if "comments" in value:
        SubElement(el, "Comments").text = str(value["comments"])
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
    if "allow_quoted_record_delimiter" in value:
        SubElement(el, "AllowQuotedRecordDelimiter").text = (
            "true" if value["allow_quoted_record_delimiter"] else "false"
        )


def deserialize_xml(el: Element) -> CSVInput:
    out: CSVInput = {}  # type: ignore[typeddict-item]
    child_file_header_info = el.find("FileHeaderInfo")
    if child_file_header_info is not None:
        import capo_s3.types.file_header_info

        out["file_header_info"] = capo_s3.types.file_header_info.deserialize_xml(
            child_file_header_info
        )
    child_comments = el.find("Comments")
    if child_comments is not None:
        out["comments"] = str(child_comments.text or "")
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
    child_allow_quoted_record_delimiter = el.find("AllowQuotedRecordDelimiter")
    if child_allow_quoted_record_delimiter is not None:
        out["allow_quoted_record_delimiter"] = (
            child_allow_quoted_record_delimiter.text or ""
        ).lower() == "true"
    return out
