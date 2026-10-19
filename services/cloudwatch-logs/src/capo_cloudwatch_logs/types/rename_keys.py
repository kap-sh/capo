"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RenameKeys``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.rename_key_entries


class RenameKeys(TypedDict, closed=True):
    entries: "capo_cloudwatch_logs.types.rename_key_entries.RenameKeyEntries"
    """<p>An array of <code>RenameKeyEntry</code> objects, where each object contains the information about a single key to rename. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameKeys) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.rename_key_entries

    out["entries"] = (
        capo_cloudwatch_logs.types.rename_key_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenameKeys:
    out: RenameKeys = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_cloudwatch_logs.types.rename_key_entries

        out["entries"] = (
            capo_cloudwatch_logs.types.rename_key_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
