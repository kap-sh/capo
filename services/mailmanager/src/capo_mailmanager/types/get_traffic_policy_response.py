"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetTrafficPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.max_message_size_bytes
    import capo_mailmanager.types.policy_statement_list
    import capo_mailmanager.types.traffic_policy_arn
    import capo_mailmanager.types.traffic_policy_id
    import capo_mailmanager.types.traffic_policy_name


class GetTrafficPolicyResponse(TypedDict, closed=True):
    traffic_policy_name: "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    """<p>A user-friendly name for the traffic policy resource.</p>"""
    traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy resource.</p>"""
    traffic_policy_arn: NotRequired[
        "capo_mailmanager.types.traffic_policy_arn.TrafficPolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the traffic policy resource.</p>"""
    policy_statements: NotRequired[
        "capo_mailmanager.types.policy_statement_list.PolicyStatementList"
    ]
    """<p>The list of conditions which are in the traffic policy resource.</p>"""
    max_message_size_bytes: NotRequired[
        "capo_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
    ]
    """<p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>"""
    default_action: NotRequired["capo_mailmanager.types.accept_action.AcceptAction"]
    """<p>The default action of the traffic policy.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the traffic policy was created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the traffic policy was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTrafficPolicyResponse) -> dict:
    out: dict = {}
    out["TrafficPolicyName"] = value["traffic_policy_name"]
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "traffic_policy_arn" in value:
        out["TrafficPolicyArn"] = value["traffic_policy_arn"]
    if "policy_statements" in value:
        import capo_mailmanager.types.policy_statement_list

        out["PolicyStatements"] = (
            capo_mailmanager.types.policy_statement_list.serialize_aws_json_1_0(
                value["policy_statements"]
            )
        )
    if "max_message_size_bytes" in value:
        out["MaxMessageSizeBytes"] = value["max_message_size_bytes"]
    if "default_action" in value:
        import capo_mailmanager.types.accept_action

        out["DefaultAction"] = (
            capo_mailmanager.types.accept_action.serialize_aws_json_1_0(
                value["default_action"]
            )
        )
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTrafficPolicyResponse:
    out: GetTrafficPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrafficPolicyName") is not None:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    else:
        out["traffic_policy_name"] = ""
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        out["traffic_policy_id"] = ""
    if data.get("TrafficPolicyArn") is not None:
        out["traffic_policy_arn"] = data["TrafficPolicyArn"]
    if data.get("PolicyStatements") is not None:
        import capo_mailmanager.types.policy_statement_list

        out["policy_statements"] = (
            capo_mailmanager.types.policy_statement_list.deserialize_aws_json_1_0(
                data["PolicyStatements"]
            )
        )
    if data.get("MaxMessageSizeBytes") is not None:
        out["max_message_size_bytes"] = data["MaxMessageSizeBytes"]
    if data.get("DefaultAction") is not None:
        import capo_mailmanager.types.accept_action

        out["default_action"] = (
            capo_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
