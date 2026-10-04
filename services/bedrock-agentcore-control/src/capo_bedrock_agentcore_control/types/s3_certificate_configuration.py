"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3CertificateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificate_bucket_owner_account_id
    import capo_bedrock_agentcore_control.types.certificate_s3_uri


class S3CertificateConfiguration(TypedDict, closed=True):
    uri: "capo_bedrock_agentcore_control.types.certificate_s3_uri.CertificateS3Uri"
    """<p>The URI of the Amazon S3 object that contains the PEM-encoded certificate.</p>"""
    bucket_owner_account_id: NotRequired[
        "capo_bedrock_agentcore_control.types.certificate_bucket_owner_account_id.CertificateBucketOwnerAccountId"
    ]
    """<p>The account ID of the Amazon S3 bucket owner. This ID is used for cross-account access to the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3CertificateConfiguration) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    if "bucket_owner_account_id" in value:
        out["bucketOwnerAccountId"] = value["bucket_owner_account_id"]
    return out


def deserialize_json(data: dict) -> S3CertificateConfiguration:
    out: S3CertificateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("S3CertificateConfiguration.uri required")
    if data.get("bucketOwnerAccountId") is not None:
        out["bucket_owner_account_id"] = data["bucketOwnerAccountId"]
    return out
