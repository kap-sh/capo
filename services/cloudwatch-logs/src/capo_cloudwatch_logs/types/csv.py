"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CSV``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.columns
    import capo_cloudwatch_logs.types.delimiter
    import capo_cloudwatch_logs.types.destination_field
    import capo_cloudwatch_logs.types.quote_character
    import capo_cloudwatch_logs.types.source


class CSV(TypedDict, closed=True):
    quote_character: NotRequired[
        "capo_cloudwatch_logs.types.quote_character.QuoteCharacter"
    ]
    """<p>The character used used as a text qualifier for a single column of data. If you omit this, the double quotation mark <code>"</code> character is used.</p>"""
    delimiter: NotRequired["capo_cloudwatch_logs.types.delimiter.Delimiter"]
    """<p>The character used to separate each column in the original comma-separated value log event. If you omit this, the processor looks for the comma <code>,</code> character as the delimiter.</p>"""
    columns: NotRequired["capo_cloudwatch_logs.types.columns.Columns"]
    """<p>An array of names to use for the columns in the transformed log event.</p> <p>If you omit this, default column names (<code>[column_1, column_2 ...]</code>) are used.</p>"""
    source: NotRequired["capo_cloudwatch_logs.types.source.Source"]
    """<p>The path to the field in the log event that has the comma separated values to be parsed. If you omit this value, the whole log message is processed.</p>"""
    destination: NotRequired[
        "capo_cloudwatch_logs.types.destination_field.DestinationField"
    ]
    """<p>The path to the parent field to put transformed key value pairs under. If you omit this value, the key value pairs will be placed under the root node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CSV) -> dict:
    out: dict = {}
    if "quote_character" in value:
        out["quoteCharacter"] = value["quote_character"]
    if "delimiter" in value:
        out["delimiter"] = value["delimiter"]
    if "columns" in value:
        import capo_cloudwatch_logs.types.columns

        out["columns"] = capo_cloudwatch_logs.types.columns.serialize_aws_json_1_1(
            value["columns"]
        )
    if "source" in value:
        out["source"] = value["source"]
    if "destination" in value:
        out["destination"] = value["destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CSV:
    out: CSV = {}  # type: ignore[typeddict-item]
    if data.get("quoteCharacter") is not None:
        out["quote_character"] = data["quoteCharacter"]
    if data.get("delimiter") is not None:
        out["delimiter"] = data["delimiter"]
    if data.get("columns") is not None:
        import capo_cloudwatch_logs.types.columns

        out["columns"] = capo_cloudwatch_logs.types.columns.deserialize_aws_json_1_1(
            data["columns"]
        )
    if data.get("source") is not None:
        out["source"] = data["source"]
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    return out
