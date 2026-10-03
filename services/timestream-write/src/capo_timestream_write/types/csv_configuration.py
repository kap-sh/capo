"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CsvConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.boolean
    import capo_timestream_write.types.string_value1
    import capo_timestream_write.types.string_value256


class CsvConfiguration(TypedDict, closed=True):
    column_separator: NotRequired[
        "capo_timestream_write.types.string_value1.StringValue1"
    ]
    """<p>Column separator can be one of comma (','), pipe ('|), semicolon (';'), tab('/t'), or blank space (' '). </p>"""
    escape_char: NotRequired["capo_timestream_write.types.string_value1.StringValue1"]
    """<p>Escape character can be one of </p>"""
    quote_char: NotRequired["capo_timestream_write.types.string_value1.StringValue1"]
    """<p>Can be single quote (') or double quote (").</p>"""
    null_value: NotRequired[
        "capo_timestream_write.types.string_value256.StringValue256"
    ]
    """<p>Can be blank space (' ').</p>"""
    trim_white_space: NotRequired["capo_timestream_write.types.boolean.Boolean"]
    """<p>Specifies to trim leading and trailing white space.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CsvConfiguration) -> dict:
    out: dict = {}
    if "column_separator" in value:
        out["ColumnSeparator"] = value["column_separator"]
    if "escape_char" in value:
        out["EscapeChar"] = value["escape_char"]
    if "quote_char" in value:
        out["QuoteChar"] = value["quote_char"]
    if "null_value" in value:
        out["NullValue"] = value["null_value"]
    if "trim_white_space" in value:
        out["TrimWhiteSpace"] = value["trim_white_space"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CsvConfiguration:
    out: CsvConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ColumnSeparator") is not None:
        out["column_separator"] = data["ColumnSeparator"]
    if data.get("EscapeChar") is not None:
        out["escape_char"] = data["EscapeChar"]
    if data.get("QuoteChar") is not None:
        out["quote_char"] = data["QuoteChar"]
    if data.get("NullValue") is not None:
        out["null_value"] = data["NullValue"]
    if data.get("TrimWhiteSpace") is not None:
        out["trim_white_space"] = data["TrimWhiteSpace"]
    return out
