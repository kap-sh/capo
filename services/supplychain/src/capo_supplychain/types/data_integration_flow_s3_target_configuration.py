"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowS3TargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_s3_options
    import capo_supplychain.types.data_integration_flow_s3_prefix
    import capo_supplychain.types.s3_bucket_name


class DataIntegrationFlowS3TargetConfiguration(TypedDict, closed=True):
    bucket_name: "capo_supplychain.types.s3_bucket_name.S3BucketName"
    """<p>The bucketName of the S3 target objects.</p>"""
    prefix: "capo_supplychain.types.data_integration_flow_s3_prefix.DataIntegrationFlowS3Prefix"
    """<p>The prefix of the S3 target objects.</p>"""
    options: NotRequired[
        "capo_supplychain.types.data_integration_flow_s3_options.DataIntegrationFlowS3Options"
    ]
    """<p>The S3 DataIntegrationFlow target options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowS3TargetConfiguration) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["prefix"] = value["prefix"]
    if "options" in value:
        import capo_supplychain.types.data_integration_flow_s3_options

        out["options"] = (
            capo_supplychain.types.data_integration_flow_s3_options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowS3TargetConfiguration:
    out: DataIntegrationFlowS3TargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("options") is not None:
        import capo_supplychain.types.data_integration_flow_s3_options

        out["options"] = (
            capo_supplychain.types.data_integration_flow_s3_options.deserialize_json(
                data["options"]
            )
        )
    return out
