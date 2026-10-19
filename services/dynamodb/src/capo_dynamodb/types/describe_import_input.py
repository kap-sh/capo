"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeImportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.import_arn


class DescribeImportInput(TypedDict, closed=True):
    import_arn: "capo_dynamodb.types.import_arn.ImportArn"
    """<p> The Amazon Resource Name (ARN) associated with the table you're importing to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeImportInput) -> dict:
    out: dict = {}
    out["ImportArn"] = value["import_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeImportInput:
    out: DescribeImportInput = {}  # type: ignore[typeddict-item]
    if data.get("ImportArn") is not None:
        out["import_arn"] = data["ImportArn"]
    else:
        out["import_arn"] = ""
    return out
