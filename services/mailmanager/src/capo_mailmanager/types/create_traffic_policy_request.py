"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateTrafficPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.max_message_size_bytes
    import capo_mailmanager.types.policy_statement_list
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.traffic_policy_name


class CreateTrafficPolicyRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    traffic_policy_name: "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    """<p>A user-friendly name for the traffic policy resource.</p>"""
    policy_statements: (
        "capo_mailmanager.types.policy_statement_list.PolicyStatementList"
    )
    """<p>Conditional statements for filtering email traffic.</p>"""
    default_action: "capo_mailmanager.types.accept_action.AcceptAction"
    """<p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>"""
    max_message_size_bytes: NotRequired[
        "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
    ]
    """<p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTrafficPolicyRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["TrafficPolicyName"] = value["traffic_policy_name"]
    import capo_mailmanager.types.policy_statement_list

    out["PolicyStatements"] = (
        capo_mailmanager.types.policy_statement_list.serialize_aws_json_1_0(
            value["policy_statements"]
        )
    )
    import capo_mailmanager.types.accept_action

    out["DefaultAction"] = capo_mailmanager.types.accept_action.serialize_aws_json_1_0(
        value["default_action"]
    )
    if "max_message_size_bytes" in value:
        out["MaxMessageSizeBytes"] = value["max_message_size_bytes"]
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTrafficPolicyRequest:
    out: CreateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("TrafficPolicyName") is not None:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    else:
        raise DeserializationError(
            "CreateTrafficPolicyRequest.traffic_policy_name required"
        )
    if data.get("PolicyStatements") is not None:
        import capo_mailmanager.types.policy_statement_list

        out["policy_statements"] = (
            capo_mailmanager.types.policy_statement_list.deserialize_aws_json_1_0(
                data["PolicyStatements"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTrafficPolicyRequest.policy_statements required"
        )
    if data.get("DefaultAction") is not None:
        import capo_mailmanager.types.accept_action

        out["default_action"] = (
            capo_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    else:
        raise DeserializationError("CreateTrafficPolicyRequest.default_action required")
    if data.get("MaxMessageSizeBytes") is not None:
        out["max_message_size_bytes"] = data["MaxMessageSizeBytes"]
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
