"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.organizational_unit_id
    import capo_cloudformation.types.reason
    import capo_cloudformation.types.region
    import capo_cloudformation.types.stack_drift_status
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_instance_comprehensive_status
    import capo_cloudformation.types.stack_instance_status
    import capo_cloudformation.types.stack_set_id
    import capo_cloudformation.types.timestamp


class StackInstanceSummary(TypedDict, closed=True):
    stack_set_id: NotRequired["capo_cloudformation.types.stack_set_id.StackSetId"]
    """<p>The name or unique ID of the StackSet that the stack instance is associated with.</p>"""
    region: NotRequired["capo_cloudformation.types.region.Region"]
    """<p>The name of the Amazon Web Services Region that the stack instance is associated with.</p>"""
    account: NotRequired["capo_cloudformation.types.account.Account"]
    """<p>[Self-managed permissions] The name of the Amazon Web Services account that the stack instance is associated with.</p>"""
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The ID of the stack instance.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.stack_instance_status.StackInstanceStatus"
    ]
    """<p>The status of the stack instance, in terms of its synchronization with its associated stack set.</p> <ul> <li> <p> <code>INOPERABLE</code>: A <code>DeleteStackInstances</code> operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further <code>UpdateStackSet</code> operations. You might need to perform a <code>DeleteStackInstances</code> operation, with <code>RetainStacks</code> set to <code>true</code>, to delete the stack instance, and then delete the stack manually. <code>INOPERABLE</code> can be returned here when the cause is a failed import. If it's due to a failed import, the operation can be retried once the failures are fixed. To see if this is due to a failed import, call the <a>DescribeStackInstance</a> API operation, look at the <code>DetailedStatus</code> member returned in the <code>StackInstanceSummary</code> member.</p> </li> <li> <p> <code>OUTDATED</code>: The stack isn't currently up to date with the StackSet because:</p> <ul> <li> <p>The associated stack failed during a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation.</p> </li> <li> <p>The stack was part of a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation that failed or was stopped before the stack was created or updated.</p> </li> </ul> </li> <li> <p> <code>CURRENT</code>: The stack is currently up to date with the StackSet.</p> </li> </ul>"""
    status_reason: NotRequired["capo_cloudformation.types.reason.Reason"]
    """<p>The explanation for the specific status code assigned to this stack instance.</p>"""
    stack_instance_status: NotRequired[
        "capo_cloudformation.types.stack_instance_comprehensive_status.StackInstanceComprehensiveStatus"
    ]
    """<p>The detailed status of the stack instance.</p>"""
    organizational_unit_id: NotRequired[
        "capo_cloudformation.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.</p>"""
    drift_status: NotRequired[
        "capo_cloudformation.types.stack_drift_status.StackDriftStatus"
    ]
    """<p>Status of the stack instance's actual configuration compared to the expected template and parameter configuration of the StackSet it belongs to.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from the expected template and parameter configuration of the StackSet it belongs to. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack instance differs from its expected StackSet configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack instance's actual configuration matches its expected StackSet configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>"""
    last_drift_check_timestamp: NotRequired[
        "capo_cloudformation.types.timestamp.Timestamp"
    ]
    """<p>Most recent time when CloudFormation performed a drift detection operation on the stack instance. This value will be <code>NULL</code> for any stack instance that drift detection hasn't yet been performed on.</p>"""
    last_operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The last unique ID of a StackSet operation performed on a stack instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_id" in value:
        pairs.append((f"{key_prefix}StackSetId", str(value["stack_set_id"])))
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "account" in value:
        pairs.append((f"{key_prefix}Account", str(value["account"])))
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "status" in value:
        import capo_cloudformation.types.stack_instance_status

        capo_cloudformation.types.stack_instance_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "stack_instance_status" in value:
        import capo_cloudformation.types.stack_instance_comprehensive_status

        capo_cloudformation.types.stack_instance_comprehensive_status.serialize_query(
            value["stack_instance_status"], pairs, f"{key_prefix}StackInstanceStatus"
        )
    if "organizational_unit_id" in value:
        pairs.append(
            (f"{key_prefix}OrganizationalUnitId", str(value["organizational_unit_id"]))
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
    if "last_operation_id" in value:
        pairs.append((f"{key_prefix}LastOperationId", str(value["last_operation_id"])))


def deserialize_query(el: Element) -> StackInstanceSummary:
    out: StackInstanceSummary = {}  # type: ignore[typeddict-item]
    child_stack_set_id = el.find("StackSetId")
    if child_stack_set_id is not None:
        out["stack_set_id"] = str(child_stack_set_id.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stack_instance_status

        out["status"] = (
            capo_cloudformation.types.stack_instance_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_stack_instance_status = el.find("StackInstanceStatus")
    if child_stack_instance_status is not None:
        import capo_cloudformation.types.stack_instance_comprehensive_status

        out["stack_instance_status"] = (
            capo_cloudformation.types.stack_instance_comprehensive_status.deserialize_query(
                child_stack_instance_status
            )
        )
    child_organizational_unit_id = el.find("OrganizationalUnitId")
    if child_organizational_unit_id is not None:
        out["organizational_unit_id"] = str(child_organizational_unit_id.text or "")
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
    child_last_operation_id = el.find("LastOperationId")
    if child_last_operation_id is not None:
        out["last_operation_id"] = str(child_last_operation_id.text or "")
    return out
