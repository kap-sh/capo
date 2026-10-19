"""Generated from Smithy shape ``com.amazonaws.glue#CreateCsvClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.csv_column_delimiter
    import capo_glue.types.csv_header
    import capo_glue.types.csv_header_option
    import capo_glue.types.csv_quote_symbol
    import capo_glue.types.csv_serde_option
    import capo_glue.types.custom_datatypes
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean


class CreateCsvClassifierRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    delimiter: NotRequired["capo_glue.types.csv_column_delimiter.CsvColumnDelimiter"]
    """<p>A custom symbol to denote what separates each column entry in the row.</p>"""
    quote_symbol: NotRequired["capo_glue.types.csv_quote_symbol.CsvQuoteSymbol"]
    """<p>A custom symbol to denote what combines content into a single column value. Must be different from the column delimiter.</p>"""
    contains_header: NotRequired["capo_glue.types.csv_header_option.CsvHeaderOption"]
    """<p>Indicates whether the CSV file contains a header.</p>"""
    header: NotRequired["capo_glue.types.csv_header.CsvHeader"]
    """<p>A list of strings representing column names.</p>"""
    disable_value_trimming: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies not to trim values before identifying the type of column values. The default value is true.</p>"""
    allow_single_column: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Enables the processing of files that contain only one column.</p>"""
    custom_datatype_configured: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables the configuration of custom datatypes.</p>"""
    custom_datatypes: NotRequired["capo_glue.types.custom_datatypes.CustomDatatypes"]
    """<p>Creates a list of supported custom datatypes.</p>"""
    serde: NotRequired["capo_glue.types.csv_serde_option.CsvSerdeOption"]
    """<p>Sets the SerDe for processing CSV in the classifier, which will be applied in the Data Catalog. Valid values are <code>OpenCSVSerDe</code>, <code>LazySimpleSerDe</code>, and <code>None</code>. You can specify the <code>None</code> value when you want the crawler to do the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCsvClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "quote_symbol" in value:
        out["QuoteSymbol"] = value["quote_symbol"]
    if "contains_header" in value:
        import capo_glue.types.csv_header_option

        out["ContainsHeader"] = (
            capo_glue.types.csv_header_option.serialize_aws_json_1_1(
                value["contains_header"]
            )
        )
    if "header" in value:
        import capo_glue.types.csv_header

        out["Header"] = capo_glue.types.csv_header.serialize_aws_json_1_1(
            value["header"]
        )
    if "disable_value_trimming" in value:
        out["DisableValueTrimming"] = value["disable_value_trimming"]
    if "allow_single_column" in value:
        out["AllowSingleColumn"] = value["allow_single_column"]
    if "custom_datatype_configured" in value:
        out["CustomDatatypeConfigured"] = value["custom_datatype_configured"]
    if "custom_datatypes" in value:
        import capo_glue.types.custom_datatypes

        out["CustomDatatypes"] = (
            capo_glue.types.custom_datatypes.serialize_aws_json_1_1(
                value["custom_datatypes"]
            )
        )
    if "serde" in value:
        import capo_glue.types.csv_serde_option

        out["Serde"] = capo_glue.types.csv_serde_option.serialize_aws_json_1_1(
            value["serde"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCsvClassifierRequest:
    out: CreateCsvClassifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Delimiter") is not None:
        out["delimiter"] = data["Delimiter"]
    if data.get("QuoteSymbol") is not None:
        out["quote_symbol"] = data["QuoteSymbol"]
    if data.get("ContainsHeader") is not None:
        import capo_glue.types.csv_header_option

        out["contains_header"] = (
            capo_glue.types.csv_header_option.deserialize_aws_json_1_1(
                data["ContainsHeader"]
            )
        )
    if data.get("Header") is not None:
        import capo_glue.types.csv_header

        out["header"] = capo_glue.types.csv_header.deserialize_aws_json_1_1(
            data["Header"]
        )
    if data.get("DisableValueTrimming") is not None:
        out["disable_value_trimming"] = data["DisableValueTrimming"]
    if data.get("AllowSingleColumn") is not None:
        out["allow_single_column"] = data["AllowSingleColumn"]
    if data.get("CustomDatatypeConfigured") is not None:
        out["custom_datatype_configured"] = data["CustomDatatypeConfigured"]
    if data.get("CustomDatatypes") is not None:
        import capo_glue.types.custom_datatypes

        out["custom_datatypes"] = (
            capo_glue.types.custom_datatypes.deserialize_aws_json_1_1(
                data["CustomDatatypes"]
            )
        )
    if data.get("Serde") is not None:
        import capo_glue.types.csv_serde_option

        out["serde"] = capo_glue.types.csv_serde_option.deserialize_aws_json_1_1(
            data["Serde"]
        )
    return out
