"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.auto_deployment
    import capo_cloudformation.types.description
    import capo_cloudformation.types.managed_execution
    import capo_cloudformation.types.permission_models
    import capo_cloudformation.types.stack_drift_status
    import capo_cloudformation.types.stack_set_id
    import capo_cloudformation.types.stack_set_name
    import capo_cloudformation.types.stack_set_status
    import capo_cloudformation.types.timestamp


class StackSetSummary(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name of the StackSet.</p>"""
    stack_set_id: NotRequired["capo_cloudformation.types.stack_set_id.StackSetId"]
    """<p>The ID of the StackSet.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A description of the StackSet that you specify when the StackSet is created or updated.</p>"""
    status: NotRequired["capo_cloudformation.types.stack_set_status.StackSetStatus"]
    """<p>The status of the StackSet.</p>"""
    auto_deployment: NotRequired[
        "capo_cloudformation.types.auto_deployment.AutoDeployment"
    ]
    """<p>[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organizational unit (OU).</p>"""
    permission_model: NotRequired[
        "capo_cloudformation.types.permission_models.PermissionModels"
    ]
    """<p>Describes how the IAM roles required for StackSet operations are created.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html">Activate trusted access for StackSets with Organizations</a>.</p> </li> </ul>"""
    drift_status: NotRequired[
        "capo_cloudformation.types.stack_drift_status.StackDriftStatus"
    ]
    """<p>Status of the StackSet's actual configuration compared to its expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the StackSet differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the StackSet for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All the stack instances belonging to the StackSet match the expected template and parameter configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>"""
    last_drift_check_timestamp: NotRequired[
        "capo_cloudformation.types.timestamp.Timestamp"
    ]
    """<p>Most recent time when CloudFormation performed a drift detection operation on the StackSet. This value will be <code>NULL</code> for any StackSet that drift detection hasn't yet been performed on.</p>"""
    managed_execution: NotRequired[
        "capo_cloudformation.types.managed_execution.ManagedExecution"
    ]
    """<p>Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "stack_set_id" in value:
        pairs.append((f"{key_prefix}StackSetId", str(value["stack_set_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "status" in value:
        import capo_cloudformation.types.stack_set_status

        capo_cloudformation.types.stack_set_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "auto_deployment" in value:
        import capo_cloudformation.types.auto_deployment

        capo_cloudformation.types.auto_deployment.serialize_query(
            value["auto_deployment"], pairs, f"{key_prefix}AutoDeployment"
        )
    if "permission_model" in value:
        import capo_cloudformation.types.permission_models

        capo_cloudformation.types.permission_models.serialize_query(
            value["permission_model"], pairs, f"{key_prefix}PermissionModel"
        )
    if "drift_status" in value:
        import capo_cloudformation.types.stack_drift_status

        capo_cloudformation.types.stack_drift_status.serialize_query(
            value["drift_status"], pairs, f"{key_prefix}DriftStatus"
        )
    if "last_drift_check_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_drift_check_timestamp"],
            pairs,
            f"{key_prefix}LastDriftCheckTimestamp",
        )
    if "managed_execution" in value:
        import capo_cloudformation.types.managed_execution

        capo_cloudformation.types.managed_execution.serialize_query(
            value["managed_execution"], pairs, f"{key_prefix}ManagedExecution"
        )


def deserialize_query(el: Element) -> StackSetSummary:
    out: StackSetSummary = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_stack_set_id = el.find("StackSetId")
    if child_stack_set_id is not None:
        out["stack_set_id"] = str(child_stack_set_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stack_set_status

        out["status"] = capo_cloudformation.types.stack_set_status.deserialize_query(
            child_status
        )
    child_auto_deployment = el.find("AutoDeployment")
    if child_auto_deployment is not None:
        import capo_cloudformation.types.auto_deployment

        out["auto_deployment"] = (
            capo_cloudformation.types.auto_deployment.deserialize_query(
                child_auto_deployment
            )
        )
    child_permission_model = el.find("PermissionModel")
    if child_permission_model is not None:
        import capo_cloudformation.types.permission_models

        out["permission_model"] = (
            capo_cloudformation.types.permission_models.deserialize_query(
                child_permission_model
            )
        )
    child_drift_status = el.find("DriftStatus")
    if child_drift_status is not None:
        import capo_cloudformation.types.stack_drift_status

        out["drift_status"] = (
            capo_cloudformation.types.stack_drift_status.deserialize_query(
                child_drift_status
            )
        )
    child_last_drift_check_timestamp = el.find("LastDriftCheckTimestamp")
    if child_last_drift_check_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["last_drift_check_timestamp"] = (
            capo_cloudformation.types.timestamp.deserialize_query(
                child_last_drift_check_timestamp
            )
        )
    child_managed_execution = el.find("ManagedExecution")
    if child_managed_execution is not None:
        import capo_cloudformation.types.managed_execution

        out["managed_execution"] = (
            capo_cloudformation.types.managed_execution.deserialize_query(
                child_managed_execution
            )
        )
    return out
