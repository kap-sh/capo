"""Generated from Smithy shape ``com.amazonaws.datazone#CreateRuleInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_target


class CreateRuleInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the rule is created.</p>"""
    name: "capo_datazone.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    target: "capo_datazone.types.rule_target.RuleTarget"
    """<p>The target of the rule.</p>"""
    action: "capo_datazone.types.rule_action.RuleAction"
    """<p>The action of the rule.</p>"""
    scope: "capo_datazone.types.rule_scope.RuleScope"
    """<p>The scope of the rule.</p>"""
    detail: "capo_datazone.types.rule_detail.RuleDetail"
    """<p>The detail of the rule.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_datazone.types.rule_target

    out["target"] = capo_datazone.types.rule_target.serialize_json(value["target"])
    import capo_datazone.types.rule_action

    out["action"] = capo_datazone.types.rule_action.serialize_json(value["action"])
    import capo_datazone.types.rule_scope

    out["scope"] = capo_datazone.types.rule_scope.serialize_json(value["scope"])
    import capo_datazone.types.rule_detail

    out["detail"] = capo_datazone.types.rule_detail.serialize_json(value["detail"])
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRuleInput:
    out: CreateRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("target") is not None:
        import capo_datazone.types.rule_target

        out["target"] = capo_datazone.types.rule_target.deserialize_json(data["target"])
    else:
        out["target"] = {"$unknown": {"name": ""}}
    if data.get("action") is not None:
        import capo_datazone.types.rule_action

        out["action"] = capo_datazone.types.rule_action.deserialize_json(data["action"])
    else:
        import typing

        out["action"] = typing.cast("capo_datazone.types.rule_action.RuleAction", "")
    if data.get("scope") is not None:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("CreateRuleInput.scope required")
    if data.get("detail") is not None:
        import capo_datazone.types.rule_detail

        out["detail"] = capo_datazone.types.rule_detail.deserialize_json(data["detail"])
    else:
        out["detail"] = {"$unknown": {"name": ""}}
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateRuleInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
