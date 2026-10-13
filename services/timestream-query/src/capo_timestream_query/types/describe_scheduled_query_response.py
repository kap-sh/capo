"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeScheduledQueryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.scheduled_query_description


class DescribeScheduledQueryResponse(TypedDict, closed=True):
    scheduled_query: "capo_timestream_query.types.scheduled_query_description.ScheduledQueryDescription"
    """<p>The scheduled query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeScheduledQueryResponse) -> dict:
    out: dict = {}
    import capo_timestream_query.types.scheduled_query_description

    out["ScheduledQuery"] = (
        capo_timestream_query.types.scheduled_query_description.serialize_aws_json_1_0(
            value["scheduled_query"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeScheduledQueryResponse:
    out: DescribeScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledQuery") is not None:
        import capo_timestream_query.types.scheduled_query_description

        out["scheduled_query"] = (
            capo_timestream_query.types.scheduled_query_description.deserialize_aws_json_1_0(
                data["ScheduledQuery"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeScheduledQueryResponse.scheduled_query required"
        )
    return out


def redact_sensitive(value: DescribeScheduledQueryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scheduled_query" in value:
        import capo_timestream_query.types.scheduled_query_description

        out["scheduled_query"] = (
            capo_timestream_query.types.scheduled_query_description.redact_sensitive(
                value["scheduled_query"]
            )
        )
    return out
