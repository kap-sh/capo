"""Generated from Smithy shape ``com.amazonaws.athena#S3LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.kms_key
    import capo_athena.types.s3_output_location


class S3LoggingConfiguration(TypedDict, closed=True):
    enabled: "capo_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Enables S3 log delivery.</p>"""
    kms_key: NotRequired["capo_athena.types.kms_key.KmsKey"]
    """<p>The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.</p>"""
    log_location: NotRequired["capo_athena.types.s3_output_location.S3OutputLocation"]
    """<p>The Amazon S3 destination URI for log publishing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3LoggingConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "log_location" in value:
        out["LogLocation"] = value["log_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3LoggingConfiguration:
    out: S3LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    if data.get("LogLocation") is not None:
        out["log_location"] = data["LogLocation"]
    return out
