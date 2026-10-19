"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SubstituteString``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.substitute_string_entries


class SubstituteString(TypedDict, closed=True):
    entries: (
        "capo_cloudwatch_logs.types.substitute_string_entries.SubstituteStringEntries"
    )
    """<p>An array of objects, where each object contains the information about one key to match and replace. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubstituteString) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.substitute_string_entries

    out["entries"] = (
        capo_cloudwatch_logs.types.substitute_string_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubstituteString:
    out: SubstituteString = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_cloudwatch_logs.types.substitute_string_entries

        out["entries"] = (
            capo_cloudwatch_logs.types.substitute_string_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
