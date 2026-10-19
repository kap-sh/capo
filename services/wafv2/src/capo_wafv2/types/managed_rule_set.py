"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.label_name
    import capo_wafv2.types.published_versions
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.version_key_string


class ManagedRuleSet(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>"""
    id: "capo_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>"""
    arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the set that helps with identification. </p>"""
    published_versions: NotRequired[
        "capo_wafv2.types.published_versions.PublishedVersions"
    ]
    """<p>The versions of this managed rule set that are available for use by customers. </p>"""
    recommended_version: NotRequired[
        "capo_wafv2.types.version_key_string.VersionKeyString"
    ]
    """<p>The version that you would like your customers to use.</p>"""
    label_namespace: NotRequired["capo_wafv2.types.label_name.LabelName"]
    """<p>The label namespace prefix for the managed rule groups that are offered to customers from this managed rule set. All labels that are added by rules in the managed rule group have this prefix. </p> <ul> <li> <p>The syntax for the label namespace prefix for a managed rule group is the following: </p> <p> <code>awswaf:managed:<vendor>:<rule group name></code>:</p> </li> <li> <p>When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: </p> <p> <code><label namespace>:<label from rule></code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleSet) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["ARN"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "published_versions" in value:
        import capo_wafv2.types.published_versions

        out["PublishedVersions"] = (
            capo_wafv2.types.published_versions.serialize_aws_json_1_1(
                value["published_versions"]
            )
        )
    if "recommended_version" in value:
        out["RecommendedVersion"] = value["recommended_version"]
    if "label_namespace" in value:
        out["LabelNamespace"] = value["label_namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleSet:
    out: ManagedRuleSet = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    else:
        out["arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PublishedVersions") is not None:
        import capo_wafv2.types.published_versions

        out["published_versions"] = (
            capo_wafv2.types.published_versions.deserialize_aws_json_1_1(
                data["PublishedVersions"]
            )
        )
    if data.get("RecommendedVersion") is not None:
        out["recommended_version"] = data["RecommendedVersion"]
    if data.get("LabelNamespace") is not None:
        out["label_namespace"] = data["LabelNamespace"]
    return out
