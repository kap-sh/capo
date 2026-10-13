"""Generated from Smithy shape ``com.amazonaws.datazone#SparkEmrPropertiesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.governance_type
    import capo_datazone.types.managed_endpoint_credentials
    import capo_datazone.types.username_password


class SparkEmrPropertiesOutput(TypedDict, closed=True):
    compute_arn: NotRequired["str"]
    """<p>The compute ARN of the Spark EMR.</p>"""
    credentials: NotRequired["capo_datazone.types.username_password.UsernamePassword"]
    """<p>The credentials of the Spark EMR.</p>"""
    credentials_expiration: NotRequired["datetime.datetime"]
    """<p>The credential expiration of the Spark EMR.</p>"""
    governance_type: NotRequired["capo_datazone.types.governance_type.GovernanceType"]
    """<p>The governance type of the Spark EMR.</p>"""
    instance_profile_arn: NotRequired["str"]
    """<p>The instance profile ARN of the Spark EMR.</p>"""
    java_virtual_env: NotRequired["str"]
    """<p>The Java virtual env of the Spark EMR.</p>"""
    livy_endpoint: NotRequired["str"]
    """<p>The livy endpoint of the Spark EMR.</p>"""
    log_uri: NotRequired["str"]
    """<p>The log URI of the Spark EMR.</p>"""
    python_virtual_env: NotRequired["str"]
    """<p>The Python virtual env of the Spark EMR.</p>"""
    runtime_role: NotRequired["str"]
    """<p>The runtime role of the Spark EMR.</p>"""
    trusted_certificates_s3_uri: NotRequired["str"]
    """<p>The trusted certificate S3 URL of the Spark EMR.</p>"""
    certificate_data: NotRequired["str"]
    """<p>The certificate data of the EMR on EKS cluster.</p>"""
    managed_endpoint_arn: NotRequired["str"]
    """<p>The managed endpoint ARN of the EMR on EKS cluster.</p>"""
    managed_endpoint_credentials: NotRequired[
        "capo_datazone.types.managed_endpoint_credentials.ManagedEndpointCredentials"
    ]
    """<p>The managed endpoint credentials of the EMR on EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkEmrPropertiesOutput) -> dict:
    out: dict = {}
    if "compute_arn" in value:
        out["computeArn"] = value["compute_arn"]
    if "credentials" in value:
        import capo_datazone.types.username_password

        out["credentials"] = capo_datazone.types.username_password.serialize_json(
            value["credentials"]
        )
    if "credentials_expiration" in value:
        import capo_datazone._protocol.serialize

        out["credentialsExpiration"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["credentials_expiration"]
        )
    if "governance_type" in value:
        import capo_datazone.types.governance_type

        out["governanceType"] = capo_datazone.types.governance_type.serialize_json(
            value["governance_type"]
        )
    if "instance_profile_arn" in value:
        out["instanceProfileArn"] = value["instance_profile_arn"]
    if "java_virtual_env" in value:
        out["javaVirtualEnv"] = value["java_virtual_env"]
    if "livy_endpoint" in value:
        out["livyEndpoint"] = value["livy_endpoint"]
    if "log_uri" in value:
        out["logUri"] = value["log_uri"]
    if "python_virtual_env" in value:
        out["pythonVirtualEnv"] = value["python_virtual_env"]
    if "runtime_role" in value:
        out["runtimeRole"] = value["runtime_role"]
    if "trusted_certificates_s3_uri" in value:
        out["trustedCertificatesS3Uri"] = value["trusted_certificates_s3_uri"]
    if "certificate_data" in value:
        out["certificateData"] = value["certificate_data"]
    if "managed_endpoint_arn" in value:
        out["managedEndpointArn"] = value["managed_endpoint_arn"]
    if "managed_endpoint_credentials" in value:
        import capo_datazone.types.managed_endpoint_credentials

        out["managedEndpointCredentials"] = (
            capo_datazone.types.managed_endpoint_credentials.serialize_json(
                value["managed_endpoint_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> SparkEmrPropertiesOutput:
    out: SparkEmrPropertiesOutput = {}  # type: ignore[typeddict-item]
    if data.get("computeArn") is not None:
        out["compute_arn"] = data["computeArn"]
    if data.get("credentials") is not None:
        import capo_datazone.types.username_password

        out["credentials"] = capo_datazone.types.username_password.deserialize_json(
            data["credentials"]
        )
    if data.get("credentialsExpiration") is not None:
        import datetime

        out["credentials_expiration"] = datetime.datetime.fromisoformat(
            data["credentialsExpiration"].replace("Z", "+00:00")
        )
    if data.get("governanceType") is not None:
        import capo_datazone.types.governance_type

        out["governance_type"] = capo_datazone.types.governance_type.deserialize_json(
            data["governanceType"]
        )
    if data.get("instanceProfileArn") is not None:
        out["instance_profile_arn"] = data["instanceProfileArn"]
    if data.get("javaVirtualEnv") is not None:
        out["java_virtual_env"] = data["javaVirtualEnv"]
    if data.get("livyEndpoint") is not None:
        out["livy_endpoint"] = data["livyEndpoint"]
    if data.get("logUri") is not None:
        out["log_uri"] = data["logUri"]
    if data.get("pythonVirtualEnv") is not None:
        out["python_virtual_env"] = data["pythonVirtualEnv"]
    if data.get("runtimeRole") is not None:
        out["runtime_role"] = data["runtimeRole"]
    if data.get("trustedCertificatesS3Uri") is not None:
        out["trusted_certificates_s3_uri"] = data["trustedCertificatesS3Uri"]
    if data.get("certificateData") is not None:
        out["certificate_data"] = data["certificateData"]
    if data.get("managedEndpointArn") is not None:
        out["managed_endpoint_arn"] = data["managedEndpointArn"]
    if data.get("managedEndpointCredentials") is not None:
        import capo_datazone.types.managed_endpoint_credentials

        out["managed_endpoint_credentials"] = (
            capo_datazone.types.managed_endpoint_credentials.deserialize_json(
                data["managedEndpointCredentials"]
            )
        )
    return out


def redact_sensitive(value: SparkEmrPropertiesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    if "managed_endpoint_credentials" in value:
        out["managed_endpoint_credentials"] = "*** Sensitive Data Redacted ***"
    return out
