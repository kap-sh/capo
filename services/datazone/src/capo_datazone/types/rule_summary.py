"""Generated from Smithy shape ``com.amazonaws.datazone#RuleSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.revision
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_id
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_target
    import capo_datazone.types.rule_target_type
    import capo_datazone.types.rule_type
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class RuleSummary(TypedDict, closed=True):
    identifier: NotRequired["capo_datazone.types.rule_id.RuleId"]
    """<p>The ID of the rule.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the rule.</p>"""
    rule_type: NotRequired["capo_datazone.types.rule_type.RuleType"]
    """<p>The type of the rule.</p>"""
    name: NotRequired["capo_datazone.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    target_type: NotRequired["capo_datazone.types.rule_target_type.RuleTargetType"]
    """<p>The target type of the rule.</p>"""
    target: NotRequired["capo_datazone.types.rule_target.RuleTarget"]
    """<p>The target of the rule.</p>"""
    action: NotRequired["capo_datazone.types.rule_action.RuleAction"]
    """<p>The action of the rule.</p>"""
    scope: NotRequired["capo_datazone.types.rule_scope.RuleScope"]
    """<p>The scope of the rule.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the rule was last updated.</p>"""
    last_updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The timestamp at which the rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "rule_type" in value:
        import capo_datazone.types.rule_type

        out["ruleType"] = capo_datazone.types.rule_type.serialize_json(
            value["rule_type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "target_type" in value:
        import capo_datazone.types.rule_target_type

        out["targetType"] = capo_datazone.types.rule_target_type.serialize_json(
            value["target_type"]
        )
    if "target" in value:
        import capo_datazone.types.rule_target

        out["target"] = capo_datazone.types.rule_target.serialize_json(value["target"])
    if "action" in value:
        import capo_datazone.types.rule_action

        out["action"] = capo_datazone.types.rule_action.serialize_json(value["action"])
    if "scope" in value:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.serialize_json(value["scope"])
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("ruleType") is not None:
        import capo_datazone.types.rule_type

        out["rule_type"] = capo_datazone.types.rule_type.deserialize_json(
            data["ruleType"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("targetType") is not None:
        import capo_datazone.types.rule_target_type

        out["target_type"] = capo_datazone.types.rule_target_type.deserialize_json(
            data["targetType"]
        )
    if data.get("target") is not None:
        import capo_datazone.types.rule_target

        out["target"] = capo_datazone.types.rule_target.deserialize_json(data["target"])
    if data.get("action") is not None:
        import capo_datazone.types.rule_action

        out["action"] = capo_datazone.types.rule_action.deserialize_json(data["action"])
    if data.get("scope") is not None:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.deserialize_json(data["scope"])
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    return out


def redact_sensitive(value: RuleSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
