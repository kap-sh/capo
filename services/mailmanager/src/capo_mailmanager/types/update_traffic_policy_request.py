"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateTrafficPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.max_message_size_bytes
    import capo_mailmanager.types.policy_statement_list
    import capo_mailmanager.types.traffic_policy_id
    import capo_mailmanager.types.traffic_policy_name


class UpdateTrafficPolicyRequest(TypedDict, closed=True):
    traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy that you want to update.</p>"""
    traffic_policy_name: NotRequired[
        "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    ]
    """<p>A user-friendly name for the traffic policy resource.</p>"""
    policy_statements: NotRequired[
        "capo_mailmanager.types.policy_statement_list.PolicyStatementList"
    ]
    """<p>The list of conditions to be updated for filtering email traffic.</p>"""
    default_action: NotRequired["capo_mailmanager.types.accept_action.AcceptAction"]
    """<p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>"""
    max_message_size_bytes: NotRequired[
        "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
    ]
    """<p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTrafficPolicyRequest) -> dict:
    out: dict = {}
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "traffic_policy_name" in value:
        out["TrafficPolicyName"] = value["traffic_policy_name"]
    if "policy_statements" in value:
        import capo_mailmanager.types.policy_statement_list

        out["PolicyStatements"] = (
            capo_mailmanager.types.policy_statement_list.serialize_aws_json_1_0(
                value["policy_statements"]
            )
        )
    if "default_action" in value:
        import capo_mailmanager.types.accept_action

        out["DefaultAction"] = (
            capo_mailmanager.types.accept_action.serialize_aws_json_1_0(
                value["default_action"]
            )
        )
    if "max_message_size_bytes" in value:
        out["MaxMessageSizeBytes"] = value["max_message_size_bytes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTrafficPolicyRequest:
    out: UpdateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        out["traffic_policy_id"] = ""
    if data.get("TrafficPolicyName") is not None:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    if data.get("PolicyStatements") is not None:
        import capo_mailmanager.types.policy_statement_list

        out["policy_statements"] = (
            capo_mailmanager.types.policy_statement_list.deserialize_aws_json_1_0(
                data["PolicyStatements"]
            )
        )
    if data.get("DefaultAction") is not None:
        import capo_mailmanager.types.accept_action

        out["default_action"] = (
            capo_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    if data.get("MaxMessageSizeBytes") is not None:
        out["max_message_size_bytes"] = data["MaxMessageSizeBytes"]
    return out
