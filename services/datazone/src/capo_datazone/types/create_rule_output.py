"""Generated from Smithy shape ``com.amazonaws.datazone#CreateRuleOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_id
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_target
    import capo_datazone.types.rule_target_type
    import capo_datazone.types.rule_type


class CreateRuleOutput(TypedDict, closed=True):
    identifier: "capo_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule.</p>"""
    name: "capo_datazone.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_type: "capo_datazone.types.rule_type.RuleType"
    """<p>The type of the rule.</p>"""
    target: "capo_datazone.types.rule_target.RuleTarget"
    """<p>The target of the rule.</p>"""
    action: "capo_datazone.types.rule_action.RuleAction"
    """<p>The action of the rule.</p>"""
    scope: "capo_datazone.types.rule_scope.RuleScope"
    """<p>The scope of the rule.</p>"""
    detail: "capo_datazone.types.rule_detail.RuleDetail"
    """<p>The detail of the rule.</p>"""
    target_type: NotRequired["capo_datazone.types.rule_target_type.RuleTargetType"]
    """<p>The target type of the rule.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp at which the rule is created.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The user who creates the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["name"] = value["name"]
    import capo_datazone.types.rule_type

    out["ruleType"] = capo_datazone.types.rule_type.serialize_json(value["rule_type"])
    import capo_datazone.types.rule_target

    out["target"] = capo_datazone.types.rule_target.serialize_json(value["target"])
    import capo_datazone.types.rule_action

    out["action"] = capo_datazone.types.rule_action.serialize_json(value["action"])
    import capo_datazone.types.rule_scope

    out["scope"] = capo_datazone.types.rule_scope.serialize_json(value["scope"])
    import capo_datazone.types.rule_detail

    out["detail"] = capo_datazone.types.rule_detail.serialize_json(value["detail"])
    if "target_type" in value:
        import capo_datazone.types.rule_target_type

        out["targetType"] = capo_datazone.types.rule_target_type.serialize_json(
            value["target_type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> CreateRuleOutput:
    out: CreateRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ruleType") is not None:
        import capo_datazone.types.rule_type

        out["rule_type"] = capo_datazone.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    else:
        import typing

        out["rule_type"] = typing.cast("capo_datazone.types.rule_type.RuleType", "")
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
        raise DeserializationError("CreateRuleOutput.scope required")
    if data.get("detail") is not None:
        import capo_datazone.types.rule_detail

        out["detail"] = capo_datazone.types.rule_detail.deserialize_json(data["detail"])
    else:
        out["detail"] = {"$unknown": {"name": ""}}
    if data.get("targetType") is not None:
        import capo_datazone.types.rule_target_type

        out["target_type"] = capo_datazone.types.rule_target_type.deserialize_json(
            data["targetType"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    return out


def redact_sensitive(value: CreateRuleOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
