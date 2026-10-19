"""Generated from Smithy shape ``com.amazonaws.mailmanager#TrafficPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.accept_action
    import capo_mailmanager.types.traffic_policy_id
    import capo_mailmanager.types.traffic_policy_name


class TrafficPolicy(TypedDict, closed=True):
    traffic_policy_name: "capo_mailmanager.types.traffic_policy_name.TrafficPolicyName"
    """<p>A user-friendly name of the traffic policy resource.</p>"""
    traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of the traffic policy resource.</p>"""
    default_action: "capo_mailmanager.types.accept_action.AcceptAction"
    """<p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TrafficPolicy) -> dict:
    out: dict = {}
    out["TrafficPolicyName"] = value["traffic_policy_name"]
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    import capo_mailmanager.types.accept_action

    out["DefaultAction"] = capo_mailmanager.types.accept_action.serialize_aws_json_1_0(
        value["default_action"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TrafficPolicy:
    out: TrafficPolicy = {}  # type: ignore[typeddict-item]
    if data.get("TrafficPolicyName") is not None:
        out["traffic_policy_name"] = data["TrafficPolicyName"]
    else:
        out["traffic_policy_name"] = ""
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        out["traffic_policy_id"] = ""
    if data.get("DefaultAction") is not None:
        import capo_mailmanager.types.accept_action

        out["default_action"] = (
            capo_mailmanager.types.accept_action.deserialize_aws_json_1_0(
                data["DefaultAction"]
            )
        )
    else:
        import typing

        out["default_action"] = typing.cast(
            "capo_mailmanager.types.accept_action.AcceptAction", ""
        )
    return out
