"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteLookupTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn


class DeleteLookupTableRequest(TypedDict, closed=True):
    lookup_table_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the lookup table to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLookupTableRequest) -> dict:
    out: dict = {}
    out["lookupTableArn"] = value["lookup_table_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLookupTableRequest:
    out: DeleteLookupTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("lookupTableArn") is not None:
        out["lookup_table_arn"] = data["lookupTableArn"]
    else:
        out["lookup_table_arn"] = ""
    return out
