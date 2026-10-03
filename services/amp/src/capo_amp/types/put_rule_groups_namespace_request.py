"""Generated from Smithy shape ``com.amazonaws.amp#PutRuleGroupsNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.rule_groups_namespace_data
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.workspace_id


class PutRuleGroupsNamespaceRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where you are updating the rule groups namespace.</p>"""
    name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the rule groups namespace that you are updating.</p>"""
    data: "capo_amp.types.rule_groups_namespace_data.RuleGroupsNamespaceData"
    """<p>The new rules file to use in the namespace. A base64-encoded version of the YAML rule groups file.</p> <p>For details about the rule groups namespace structure, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html">RuleGroupsNamespaceData</a>.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRuleGroupsNamespaceRequest) -> dict:
    out: dict = {}
    import capo_amp.types.rule_groups_namespace_data

    out["data"] = capo_amp.types.rule_groups_namespace_data.serialize_json(
        value["data"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutRuleGroupsNamespaceRequest:
    out: PutRuleGroupsNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_amp.types.rule_groups_namespace_data

        out["data"] = capo_amp.types.rule_groups_namespace_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("PutRuleGroupsNamespaceRequest.data required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
