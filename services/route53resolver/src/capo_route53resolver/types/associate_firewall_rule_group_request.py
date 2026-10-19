"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateFirewallRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.mutation_protection_status
    import capo_route53resolver.types.name
    import capo_route53resolver.types.priority
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.tag_list


class AssociateFirewallRuleGroupRequest(TypedDict, closed=True):
    creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>"""
    firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule group. </p>"""
    vpc_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the VPC that you want to associate with the rule group. </p>"""
    priority: "capo_route53resolver.types.priority.Priority"
    """<p>The setting that determines the processing order of the rule group among the rule groups that you associate with the specified VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting. </p> <p>You must specify a unique priority for each rule group that you associate with a single VPC. To make it easier to insert rule groups later, leave space between the numbers, for example, use 101, 200, and so on. You can change the priority setting for a rule group association after you create it.</p> <p>The allowed values for <code>Priority</code> are between 100 and 9900.</p>"""
    name: "capo_route53resolver.types.name.Name"
    """<p>A name that lets you identify the association, to manage and use it.</p>"""
    mutation_protection: NotRequired[
        "capo_route53resolver.types.mutation_protection_status.MutationProtectionStatus"
    ]
    """<p>If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. When you create the association, the default setting is <code>DISABLED</code>. </p>"""
    tags: NotRequired["capo_route53resolver.types.tag_list.TagList"]
    """<p>A list of the tag keys and values that you want to associate with the rule group association. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFirewallRuleGroupRequest) -> dict:
    out: dict = {}
    out["CreatorRequestId"] = value["creator_request_id"]
    out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    out["VpcId"] = value["vpc_id"]
    out["Priority"] = value["priority"]
    out["Name"] = value["name"]
    if "mutation_protection" in value:
        import capo_route53resolver.types.mutation_protection_status

        out["MutationProtection"] = (
            capo_route53resolver.types.mutation_protection_status.serialize_aws_json_1_1(
                value["mutation_protection"]
            )
        )
    if "tags" in value:
        import capo_route53resolver.types.tag_list

        out["Tags"] = capo_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFirewallRuleGroupRequest:
    out: AssociateFirewallRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    else:
        out["creator_request_id"] = ""
    if data.get("FirewallRuleGroupId") is not None:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    else:
        out["firewall_rule_group_id"] = ""
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("MutationProtection") is not None:
        import capo_route53resolver.types.mutation_protection_status

        out["mutation_protection"] = (
            capo_route53resolver.types.mutation_protection_status.deserialize_aws_json_1_1(
                data["MutationProtection"]
            )
        )
    if data.get("Tags") is not None:
        import capo_route53resolver.types.tag_list

        out["tags"] = capo_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
