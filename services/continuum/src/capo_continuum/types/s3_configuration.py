"""Generated from Smithy shape ``com.amazonaws.continuum#S3Configuration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_s3_bucket_name
    import capo_continuum.types.integration_s3_external_id
    import capo_continuum.types.integration_s3_role_arn


class S3Configuration(TypedDict, closed=True):
    bucket: "capo_continuum.types.integration_s3_bucket_name.IntegrationS3BucketName"
    """Customer-managed source bucket name."""
    role_arn: "capo_continuum.types.integration_s3_role_arn.IntegrationS3RoleArn"
    """Role Continuum will assume to read from the source bucket."""
    external_id: (
        "capo_continuum.types.integration_s3_external_id.IntegrationS3ExternalId"
    )
    """Caller-provided external ID required by the role trust policy."""


# --- restJson1 ser/de ---
def serialize_json(value: S3Configuration) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["roleArn"] = value["role_arn"]
    out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    else:
        out["external_id"] = ""
    return out


def redact_sensitive(value: S3Configuration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "external_id" in value:
        out["external_id"] = "*** Sensitive Data Redacted ***"
    return out
