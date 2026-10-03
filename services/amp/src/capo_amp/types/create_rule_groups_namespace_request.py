"""Generated from Smithy shape ``com.amazonaws.amp#CreateRuleGroupsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.rule_groups_namespace_data
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.tag_map
    import capo_amp.types.workspace_id


class CreateRuleGroupsNamespaceRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to add the rule groups namespace.</p>"""
    name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name for the new rule groups namespace.</p>"""
    data: "capo_amp.types.rule_groups_namespace_data.RuleGroupsNamespaceData"
    """<p>The rules file to use in the new namespace.</p> <p>Contains the base64-encoded version of the YAML rules file.</p> <p>For details about the rule groups namespace structure, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html">RuleGroupsNamespaceData</a>.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values to associate with the rule groups namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleGroupsNamespaceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_amp.types.rule_groups_namespace_data

    out["data"] = capo_amp.types.rule_groups_namespace_data.serialize_json(
        value["data"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRuleGroupsNamespaceRequest:
    out: CreateRuleGroupsNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceRequest.name required")
    if data.get("data") is not None:
        import capo_amp.types.rule_groups_namespace_data

        out["data"] = capo_amp.types.rule_groups_namespace_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("CreateRuleGroupsNamespaceRequest.data required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
