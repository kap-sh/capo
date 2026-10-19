"""Generated from Smithy shape ``com.amazonaws.firehose#PartitionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.non_empty_string_without_whitespace


class PartitionField(TypedDict, closed=True):
    source_name: "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    """<p> The column name to be configured in partition spec. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionField) -> dict:
    out: dict = {}
    out["SourceName"] = value["source_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionField:
    out: PartitionField = {}  # type: ignore[typeddict-item]
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    else:
        out["source_name"] = ""
    return out
