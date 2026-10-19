"""Generated from Smithy shape ``com.amazonaws.odb#InitializeServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.access


class InitializeServiceInput(TypedDict, closed=True):
    oci_identity_domain: NotRequired["bool"]
    """<p>The Oracle Cloud Infrastructure (OCI) identity domain configuration for service initialization.</p>"""
    autonomous_database_oci_aws_secrets_manager_integration: NotRequired[
        "capo_odb.types.access.Access"
    ]
    """<p>Specifies whether to enable or disable the OCI service-account role for Amazon Web Services Secrets Manager integration with Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InitializeServiceInput) -> dict:
    out: dict = {}
    if "oci_identity_domain" in value:
        out["ociIdentityDomain"] = value["oci_identity_domain"]
    if "autonomous_database_oci_aws_secrets_manager_integration" in value:
        import capo_odb.types.access

        out["autonomousDatabaseOciAwsSecretsManagerIntegration"] = (
            capo_odb.types.access.serialize_aws_json_1_0(
                value["autonomous_database_oci_aws_secrets_manager_integration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InitializeServiceInput:
    out: InitializeServiceInput = {}  # type: ignore[typeddict-item]
    if data.get("ociIdentityDomain") is not None:
        out["oci_identity_domain"] = data["ociIdentityDomain"]
    if data.get("autonomousDatabaseOciAwsSecretsManagerIntegration") is not None:
        import capo_odb.types.access

        out["autonomous_database_oci_aws_secrets_manager_integration"] = (
            capo_odb.types.access.deserialize_aws_json_1_0(
                data["autonomousDatabaseOciAwsSecretsManagerIntegration"]
            )
        )
    return out
