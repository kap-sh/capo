"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CSVMappingParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.record_column_delimiter
    import capo_kinesis_analytics.types.record_row_delimiter


class CSVMappingParameters(TypedDict, closed=True):
    record_row_delimiter: (
        "capo_kinesis_analytics.types.record_row_delimiter.RecordRowDelimiter"
    )
    r"""<p>Row delimiter. For example, in a CSV format, <i>'\n'</i> is the typical row delimiter.</p>"""
    record_column_delimiter: (
        "capo_kinesis_analytics.types.record_column_delimiter.RecordColumnDelimiter"
    )
    """<p>Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CSVMappingParameters) -> dict:
    out: dict = {}
    out["RecordRowDelimiter"] = value["record_row_delimiter"]
    out["RecordColumnDelimiter"] = value["record_column_delimiter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CSVMappingParameters:
    out: CSVMappingParameters = {}  # type: ignore[typeddict-item]
    if data.get("RecordRowDelimiter") is not None:
        out["record_row_delimiter"] = data["RecordRowDelimiter"]
    else:
        raise DeserializationError("CSVMappingParameters.record_row_delimiter required")
    if data.get("RecordColumnDelimiter") is not None:
        out["record_column_delimiter"] = data["RecordColumnDelimiter"]
    else:
        raise DeserializationError(
            "CSVMappingParameters.record_column_delimiter required"
        )
    return out
