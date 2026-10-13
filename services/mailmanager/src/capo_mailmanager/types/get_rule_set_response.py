"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetRuleSetResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.rule_set_arn
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.rule_set_name
    import capo_mailmanager.types.rules


class GetRuleSetResponse(TypedDict, closed=True):
    rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of the rule set resource.</p>"""
    rule_set_arn: "capo_mailmanager.types.rule_set_arn.RuleSetArn"
    """<p>The Amazon Resource Name (ARN) of the rule set resource.</p>"""
    rule_set_name: "capo_mailmanager.types.rule_set_name.RuleSetName"
    """<p>A user-friendly name for the rule set resource.</p>"""
    created_date: "datetime.datetime"
    """<p>The date of when then rule set was created.</p>"""
    last_modification_date: "datetime.datetime"
    """<p>The date of when the rule set was last modified.</p>"""
    rules: "capo_mailmanager.types.rules.Rules"
    """<p>The rules contained in the rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRuleSetResponse) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    out["RuleSetArn"] = value["rule_set_arn"]
    out["RuleSetName"] = value["rule_set_name"]
    import capo_mailmanager.types._prelude.timestamp

    out["CreatedDate"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import capo_mailmanager.types._prelude.timestamp

    out["LastModificationDate"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_modification_date"]
        )
    )
    import capo_mailmanager.types.rules

    out["Rules"] = capo_mailmanager.types.rules.serialize_aws_json_1_0(value["rules"])
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRuleSetResponse:
    out: GetRuleSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("GetRuleSetResponse.rule_set_id required")
    if data.get("RuleSetArn") is not None:
        out["rule_set_arn"] = data["RuleSetArn"]
    else:
        raise DeserializationError("GetRuleSetResponse.rule_set_arn required")
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    else:
        raise DeserializationError("GetRuleSetResponse.rule_set_name required")
    if data.get("CreatedDate") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_date"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    else:
        raise DeserializationError("GetRuleSetResponse.created_date required")
    if data.get("LastModificationDate") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_modification_date"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModificationDate"]
            )
        )
    else:
        raise DeserializationError("GetRuleSetResponse.last_modification_date required")
    if data.get("Rules") is not None:
        import capo_mailmanager.types.rules

        out["rules"] = capo_mailmanager.types.rules.deserialize_aws_json_1_0(
            data["Rules"]
        )
    else:
        raise DeserializationError("GetRuleSetResponse.rules required")
    return out


def redact_sensitive(value: GetRuleSetResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rules" in value:
        import capo_mailmanager.types.rules

        out["rules"] = capo_mailmanager.types.rules.redact_sensitive(value["rules"])
    return out
