"""Generated from Smithy shape ``com.amazonaws.firehose#CopyCommand``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.copy_options
    import capo_firehose.types.data_table_columns
    import capo_firehose.types.data_table_name


class CopyCommand(TypedDict, closed=True):
    data_table_name: "capo_firehose.types.data_table_name.DataTableName"
    """<p>The name of the target table. The table must already exist in the database.</p>"""
    data_table_columns: NotRequired[
        "capo_firehose.types.data_table_columns.DataTableColumns"
    ]
    """<p>A comma-separated list of column names.</p>"""
    copy_options: NotRequired["capo_firehose.types.copy_options.CopyOptions"]
    r"""<p>Optional parameters to use with the Amazon Redshift <code>COPY</code> command. For more information, see the "Optional Parameters" section of <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html">Amazon Redshift COPY command</a>. Some possible examples that would apply to Firehose are as follows:</p> <p> <code>delimiter '\t' lzop;</code> - fields are delimited with "\t" (TAB character) and compressed using lzop.</p> <p> <code>delimiter '|'</code> - fields are delimited with "|" (this is the default delimiter).</p> <p> <code>delimiter '|' escape</code> - the delimiter should be escaped.</p> <p> <code>fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'</code> - fields are fixed width in the source, with each width specified after every column in the table.</p> <p> <code>JSON 's3://mybucket/jsonpaths.txt'</code> - data is in JSON format, and the path specified is the format of the data.</p> <p>For more examples, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html">Amazon Redshift COPY command examples</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyCommand) -> dict:
    out: dict = {}
    out["DataTableName"] = value["data_table_name"]
    if "data_table_columns" in value:
        out["DataTableColumns"] = value["data_table_columns"]
    if "copy_options" in value:
        out["CopyOptions"] = value["copy_options"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyCommand:
    out: CopyCommand = {}  # type: ignore[typeddict-item]
    if data.get("DataTableName") is not None:
        out["data_table_name"] = data["DataTableName"]
    else:
        raise DeserializationError("CopyCommand.data_table_name required")
    if data.get("DataTableColumns") is not None:
        out["data_table_columns"] = data["DataTableColumns"]
    if data.get("CopyOptions") is not None:
        out["copy_options"] = data["CopyOptions"]
    return out
