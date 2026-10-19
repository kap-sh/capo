"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AddKeys``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.add_key_entries


class AddKeys(TypedDict, closed=True):
    entries: "capo_cloudwatch_logs.types.add_key_entries.AddKeyEntries"
    """<p>An array of objects, where each object contains the information about one key to add to the log event. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddKeys) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.add_key_entries

    out["entries"] = capo_cloudwatch_logs.types.add_key_entries.serialize_aws_json_1_1(
        value["entries"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddKeys:
    out: AddKeys = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_cloudwatch_logs.types.add_key_entries

        out["entries"] = (
            capo_cloudwatch_logs.types.add_key_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
