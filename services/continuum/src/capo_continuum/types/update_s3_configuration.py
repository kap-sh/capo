"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateS3Configuration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_s3_external_id
    import capo_continuum.types.integration_s3_role_arn


class UpdateS3Configuration(TypedDict, closed=True):
    role_arn: "capo_continuum.types.integration_s3_role_arn.IntegrationS3RoleArn"
    """The role to use. Supply the current role when rotating only the external ID. The caller must be allowed to pass this exact role to Continuum."""
    external_id: NotRequired[
        "capo_continuum.types.integration_s3_external_id.IntegrationS3ExternalId"
    ]
    """The replacement external ID used when assuming the supplied role. If omitted, the existing external ID is preserved. This value is sensitive and is never included in the public integration response."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateS3Configuration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> UpdateS3Configuration:
    out: UpdateS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    return out


def redact_sensitive(value: UpdateS3Configuration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "external_id" in value:
        out["external_id"] = "*** Sensitive Data Redacted ***"
    return out
