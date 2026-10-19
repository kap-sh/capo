"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SplitStringEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.source
    import capo_cloudwatch_logs.types.split_string_delimiter


class SplitStringEntry(TypedDict, closed=True):
    source: "capo_cloudwatch_logs.types.source.Source"
    """<p>The key of the field to split.</p>"""
    delimiter: "capo_cloudwatch_logs.types.split_string_delimiter.SplitStringDelimiter"
    """<p>The separator characters to split the string entry on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitStringEntry) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["delimiter"] = value["delimiter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitStringEntry:
    out: SplitStringEntry = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("delimiter") is not None:
        out["delimiter"] = data["delimiter"]
    else:
        out["delimiter"] = ""
    return out
