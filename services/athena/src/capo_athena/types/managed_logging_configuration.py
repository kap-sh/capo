"""Generated from Smithy shape ``com.amazonaws.athena#ManagedLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.kms_key


class ManagedLoggingConfiguration(TypedDict, closed=True):
    enabled: "capo_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Enables mamanged log persistence.</p>"""
    kms_key: NotRequired["capo_athena.types.kms_key.KmsKey"]
    """<p>The KMS key ARN to encrypt the logs stored in managed log persistence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLoggingConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedLoggingConfiguration:
    out: ManagedLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    return out
