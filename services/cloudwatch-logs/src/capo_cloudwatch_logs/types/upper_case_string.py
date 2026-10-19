"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpperCaseString``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.upper_case_string_with_keys


class UpperCaseString(TypedDict, closed=True):
    with_keys: (
        "capo_cloudwatch_logs.types.upper_case_string_with_keys.UpperCaseStringWithKeys"
    )
    """<p>The array of containing the keys of the field to convert to uppercase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpperCaseString) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.upper_case_string_with_keys

    out["withKeys"] = (
        capo_cloudwatch_logs.types.upper_case_string_with_keys.serialize_aws_json_1_1(
            value["with_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpperCaseString:
    out: UpperCaseString = {}  # type: ignore[typeddict-item]
    if data.get("withKeys") is not None:
        import capo_cloudwatch_logs.types.upper_case_string_with_keys

        out["with_keys"] = (
            capo_cloudwatch_logs.types.upper_case_string_with_keys.deserialize_aws_json_1_1(
                data["withKeys"]
            )
        )
    else:
        out["with_keys"] = []
    return out
