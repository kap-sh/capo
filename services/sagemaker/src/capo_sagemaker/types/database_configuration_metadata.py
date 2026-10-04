"""Generated from Smithy shape ``com.amazonaws.sagemaker#DatabaseConfigurationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.database_configuration_rollback_status


class DatabaseConfigurationMetadata(TypedDict, closed=True):
    rollback_status: NotRequired[
        "capo_sagemaker.types.database_configuration_rollback_status.DatabaseConfigurationRollbackStatus"
    ]
    """<p>Whether HyperPod restored the previous accounting database configuration after the change failed. Valid values:</p> <ul> <li> <p> <code>NotApplicable</code>: The change failed before HyperPod modified the cluster, for example because the database could not be reached or rejected the credentials, so there was nothing to restore.</p> </li> <li> <p> <code>Reverted</code>: The change failed after it was applied, and HyperPod restored the previous configuration. The cluster continues to use the previous accounting database.</p> </li> <li> <p> <code>RevertFailed</code>: The change failed and HyperPod could not restore the previous configuration, so Slurm accounting on the cluster might not be working.</p> </li> </ul> <p>This field is omitted when the change succeeds.</p>"""
    advisory: NotRequired["str"]
    """<p>Additional information about a change that succeeded, such as an action to take on the cluster.</p>"""
    failure_message: NotRequired["str"]
    """<p>An error message describing why the accounting database change failed, and how to resolve it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseConfigurationMetadata) -> dict:
    out: dict = {}
    if "rollback_status" in value:
        import capo_sagemaker.types.database_configuration_rollback_status

        out["RollbackStatus"] = (
            capo_sagemaker.types.database_configuration_rollback_status.serialize_aws_json_1_1(
                value["rollback_status"]
            )
        )
    if "advisory" in value:
        out["Advisory"] = value["advisory"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseConfigurationMetadata:
    out: DatabaseConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("RollbackStatus") is not None:
        import capo_sagemaker.types.database_configuration_rollback_status

        out["rollback_status"] = (
            capo_sagemaker.types.database_configuration_rollback_status.deserialize_aws_json_1_1(
                data["RollbackStatus"]
            )
        )
    if data.get("Advisory") is not None:
        out["advisory"] = data["Advisory"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    return out
