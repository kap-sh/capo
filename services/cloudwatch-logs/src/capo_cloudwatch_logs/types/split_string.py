"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SplitString``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.split_string_entries


class SplitString(TypedDict, closed=True):
    entries: "capo_cloudwatch_logs.types.split_string_entries.SplitStringEntries"
    """<p>An array of <code>SplitStringEntry</code> objects, where each object contains the information about one field to split. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitString) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.split_string_entries

    out["entries"] = (
        capo_cloudwatch_logs.types.split_string_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitString:
    out: SplitString = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_cloudwatch_logs.types.split_string_entries

        out["entries"] = (
            capo_cloudwatch_logs.types.split_string_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
