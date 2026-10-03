"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.action
    import capo_cloudwatch_events.types.condition
    import capo_cloudwatch_events.types.non_partner_event_bus_name
    import capo_cloudwatch_events.types.principal
    import capo_cloudwatch_events.types.statement_id
    import capo_cloudwatch_events.types.string


class PutPermissionRequest(TypedDict, closed=True):
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.non_partner_event_bus_name.NonPartnerEventBusName"
    ]
    """<p>The name of the event bus associated with the rule. If you omit this, the default event bus is used.</p>"""
    action: NotRequired["capo_cloudwatch_events.types.action.Action"]
    """<p>The action that you are enabling the other account to perform.</p>"""
    principal: NotRequired["capo_cloudwatch_events.types.principal.Principal"]
    """<p>The 12-digit Amazon Web Services account ID that you are permitting to put events to your default event bus. Specify "*" to permit any account to put events to your default event bus.</p> <p>If you specify "*" without specifying <code>Condition</code>, avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an <code>account</code> field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.</p>"""
    statement_id: NotRequired["capo_cloudwatch_events.types.statement_id.StatementId"]
    """<p>An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this <code>StatementId</code> when you run <a href="https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html">RemovePermission</a>.</p>"""
    condition: NotRequired["capo_cloudwatch_events.types.condition.Condition"]
    """<p>This parameter enables you to limit the permission to accounts that fulfill a certain condition, such as being a member of a certain Amazon Web Services organization. For more information about Amazon Web Services Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html">What Is Amazon Web Services Organizations</a> in the <i>Amazon Web Services Organizations User Guide</i>.</p> <p>If you specify <code>Condition</code> with an Amazon Web Services organization ID, and specify "*" as the value for <code>Principal</code>, you grant permission to all the accounts in the named organization.</p> <p>The <code>Condition</code> is a JSON string which must contain <code>Type</code>, <code>Key</code>, and <code>Value</code> fields.</p>"""
    policy: NotRequired["capo_cloudwatch_events.types.string.String"]
    """<p>A JSON string that describes the permission policy statement. You can include a <code>Policy</code> parameter in the request instead of using the <code>StatementId</code>, <code>Action</code>, <code>Principal</code>, or <code>Condition</code> parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPermissionRequest) -> dict:
    out: dict = {}
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    if "action" in value:
        out["Action"] = value["action"]
    if "principal" in value:
        out["Principal"] = value["principal"]
    if "statement_id" in value:
        out["StatementId"] = value["statement_id"]
    if "condition" in value:
        import capo_cloudwatch_events.types.condition

        out["Condition"] = (
            capo_cloudwatch_events.types.condition.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPermissionRequest:
    out: PutPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    if data.get("StatementId") is not None:
        out["statement_id"] = data["StatementId"]
    if data.get("Condition") is not None:
        import capo_cloudwatch_events.types.condition

        out["condition"] = (
            capo_cloudwatch_events.types.condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
