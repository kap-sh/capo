"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.rule_set_name
    import capo_mailmanager.types.rules
    import capo_mailmanager.types.tag_list


class CreateRuleSetRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    rule_set_name: "capo_mailmanager.types.rule_set_name.RuleSetName"
    """<p>A user-friendly name for the rule set.</p>"""
    rules: "capo_mailmanager.types.rules.Rules"
    """<p>Conditional rules that are evaluated for determining actions on email.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRuleSetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["RuleSetName"] = value["rule_set_name"]
    import capo_mailmanager.types.rules

    out["Rules"] = capo_mailmanager.types.rules.serialize_aws_json_1_0(value["rules"])
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRuleSetRequest:
    out: CreateRuleSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    else:
        raise DeserializationError("CreateRuleSetRequest.rule_set_name required")
    if data.get("Rules") is not None:
        import capo_mailmanager.types.rules

        out["rules"] = capo_mailmanager.types.rules.deserialize_aws_json_1_0(
            data["Rules"]
        )
    else:
        raise DeserializationError("CreateRuleSetRequest.rules required")
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
