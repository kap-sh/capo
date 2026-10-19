"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.rule_match
    import capo_vpc_lattice.types.rule_name
    import capo_vpc_lattice.types.rule_priority
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.tag_map


class CreateRuleRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    """<p>The ID or ARN of the listener.</p>"""
    name: "capo_vpc_lattice.types.rule_name.RuleName"
    """<p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    match: "capo_vpc_lattice.types.rule_match.RuleMatch"
    """<p>The rule match.</p>"""
    priority: "capo_vpc_lattice.types.rule_priority.RulePriority"
    """<p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>"""
    action: "capo_vpc_lattice.types.rule_action.RuleAction"
    """<p>The action for the default rule.</p>"""
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_vpc_lattice.types.rule_match

    out["match"] = capo_vpc_lattice.types.rule_match.serialize_json(value["match"])
    out["priority"] = value["priority"]
    import capo_vpc_lattice.types.rule_action

    out["action"] = capo_vpc_lattice.types.rule_action.serialize_json(value["action"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRuleRequest:
    out: CreateRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("match") is not None:
        import capo_vpc_lattice.types.rule_match

        out["match"] = capo_vpc_lattice.types.rule_match.deserialize_json(data["match"])
    else:
        import capo_vpc_lattice.types._unknown

        out["match"] = capo_vpc_lattice.types._unknown.UnknownUnionMember("")
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
    if data.get("action") is not None:
        import capo_vpc_lattice.types.rule_action

        out["action"] = capo_vpc_lattice.types.rule_action.deserialize_json(
            data["action"]
        )
    else:
        import capo_vpc_lattice.types._unknown

        out["action"] = capo_vpc_lattice.types._unknown.UnknownUnionMember("")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
