"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListHookResultsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.hook_result_id
    import capo_cloudformation.types.hook_status
    import capo_cloudformation.types.hook_type_arn
    import capo_cloudformation.types.list_hook_results_target_type
    import capo_cloudformation.types.next_token


class ListHookResultsInput(TypedDict, closed=True):
    target_type: NotRequired[
        "capo_cloudformation.types.list_hook_results_target_type.ListHookResultsTargetType"
    ]
    """<p>Filters results by target type. Currently, only <code>CHANGE_SET</code> and <code>CLOUD_CONTROL</code> are supported filter options.</p> <p>Required when <code>TargetId</code> is specified and cannot be used otherwise.</p>"""
    target_id: NotRequired["capo_cloudformation.types.hook_result_id.HookResultId"]
    """<p>Filters results by the unique identifier of the target the Hook was invoked against.</p> <p>For change sets, this is the change set ARN. When the target is a Cloud Control API operation, this value must be the <code>HookRequestToken</code> returned by the Cloud Control API request. For more information on the <code>HookRequestToken</code>, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ProgressEvent.html">ProgressEvent</a>.</p> <p>Required when <code>TargetType</code> is specified and cannot be used otherwise.</p>"""
    type_arn: NotRequired["capo_cloudformation.types.hook_type_arn.HookTypeArn"]
    """<p>Filters results by the ARN of the Hook. Can be used alone or in combination with <code>Status</code>.</p>"""
    status: NotRequired["capo_cloudformation.types.hook_status.HookStatus"]
    """<p>Filters results by the status of Hook invocations. Can only be used in combination with <code>TypeArn</code>. Valid values are:</p> <ul> <li> <p> <code>HOOK_IN_PROGRESS</code>: The Hook is currently running.</p> </li> <li> <p> <code>HOOK_COMPLETE_SUCCEEDED</code>: The Hook completed successfully.</p> </li> <li> <p> <code>HOOK_COMPLETE_FAILED</code>: The Hook completed but failed validation.</p> </li> <li> <p> <code>HOOK_FAILED</code>: The Hook encountered an error during execution.</p> </li> </ul>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListHookResultsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_type" in value:
        import capo_cloudformation.types.list_hook_results_target_type

        capo_cloudformation.types.list_hook_results_target_type.serialize_query(
            value["target_type"], pairs, f"{key_prefix}TargetType"
        )
    if "target_id" in value:
        pairs.append((f"{key_prefix}TargetId", str(value["target_id"])))
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "status" in value:
        import capo_cloudformation.types.hook_status

        capo_cloudformation.types.hook_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListHookResultsInput:
    out: ListHookResultsInput = {}  # type: ignore[typeddict-item]
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import capo_cloudformation.types.list_hook_results_target_type

        out["target_type"] = (
            capo_cloudformation.types.list_hook_results_target_type.deserialize_query(
                child_target_type
            )
        )
    child_target_id = el.find("TargetId")
    if child_target_id is not None:
        out["target_id"] = str(child_target_id.text or "")
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.hook_status

        out["status"] = capo_cloudformation.types.hook_status.deserialize_query(
            child_status
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
