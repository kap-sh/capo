"""Generated from Smithy shape ``com.amazonaws.firehose#HiveJsonSerDe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.list_of_non_empty_strings


class HiveJsonSerDe(TypedDict, closed=True):
    timestamp_formats: NotRequired[
        "capo_firehose.types.list_of_non_empty_strings.ListOfNonEmptyStrings"
    ]
    """<p>Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see <a href="https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html">Class DateTimeFormat</a>. You can also use the special value <code>millis</code> to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses <code>java.sql.Timestamp::valueOf</code> by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HiveJsonSerDe) -> dict:
    out: dict = {}
    if "timestamp_formats" in value:
        import capo_firehose.types.list_of_non_empty_strings

        out["TimestampFormats"] = (
            capo_firehose.types.list_of_non_empty_strings.serialize_aws_json_1_1(
                value["timestamp_formats"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HiveJsonSerDe:
    out: HiveJsonSerDe = {}  # type: ignore[typeddict-item]
    if data.get("TimestampFormats") is not None:
        import capo_firehose.types.list_of_non_empty_strings

        out["timestamp_formats"] = (
            capo_firehose.types.list_of_non_empty_strings.deserialize_aws_json_1_1(
                data["TimestampFormats"]
            )
        )
    return out
