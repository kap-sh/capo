"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CopyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.copy_value_entries


class CopyValue(TypedDict, closed=True):
    entries: "capo_cloudwatch_logs.types.copy_value_entries.CopyValueEntries"
    """<p>An array of <code>CopyValueEntry</code> objects, where each object contains the information about one field value to copy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyValue) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.copy_value_entries

    out["entries"] = (
        capo_cloudwatch_logs.types.copy_value_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyValue:
    out: CopyValue = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_cloudwatch_logs.types.copy_value_entries

        out["entries"] = (
            capo_cloudwatch_logs.types.copy_value_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
