"""Generated from Smithy shape ``com.amazonaws.iot#TopicRulePayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.action
    import capo_iot.types.action_list
    import capo_iot.types.aws_iot_sql_version
    import capo_iot.types.description
    import capo_iot.types.is_disabled
    import capo_iot.types.sql


class TopicRulePayload(TypedDict, closed=True):
    sql: "capo_iot.types.sql.SQL"
    """<p>The SQL statement used to query the topic. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html">IoT SQL Reference</a> in the <i>IoT Developer Guide</i>.</p>"""
    description: NotRequired["capo_iot.types.description.Description"]
    """<p>The description of the rule.</p>"""
    actions: "capo_iot.types.action_list.ActionList"
    """<p>The actions associated with the rule.</p>"""
    rule_disabled: NotRequired["capo_iot.types.is_disabled.IsDisabled"]
    """<p>Specifies whether the rule is disabled.</p>"""
    aws_iot_sql_version: NotRequired[
        "capo_iot.types.aws_iot_sql_version.AwsIotSqlVersion"
    ]
    """<p>The version of the SQL rules engine to use when evaluating the rule.</p>"""
    error_action: NotRequired["capo_iot.types.action.Action"]
    """<p>The action to take when an error occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRulePayload) -> dict:
    out: dict = {}
    out["sql"] = value["sql"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_iot.types.action_list

    out["actions"] = capo_iot.types.action_list.serialize_json(value["actions"])
    if "rule_disabled" in value:
        out["ruleDisabled"] = value["rule_disabled"]
    if "aws_iot_sql_version" in value:
        out["awsIotSqlVersion"] = value["aws_iot_sql_version"]
    if "error_action" in value:
        import capo_iot.types.action

        out["errorAction"] = capo_iot.types.action.serialize_json(value["error_action"])
    return out


def deserialize_json(data: dict) -> TopicRulePayload:
    out: TopicRulePayload = {}  # type: ignore[typeddict-item]
    if data.get("sql") is not None:
        out["sql"] = data["sql"]
    else:
        raise DeserializationError("TopicRulePayload.sql required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("actions") is not None:
        import capo_iot.types.action_list

        out["actions"] = capo_iot.types.action_list.deserialize_json(data["actions"])
    else:
        raise DeserializationError("TopicRulePayload.actions required")
    if data.get("ruleDisabled") is not None:
        out["rule_disabled"] = data["ruleDisabled"]
    if data.get("awsIotSqlVersion") is not None:
        out["aws_iot_sql_version"] = data["awsIotSqlVersion"]
    if data.get("errorAction") is not None:
        import capo_iot.types.action

        out["error_action"] = capo_iot.types.action.deserialize_json(
            data["errorAction"]
        )
    return out
