"""Generated from Smithy shape ``com.amazonaws.cloudformation#ExecuteChangeSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_name_or_id
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.disable_rollback
    import capo_cloudformation.types.retain_except_on_create
    import capo_cloudformation.types.stack_name_or_id


class ExecuteChangeSetInput(TypedDict, closed=True):
    change_set_name: NotRequired[
        "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.</p>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.</p>"""
    disable_rollback: NotRequired[
        "capo_cloudformation.types.disable_rollback.DisableRollback"
    ]
    """<p>Preserves the state of previously provisioned resources when an operation fails. This parameter can't be specified when the <code>OnStackFailure</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html">CreateChangeSet</a> API operation was specified.</p> <ul> <li> <p> <code>True</code> - if the stack creation fails, do nothing. This is equivalent to specifying <code>DO_NOTHING</code> for the <code>OnStackFailure</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html">CreateChangeSet</a> API operation.</p> </li> <li> <p> <code>False</code> - if the stack creation fails, roll back the stack. This is equivalent to specifying <code>ROLLBACK</code> for the <code>OnStackFailure</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html">CreateChangeSet</a> API operation.</p> </li> </ul> <p>Default: <code>True</code> </p>"""
    retain_except_on_create: NotRequired[
        "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
    ]
    """<p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ExecuteChangeSetInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "change_set_name" in value:
        pairs.append((f"{key_prefix}ChangeSetName", str(value["change_set_name"])))
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )
    if "disable_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}DisableRollback",
                "true" if value["disable_rollback"] else "false",
            )
        )
    if "retain_except_on_create" in value:
        pairs.append(
            (
                f"{key_prefix}RetainExceptOnCreate",
                "true" if value["retain_except_on_create"] else "false",
            )
        )


def deserialize_query(el: Element) -> ExecuteChangeSetInput:
    out: ExecuteChangeSetInput = {}  # type: ignore[typeddict-item]
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_disable_rollback = el.find("DisableRollback")
    if child_disable_rollback is not None:
        out["disable_rollback"] = (child_disable_rollback.text or "").lower() == "true"
    child_retain_except_on_create = el.find("RetainExceptOnCreate")
    if child_retain_except_on_create is not None:
        out["retain_except_on_create"] = (
            child_retain_except_on_create.text or ""
        ).lower() == "true"
    return out
