"""Generated from Smithy shape ``com.amazonaws.timestreamquery#CreateScheduledQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name


class CreateScheduledQueryResponse(TypedDict, closed=True):
    arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>ARN for the created scheduled query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateScheduledQueryResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateScheduledQueryResponse:
    out: CreateScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
