"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationAzureBlobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.location_arn


class DescribeLocationAzureBlobRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of your Azure Blob Storage transfer location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationAzureBlobRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationAzureBlobRequest:
    out: DescribeLocationAzureBlobRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        out["location_arn"] = ""
    return out
