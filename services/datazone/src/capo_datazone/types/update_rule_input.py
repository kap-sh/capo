"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateRuleInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_id
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope


class UpdateRuleInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which a rule is to be updated.</p>"""
    identifier: "capo_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule that is to be updated</p>"""
    name: NotRequired["capo_datazone.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the rule.</p>"""
    scope: NotRequired["capo_datazone.types.rule_scope.RuleScope"]
    """<p>The scrope of the rule.</p>"""
    detail: NotRequired["capo_datazone.types.rule_detail.RuleDetail"]
    """<p>The detail of the rule.</p>"""
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether to update this rule in the child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "scope" in value:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.serialize_json(value["scope"])
    if "detail" in value:
        import capo_datazone.types.rule_detail

        out["detail"] = capo_datazone.types.rule_detail.serialize_json(value["detail"])
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> UpdateRuleInput:
    out: UpdateRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("scope") is not None:
        import capo_datazone.types.rule_scope

        out["scope"] = capo_datazone.types.rule_scope.deserialize_json(data["scope"])
    if data.get("detail") is not None:
        import capo_datazone.types.rule_detail

        out["detail"] = capo_datazone.types.rule_detail.deserialize_json(data["detail"])
    if data.get("includeChildDomainUnits") is not None:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out


def redact_sensitive(value: UpdateRuleInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
