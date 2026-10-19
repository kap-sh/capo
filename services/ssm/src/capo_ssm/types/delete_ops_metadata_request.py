"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteOpsMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_metadata_arn


class DeleteOpsMetadataRequest(TypedDict, closed=True):
    ops_metadata_arn: "capo_ssm.types.ops_metadata_arn.OpsMetadataArn"
    """<p>The Amazon Resource Name (ARN) of an OpsMetadata Object to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOpsMetadataRequest) -> dict:
    out: dict = {}
    out["OpsMetadataArn"] = value["ops_metadata_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOpsMetadataRequest:
    out: DeleteOpsMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsMetadataArn") is not None:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    else:
        out["ops_metadata_arn"] = ""
    return out
