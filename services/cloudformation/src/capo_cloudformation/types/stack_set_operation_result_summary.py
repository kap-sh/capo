"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationResultSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account
    import capo_cloudformation.types.account_gate_result
    import capo_cloudformation.types.organizational_unit_id
    import capo_cloudformation.types.reason
    import capo_cloudformation.types.region
    import capo_cloudformation.types.stack_set_operation_result_status


class StackSetOperationResultSummary(TypedDict, closed=True):
    account: NotRequired["capo_cloudformation.types.account.Account"]
    """<p>[Self-managed permissions] The name of the Amazon Web Services account for this operation result.</p>"""
    region: NotRequired["capo_cloudformation.types.region.Region"]
    """<p>The name of the Amazon Web Services Region for this operation result.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.stack_set_operation_result_status.StackSetOperationResultStatus"
    ]
    """<p>The result status of the StackSet operation for the given account in the given Region.</p> <ul> <li> <p> <code>CANCELLED</code>: The operation in the specified account and Region has been canceled. This is either because a user has stopped the StackSet operation, or because the failure tolerance of the StackSet operation has been exceeded.</p> </li> <li> <p> <code>FAILED</code>: The operation in the specified account and Region failed.</p> <p>If the StackSet operation fails in enough accounts within a Region, the failure tolerance for the StackSet operation as a whole might be exceeded.</p> </li> <li> <p> <code>RUNNING</code>: The operation in the specified account and Region is currently in progress.</p> </li> <li> <p> <code>PENDING</code>: The operation in the specified account and Region has yet to start.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation in the specified account and Region completed successfully.</p> </li> </ul>"""
    status_reason: NotRequired["capo_cloudformation.types.reason.Reason"]
    """<p>The reason for the assigned result status.</p>"""
    account_gate_result: NotRequired[
        "capo_cloudformation.types.account_gate_result.AccountGateResult"
    ]
    """<p>The results of the account gate function CloudFormation invokes, if present, before proceeding with StackSet operations in an account.</p>"""
    organizational_unit_id: NotRequired[
        "capo_cloudformation.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperationResultSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account" in value:
        pairs.append((f"{key_prefix}Account", str(value["account"])))
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "status" in value:
        import capo_cloudformation.types.stack_set_operation_result_status

        capo_cloudformation.types.stack_set_operation_result_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "account_gate_result" in value:
        import capo_cloudformation.types.account_gate_result

        capo_cloudformation.types.account_gate_result.serialize_query(
            value["account_gate_result"], pairs, f"{key_prefix}AccountGateResult"
        )
    if "organizational_unit_id" in value:
        pairs.append(
            (f"{key_prefix}OrganizationalUnitId", str(value["organizational_unit_id"]))
        )


def deserialize_query(el: Element) -> StackSetOperationResultSummary:
    out: StackSetOperationResultSummary = {}  # type: ignore[typeddict-item]
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stack_set_operation_result_status

        out["status"] = (
            capo_cloudformation.types.stack_set_operation_result_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_account_gate_result = el.find("AccountGateResult")
    if child_account_gate_result is not None:
        import capo_cloudformation.types.account_gate_result

        out["account_gate_result"] = (
            capo_cloudformation.types.account_gate_result.deserialize_query(
                child_account_gate_result
            )
        )
    child_organizational_unit_id = el.find("OrganizationalUnitId")
    if child_organizational_unit_id is not None:
        out["organizational_unit_id"] = str(child_organizational_unit_id.text or "")
    return out
