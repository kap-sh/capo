"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.pre_evaluation_filters
    import capo_connect.types.rule_actions
    import capo_connect.types.rule_function
    import capo_connect.types.rule_id
    import capo_connect.types.rule_name
    import capo_connect.types.rule_publish_status


class UpdateRuleRequest(TypedDict, closed=True):
    rule_id: "capo_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.rule_name.RuleName"
    """<p>The name of the rule. You can change the name only if <code>TriggerEventSource</code> is one of the following values: <code>OnZendeskTicketCreate</code> | <code>OnZendeskTicketStatusUpdate</code> | <code>OnSalesforceCaseCreate</code> </p>"""
    function: "capo_connect.types.rule_function.RuleFunction"
    """<p>The conditions of the rule.</p>"""
    actions: "capo_connect.types.rule_actions.RuleActions"
    """<p>A list of actions to be run when the rule is triggered.</p>"""
    publish_status: "capo_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""
    pre_evaluation_filters: NotRequired[
        "capo_connect.types.pre_evaluation_filters.PreEvaluationFilters"
    ]
    """<p>The pre-evaluation filters for the rule, that restrict the rule to be applied to only certain resources based on the resource's attributes, such as tags assigned to a contact. The pre-evaluation filters are applied even before rule conditions are evaluated and are used to enforce tag-based-access-control while applying rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Function"] = value["function"]
    import capo_connect.types.rule_actions

    out["Actions"] = capo_connect.types.rule_actions.serialize_json(value["actions"])
    import capo_connect.types.rule_publish_status

    out["PublishStatus"] = capo_connect.types.rule_publish_status.serialize_json(
        value["publish_status"]
    )
    if "pre_evaluation_filters" in value:
        import capo_connect.types.pre_evaluation_filters

        out["PreEvaluationFilters"] = (
            capo_connect.types.pre_evaluation_filters.serialize_json(
                value["pre_evaluation_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRuleRequest:
    out: UpdateRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateRuleRequest.name required")
    if data.get("Function") is not None:
        out["function"] = data["Function"]
    else:
        raise DeserializationError("UpdateRuleRequest.function required")
    if data.get("Actions") is not None:
        import capo_connect.types.rule_actions

        out["actions"] = capo_connect.types.rule_actions.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("UpdateRuleRequest.actions required")
    if data.get("PublishStatus") is not None:
        import capo_connect.types.rule_publish_status

        out["publish_status"] = capo_connect.types.rule_publish_status.deserialize_json(
            data["PublishStatus"]
        )
    else:
        raise DeserializationError("UpdateRuleRequest.publish_status required")
    if data.get("PreEvaluationFilters") is not None:
        import capo_connect.types.pre_evaluation_filters

        out["pre_evaluation_filters"] = (
            capo_connect.types.pre_evaluation_filters.deserialize_json(
                data["PreEvaluationFilters"]
            )
        )
    return out
