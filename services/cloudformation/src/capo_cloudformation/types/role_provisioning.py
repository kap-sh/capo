"""Generated from Smithy shape ``com.amazonaws.cloudformation#RoleProvisioning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.completed_accounts_count
    import capo_cloudformation.types.failed_accounts_count
    import capo_cloudformation.types.pending_accounts_count
    import capo_cloudformation.types.stage_percentage_completed
    import capo_cloudformation.types.stage_status
    import capo_cloudformation.types.succeeded_accounts_count


class RoleProvisioning(TypedDict, closed=True):
    status: NotRequired["capo_cloudformation.types.stage_status.StageStatus"]
    """<p>The status of the role provisioning stage can be one of the following values:</p> <ul> <li> <p> <code>NOT_APPLICABLE</code>: The operation does not provision roles. This includes self-managed operations and service-managed operations whose configuration does not require role provisioning.</p> </li> <li> <p> <code>NOT_STARTED</code>: Role provisioning has not started. The operation has not begun resolving target accounts, or it failed or stopped before the total number of target accounts was resolved.</p> </li> <li> <p> <code>IN_PROGRESS</code>: Role provisioning is actively processing target accounts.</p> </li> <li> <p> <code>SUCCEEDED</code>: Role provisioning finished and succeeded for all target accounts.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: Role provisioning finished, but succeeded for only a subset of target accounts; one or more accounts failed.</p> </li> <li> <p> <code>FAILED</code>: Role provisioning finished and failed for all target accounts.</p> </li> </ul>"""
    succeeded_accounts_count: NotRequired[
        "capo_cloudformation.types.succeeded_accounts_count.SucceededAccountsCount"
    ]
    """<p>The number of accounts for which role provisioning succeeded.</p>"""
    failed_accounts_count: NotRequired[
        "capo_cloudformation.types.failed_accounts_count.FailedAccountsCount"
    ]
    """<p>The number of accounts for which role provisioning failed.</p>"""
    completed_accounts_count: NotRequired[
        "capo_cloudformation.types.completed_accounts_count.CompletedAccountsCount"
    ]
    """<p>The number of accounts that have finished role provisioning, including both succeeded and failed accounts.</p>"""
    pending_accounts_count: NotRequired[
        "capo_cloudformation.types.pending_accounts_count.PendingAccountsCount"
    ]
    """<p>The number of accounts that are still awaiting role provisioning.</p>"""
    percentage_completed: NotRequired[
        "capo_cloudformation.types.stage_percentage_completed.StagePercentageCompleted"
    ]
    """<p>The percentage of accounts that have completed role provisioning.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleProvisioning, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_cloudformation.types.stage_status

        capo_cloudformation.types.stage_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "succeeded_accounts_count" in value:
        pairs.append(
            (
                f"{key_prefix}SucceededAccountsCount",
                str(value["succeeded_accounts_count"]),
            )
        )
    if "failed_accounts_count" in value:
        pairs.append(
            (f"{key_prefix}FailedAccountsCount", str(value["failed_accounts_count"]))
        )
    if "completed_accounts_count" in value:
        pairs.append(
            (
                f"{key_prefix}CompletedAccountsCount",
                str(value["completed_accounts_count"]),
            )
        )
    if "pending_accounts_count" in value:
        pairs.append(
            (f"{key_prefix}PendingAccountsCount", str(value["pending_accounts_count"]))
        )
    if "percentage_completed" in value:
        pairs.append(
            (
                f"{key_prefix}PercentageCompleted",
                (
                    "NaN"
                    if value["percentage_completed"] != value["percentage_completed"]
                    else "Infinity"
                    if value["percentage_completed"] == float("inf")
                    else "-Infinity"
                    if value["percentage_completed"] == float("-inf")
                    else str(value["percentage_completed"])
                ),
            )
        )


def deserialize_query(el: Element) -> RoleProvisioning:
    out: RoleProvisioning = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stage_status

        out["status"] = capo_cloudformation.types.stage_status.deserialize_query(
            child_status
        )
    child_succeeded_accounts_count = el.find("SucceededAccountsCount")
    if child_succeeded_accounts_count is not None:
        out["succeeded_accounts_count"] = int(child_succeeded_accounts_count.text or "")
    child_failed_accounts_count = el.find("FailedAccountsCount")
    if child_failed_accounts_count is not None:
        out["failed_accounts_count"] = int(child_failed_accounts_count.text or "")
    child_completed_accounts_count = el.find("CompletedAccountsCount")
    if child_completed_accounts_count is not None:
        out["completed_accounts_count"] = int(child_completed_accounts_count.text or "")
    child_pending_accounts_count = el.find("PendingAccountsCount")
    if child_pending_accounts_count is not None:
        out["pending_accounts_count"] = int(child_pending_accounts_count.text or "")
    child_percentage_completed = el.find("PercentageCompleted")
    if child_percentage_completed is not None:
        out["percentage_completed"] = float(child_percentage_completed.text or "")
    return out
