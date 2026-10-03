"""Generated from Smithy shape ``com.amazonaws.fms#Policy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.customer_policy_scope_map
    import capo_fms.types.customer_policy_status
    import capo_fms.types.policy_id
    import capo_fms.types.policy_update_token
    import capo_fms.types.resource_description
    import capo_fms.types.resource_name
    import capo_fms.types.resource_set_ids
    import capo_fms.types.resource_tag_logical_operator
    import capo_fms.types.resource_tags
    import capo_fms.types.resource_type
    import capo_fms.types.resource_type_list
    import capo_fms.types.security_service_policy_data


class Policy(TypedDict, closed=True):
    policy_id: NotRequired["capo_fms.types.policy_id.PolicyId"]
    """<p>The ID of the Firewall Manager policy.</p>"""
    policy_name: "capo_fms.types.resource_name.ResourceName"
    """<p>The name of the Firewall Manager policy.</p>"""
    policy_update_token: NotRequired[
        "capo_fms.types.policy_update_token.PolicyUpdateToken"
    ]
    """<p>A unique identifier for each update to the policy. When issuing a <code>PutPolicy</code> request, the <code>PolicyUpdateToken</code> in the request must match the <code>PolicyUpdateToken</code> of the current policy version. To get the <code>PolicyUpdateToken</code> of the current policy version, use a <code>GetPolicy</code> request.</p>"""
    security_service_policy_data: (
        "capo_fms.types.security_service_policy_data.SecurityServicePolicyData"
    )
    """<p>Details about the security service that is being used to protect the resources.</p>"""
    resource_type: "capo_fms.types.resource_type.ResourceType"
    """<p>The type of resource protected by or in scope of the policy. This is in the format shown in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a>. To apply this policy to multiple resource types, specify a resource type of <code>ResourceTypeList</code> and then specify the resource types in a <code>ResourceTypeList</code>.</p> <p>The following are valid resource types for each Firewall Manager policy type:</p> <ul> <li> <p>Amazon Web Services WAF Classic - <code>AWS::ApiGateway::Stage</code>, <code>AWS::CloudFront::Distribution</code>, and <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code>.</p> </li> <li> <p>WAF - <code>AWS::ApiGateway::Stage</code>, <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code>, and <code>AWS::CloudFront::Distribution</code>.</p> </li> <li> <p>Shield Advanced - <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code>, <code>AWS::ElasticLoadBalancing::LoadBalancer</code>, <code>AWS::EC2::EIP</code>, and <code>AWS::CloudFront::Distribution</code>.</p> </li> <li> <p>Network ACL - <code>AWS::EC2::Subnet</code>.</p> </li> <li> <p>Security group usage audit - <code>AWS::EC2::SecurityGroup</code>.</p> </li> <li> <p>Security group content audit - <code>AWS::EC2::SecurityGroup</code>, <code>AWS::EC2::NetworkInterface</code>, and <code>AWS::EC2::Instance</code>.</p> </li> <li> <p>DNS Firewall, Network Firewall, and third-party firewall - <code>AWS::EC2::VPC</code>.</p> </li> </ul>"""
    resource_type_list: NotRequired[
        "capo_fms.types.resource_type_list.ResourceTypeList"
    ]
    """<p>An array of <code>ResourceType</code> objects. Use this only to specify multiple resource types. To specify a single resource type, use <code>ResourceType</code>.</p>"""
    resource_tags: NotRequired["capo_fms.types.resource_tags.ResourceTags"]
    """<p>An array of <code>ResourceTag</code> objects.</p>"""
    exclude_resource_tags: "capo_fms.types.boolean.Boolean"
    """<p>If set to <code>True</code>, resources with the tags that are specified in the <code>ResourceTag</code> array are not in scope of the policy. If set to <code>False</code>, and the <code>ResourceTag</code> array is not null, only resources with the specified tags are in scope of the policy.</p>"""
    remediation_enabled: "capo_fms.types.boolean.Boolean"
    """<p>Indicates if the policy should be automatically applied to new resources.</p>"""
    delete_unused_fm_managed_resources: "capo_fms.types.boolean.Boolean"
    """<p>Indicates whether Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope. </p> <p>By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources. </p> <p>This option is not available for Shield Advanced or WAF Classic policies.</p>"""
    include_map: NotRequired[
        "capo_fms.types.customer_policy_scope_map.CustomerPolicyScopeMap"
    ]
    """<p>Specifies the Amazon Web Services account IDs and Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.</p> <p>You can specify inclusions or exclusions, but not both. If you specify an <code>IncludeMap</code>, Firewall Manager applies the policy to all accounts specified by the <code>IncludeMap</code>, and does not evaluate any <code>ExcludeMap</code> specifications. If you do not specify an <code>IncludeMap</code>, then Firewall Manager applies the policy to all accounts except for those specified by the <code>ExcludeMap</code>.</p> <p>You can specify account IDs, OUs, or a combination: </p> <ul> <li> <p>Specify account IDs by setting the key to <code>ACCOUNT</code>. For example, the following is a valid map: <code>{“ACCOUNT” : [“accountID1”, “accountID2”]}</code>.</p> </li> <li> <p>Specify OUs by setting the key to <code>ORG_UNIT</code>. For example, the following is a valid map: <code>{“ORG_UNIT” : [“ouid111”, “ouid112”]}</code>.</p> </li> <li> <p>Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: <code>{“ACCOUNT” : [“accountID1”, “accountID2”], “ORG_UNIT” : [“ouid111”, “ouid112”]}</code>.</p> </li> </ul>"""
    exclude_map: NotRequired[
        "capo_fms.types.customer_policy_scope_map.CustomerPolicyScopeMap"
    ]
    """<p>Specifies the Amazon Web Services account IDs and Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.</p> <p>You can specify inclusions or exclusions, but not both. If you specify an <code>IncludeMap</code>, Firewall Manager applies the policy to all accounts specified by the <code>IncludeMap</code>, and does not evaluate any <code>ExcludeMap</code> specifications. If you do not specify an <code>IncludeMap</code>, then Firewall Manager applies the policy to all accounts except for those specified by the <code>ExcludeMap</code>.</p> <p>You can specify account IDs, OUs, or a combination: </p> <ul> <li> <p>Specify account IDs by setting the key to <code>ACCOUNT</code>. For example, the following is a valid map: <code>{“ACCOUNT” : [“accountID1”, “accountID2”]}</code>.</p> </li> <li> <p>Specify OUs by setting the key to <code>ORG_UNIT</code>. For example, the following is a valid map: <code>{“ORG_UNIT” : [“ouid111”, “ouid112”]}</code>.</p> </li> <li> <p>Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: <code>{“ACCOUNT” : [“accountID1”, “accountID2”], “ORG_UNIT” : [“ouid111”, “ouid112”]}</code>.</p> </li> </ul>"""
    resource_set_ids: NotRequired["capo_fms.types.resource_set_ids.ResourceSetIds"]
    """<p>The unique identifiers of the resource sets used by the policy.</p>"""
    policy_description: NotRequired[
        "capo_fms.types.resource_description.ResourceDescription"
    ]
    """<p>Your description of the Firewall Manager policy.</p>"""
    policy_status: NotRequired[
        "capo_fms.types.customer_policy_status.CustomerPolicyStatus"
    ]
    """<p>Indicates whether the policy is in or out of an admin's policy or Region scope.</p> <ul> <li> <p> <code>ACTIVE</code> - The administrator can manage and delete the policy.</p> </li> <li> <p> <code>OUT_OF_ADMIN_SCOPE</code> - The administrator can view the policy, but they can't edit or delete the policy. Existing policy protections stay in place. Any new resources that come into scope of the policy won't be protected.</p> </li> </ul>"""
    resource_tag_logical_operator: NotRequired[
        "capo_fms.types.resource_tag_logical_operator.ResourceTagLogicalOperator"
    ]
    """<p>Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag.</p> <p>Default: <code>AND</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Policy) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    out["PolicyName"] = value["policy_name"]
    if "policy_update_token" in value:
        out["PolicyUpdateToken"] = value["policy_update_token"]
    import capo_fms.types.security_service_policy_data

    out["SecurityServicePolicyData"] = (
        capo_fms.types.security_service_policy_data.serialize_aws_json_1_1(
            value["security_service_policy_data"]
        )
    )
    out["ResourceType"] = value["resource_type"]
    if "resource_type_list" in value:
        import capo_fms.types.resource_type_list

        out["ResourceTypeList"] = (
            capo_fms.types.resource_type_list.serialize_aws_json_1_1(
                value["resource_type_list"]
            )
        )
    if "resource_tags" in value:
        import capo_fms.types.resource_tags

        out["ResourceTags"] = capo_fms.types.resource_tags.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    out["ExcludeResourceTags"] = value.get("exclude_resource_tags", False)
    out["RemediationEnabled"] = value.get("remediation_enabled", False)
    out["DeleteUnusedFMManagedResources"] = value.get(
        "delete_unused_fm_managed_resources", False
    )
    if "include_map" in value:
        import capo_fms.types.customer_policy_scope_map

        out["IncludeMap"] = (
            capo_fms.types.customer_policy_scope_map.serialize_aws_json_1_1(
                value["include_map"]
            )
        )
    if "exclude_map" in value:
        import capo_fms.types.customer_policy_scope_map

        out["ExcludeMap"] = (
            capo_fms.types.customer_policy_scope_map.serialize_aws_json_1_1(
                value["exclude_map"]
            )
        )
    if "resource_set_ids" in value:
        import capo_fms.types.resource_set_ids

        out["ResourceSetIds"] = capo_fms.types.resource_set_ids.serialize_aws_json_1_1(
            value["resource_set_ids"]
        )
    if "policy_description" in value:
        out["PolicyDescription"] = value["policy_description"]
    if "policy_status" in value:
        import capo_fms.types.customer_policy_status

        out["PolicyStatus"] = (
            capo_fms.types.customer_policy_status.serialize_aws_json_1_1(
                value["policy_status"]
            )
        )
    if "resource_tag_logical_operator" in value:
        import capo_fms.types.resource_tag_logical_operator

        out["ResourceTagLogicalOperator"] = (
            capo_fms.types.resource_tag_logical_operator.serialize_aws_json_1_1(
                value["resource_tag_logical_operator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("Policy.policy_name required")
    if data.get("PolicyUpdateToken") is not None:
        out["policy_update_token"] = data["PolicyUpdateToken"]
    if data.get("SecurityServicePolicyData") is not None:
        import capo_fms.types.security_service_policy_data

        out["security_service_policy_data"] = (
            capo_fms.types.security_service_policy_data.deserialize_aws_json_1_1(
                data["SecurityServicePolicyData"]
            )
        )
    else:
        raise DeserializationError("Policy.security_service_policy_data required")
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("Policy.resource_type required")
    if data.get("ResourceTypeList") is not None:
        import capo_fms.types.resource_type_list

        out["resource_type_list"] = (
            capo_fms.types.resource_type_list.deserialize_aws_json_1_1(
                data["ResourceTypeList"]
            )
        )
    if data.get("ResourceTags") is not None:
        import capo_fms.types.resource_tags

        out["resource_tags"] = capo_fms.types.resource_tags.deserialize_aws_json_1_1(
            data["ResourceTags"]
        )
    if data.get("ExcludeResourceTags") is not None:
        out["exclude_resource_tags"] = data["ExcludeResourceTags"]
    else:
        out["exclude_resource_tags"] = False
    if data.get("RemediationEnabled") is not None:
        out["remediation_enabled"] = data["RemediationEnabled"]
    else:
        out["remediation_enabled"] = False
    if data.get("DeleteUnusedFMManagedResources") is not None:
        out["delete_unused_fm_managed_resources"] = data[
            "DeleteUnusedFMManagedResources"
        ]
    else:
        out["delete_unused_fm_managed_resources"] = False
    if data.get("IncludeMap") is not None:
        import capo_fms.types.customer_policy_scope_map

        out["include_map"] = (
            capo_fms.types.customer_policy_scope_map.deserialize_aws_json_1_1(
                data["IncludeMap"]
            )
        )
    if data.get("ExcludeMap") is not None:
        import capo_fms.types.customer_policy_scope_map

        out["exclude_map"] = (
            capo_fms.types.customer_policy_scope_map.deserialize_aws_json_1_1(
                data["ExcludeMap"]
            )
        )
    if data.get("ResourceSetIds") is not None:
        import capo_fms.types.resource_set_ids

        out["resource_set_ids"] = (
            capo_fms.types.resource_set_ids.deserialize_aws_json_1_1(
                data["ResourceSetIds"]
            )
        )
    if data.get("PolicyDescription") is not None:
        out["policy_description"] = data["PolicyDescription"]
    if data.get("PolicyStatus") is not None:
        import capo_fms.types.customer_policy_status

        out["policy_status"] = (
            capo_fms.types.customer_policy_status.deserialize_aws_json_1_1(
                data["PolicyStatus"]
            )
        )
    if data.get("ResourceTagLogicalOperator") is not None:
        import capo_fms.types.resource_tag_logical_operator

        out["resource_tag_logical_operator"] = (
            capo_fms.types.resource_tag_logical_operator.deserialize_aws_json_1_1(
                data["ResourceTagLogicalOperator"]
            )
        )
    return out
