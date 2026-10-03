"""Generated from Smithy shape ``com.amazonaws.iam#SimulatePrincipalPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.action_name_list_type
    import capo_iam.types.arn_type
    import capo_iam.types.context_entry_list_type
    import capo_iam.types.marker_type
    import capo_iam.types.max_items_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.policy_exclusions_list_type
    import capo_iam.types.resource_handling_option_type
    import capo_iam.types.resource_name_list_type
    import capo_iam.types.resource_name_type
    import capo_iam.types.simulation_policy_list_type


class SimulatePrincipalPolicyRequest(TypedDict, closed=True):
    policy_source_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation. If you specify a user, group, or role, the simulation includes all policies that are associated with that entity. If you specify a user, the simulation also includes all policies that are attached to any groups the user belongs to.</p> <p>The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length">IAM and STS character quotas</a>.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    policy_input_list: NotRequired[
        "capo_iam.types.simulation_policy_list_type.SimulationPolicyListType"
    ]
    r"""<p>An optional list of additional policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    permissions_boundary_policy_input_list: NotRequired[
        "capo_iam.types.simulation_policy_list_type.SimulationPolicyListType"
    ]
    r"""<p>The IAM permissions boundary policy to simulate. The permissions boundary sets the maximum permissions that the entity can have. You can input only one permissions boundary when you pass a policy to this operation. An IAM entity can only have one permissions boundary in effect at a time. For example, if a permissions boundary is attached to an entity and you pass in a different permissions boundary policy using this parameter, then the new permissions boundary policy is used for the simulation. For more information about permissions boundaries, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM entities</a> in the <i>IAM User Guide</i>. The policy input is specified as a string containing the complete, valid JSON text of a permissions boundary policy.</p> <p>The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length">IAM and STS character quotas</a>.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    policy_exclusion_list: NotRequired[
        "capo_iam.types.policy_exclusions_list_type.PolicyExclusionsListType"
    ]
    """<p>A list of policies to exclude from the simulation. Use this parameter to test what the simulation result would be if a policy were removed, without changing which policies are actually attached to the principal identified by <code>PolicySourceArn</code>.</p> <p>Each entry is a <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyIdentifier.html">PolicyIdentifier</a> that identifies one or more policies to exclude by policy type, by Amazon Resource Name (ARN), or by the name of an inline policy and the entity it is attached to.</p> <p>Syntactically invalid identifiers, such as malformed ARNs or wildcards in disallowed positions, cause the request to fail with an <code>InvalidInput</code> error. Syntactically valid identifiers that don't match any attached policy are ignored. Resource control policies (RCPs) are not supported in this release; identifiers that target RCPs are also ignored.</p>"""
    action_names: "capo_iam.types.action_name_list_type.ActionNameListType"
    """<p>A list of names of API operations to evaluate in the simulation. Each operation is evaluated for each resource. Each operation must include the service identifier, such as <code>iam:CreateUser</code>.</p>"""
    resource_arns: NotRequired[
        "capo_iam.types.resource_name_list_type.ResourceNameListType"
    ]
    """<p>A list of ARNs of Amazon Web Services resources to include in the simulation. If this parameter is not provided, then the value defaults to <code>*</code> (all resources). Each API in the <code>ActionNames</code> parameter is evaluated for each resource in this list. The simulation determines the access result (allowed or denied) of each combination and reports it in the response. You can simulate resources that don't exist in your account.</p> <p>The simulation does not automatically retrieve policies for the specified resources. If you want to include a resource policy in the simulation, then you must include the policy as a string in the <code>ResourcePolicy</code> parameter.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p> <note> <p>Simulation of resource-based policies isn't supported for IAM roles.</p> </note>"""
    resource_policy: NotRequired[
        "capo_iam.types.policy_document_type.policyDocumentType"
    ]
    r"""<p>A resource-based policy to include in the simulation provided as a string. Each resource in the simulation is treated as if it had this policy attached. You can include only one resource-based policy in a simulation.</p> <p>The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length">IAM and STS character quotas</a>.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul> <note> <p>Simulation of resource-based policies isn't supported for IAM roles.</p> </note>"""
    resource_owner: NotRequired["capo_iam.types.resource_name_type.ResourceNameType"]
    """<p>An Amazon Web Services account ID that specifies the owner of any simulated resource that does not identify its owner in the resource ARN. Examples of resource ARNs include an S3 bucket or object. If <code>ResourceOwner</code> is specified, it is also used as the account owner of any <code>ResourcePolicy</code> included in the simulation. If the <code>ResourceOwner</code> parameter is not specified, then the owner of the resources and the resource policy defaults to the account of the identity provided in <code>CallerArn</code>. This parameter is required only if you specify a resource-based policy and account that owns the resource is different from the account that owns the simulated calling user <code>CallerArn</code>.</p>"""
    caller_arn: NotRequired["capo_iam.types.resource_name_type.ResourceNameType"]
    """<p>The ARN of the IAM user, group, or role that you want to specify as the simulated caller of the API operations. If you do not specify a <code>CallerArn</code>, it defaults to the ARN of the user, group, or role that you specify in <code>PolicySourceArn</code>. If you include both a <code>PolicySourceArn</code> (for example, <code>arn:aws:iam::123456789012:user/David</code>) and a <code>CallerArn</code> (for example, <code>arn:aws:iam::123456789012:user/Bob</code>), the result is that you simulate calling the API operations as Bob, as if Bob had David's policies.</p> <p>You can specify the ARN of an IAM user, group, or role. You cannot specify the ARN of an assumed role, federated user, or a service principal.</p> <p> <code>CallerArn</code> is required if you include a <code>ResourcePolicy</code> and the <code>PolicySourceArn</code> is not the ARN for an IAM user, group, or role. This is required so that the resource-based policy's <code>Principal</code> element has a value to use in evaluating the policy.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    context_entries: NotRequired[
        "capo_iam.types.context_entry_list_type.ContextEntryListType"
    ]
    """<p>A list of context keys and corresponding values for the simulation to use. Whenever a context key is evaluated in one of the simulated IAM permissions policies, the corresponding value is supplied.</p>"""
    resource_handling_option: NotRequired[
        "capo_iam.types.resource_handling_option_type.ResourceHandlingOptionType"
    ]
    """<p>Specifies the type of simulation to run. Different API operations that support resource-based policies require different combinations of resources. By specifying the type of simulation to run, you enable the policy simulator to enforce the presence of the required resources to ensure reliable simulation results. If your simulation does not match one of the following scenarios, then you can omit this parameter. The following list shows each of the supported scenario values and the resources that you must define to run the simulation.</p> <p>Each of the Amazon EC2 scenarios requires that you specify instance, image, and security group resources. If your scenario includes an EBS volume, then you must specify that volume as a resource. If the Amazon EC2 scenario includes VPC, then you must supply the network interface resource. If it includes an IP subnet, then you must specify the subnet resource. For more information on the Amazon EC2 scenario options, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html">Supported platforms</a> in the <i>Amazon EC2 User Guide</i>.</p> <ul> <li> <p> <b>EC2-VPC-InstanceStore</b> </p> <p>instance, image, security group, network interface</p> </li> <li> <p> <b>EC2-VPC-InstanceStore-Subnet</b> </p> <p>instance, image, security group, network interface, subnet</p> </li> <li> <p> <b>EC2-VPC-EBS</b> </p> <p>instance, image, security group, network interface, volume</p> </li> <li> <p> <b>EC2-VPC-EBS-Subnet</b> </p> <p>instance, image, security group, network interface, subnet, volume</p> </li> </ul>"""
    max_items: NotRequired["capo_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>.</p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from.</p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SimulatePrincipalPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicySourceArn", str(value["policy_source_arn"])))
    if "policy_input_list" in value:
        import capo_iam.types.simulation_policy_list_type

        capo_iam.types.simulation_policy_list_type.serialize_query(
            value["policy_input_list"], pairs, f"{key_prefix}PolicyInputList"
        )
    if "permissions_boundary_policy_input_list" in value:
        import capo_iam.types.simulation_policy_list_type

        capo_iam.types.simulation_policy_list_type.serialize_query(
            value["permissions_boundary_policy_input_list"],
            pairs,
            f"{key_prefix}PermissionsBoundaryPolicyInputList",
        )
    if "policy_exclusion_list" in value:
        import capo_iam.types.policy_exclusions_list_type

        capo_iam.types.policy_exclusions_list_type.serialize_query(
            value["policy_exclusion_list"], pairs, f"{key_prefix}PolicyExclusionList"
        )
    import capo_iam.types.action_name_list_type

    capo_iam.types.action_name_list_type.serialize_query(
        value["action_names"], pairs, f"{key_prefix}ActionNames"
    )
    if "resource_arns" in value:
        import capo_iam.types.resource_name_list_type

        capo_iam.types.resource_name_list_type.serialize_query(
            value["resource_arns"], pairs, f"{key_prefix}ResourceArns"
        )
    if "resource_policy" in value:
        pairs.append((f"{key_prefix}ResourcePolicy", str(value["resource_policy"])))
    if "resource_owner" in value:
        pairs.append((f"{key_prefix}ResourceOwner", str(value["resource_owner"])))
    if "caller_arn" in value:
        pairs.append((f"{key_prefix}CallerArn", str(value["caller_arn"])))
    if "context_entries" in value:
        import capo_iam.types.context_entry_list_type

        capo_iam.types.context_entry_list_type.serialize_query(
            value["context_entries"], pairs, f"{key_prefix}ContextEntries"
        )
    if "resource_handling_option" in value:
        pairs.append(
            (
                f"{key_prefix}ResourceHandlingOption",
                str(value["resource_handling_option"]),
            )
        )
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> SimulatePrincipalPolicyRequest:
    out: SimulatePrincipalPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_source_arn = el.find("PolicySourceArn")
    if child_policy_source_arn is not None:
        out["policy_source_arn"] = str(child_policy_source_arn.text or "")
    else:
        raise DeserializationError(
            "SimulatePrincipalPolicyRequest.policy_source_arn required"
        )
    child_policy_input_list = el.find("PolicyInputList")
    if child_policy_input_list is not None:
        import capo_iam.types.simulation_policy_list_type

        out["policy_input_list"] = (
            capo_iam.types.simulation_policy_list_type.deserialize_query(
                child_policy_input_list
            )
        )
    child_permissions_boundary_policy_input_list = el.find(
        "PermissionsBoundaryPolicyInputList"
    )
    if child_permissions_boundary_policy_input_list is not None:
        import capo_iam.types.simulation_policy_list_type

        out["permissions_boundary_policy_input_list"] = (
            capo_iam.types.simulation_policy_list_type.deserialize_query(
                child_permissions_boundary_policy_input_list
            )
        )
    child_policy_exclusion_list = el.find("PolicyExclusionList")
    if child_policy_exclusion_list is not None:
        import capo_iam.types.policy_exclusions_list_type

        out["policy_exclusion_list"] = (
            capo_iam.types.policy_exclusions_list_type.deserialize_query(
                child_policy_exclusion_list
            )
        )
    child_action_names = el.find("ActionNames")
    if child_action_names is not None:
        import capo_iam.types.action_name_list_type

        out["action_names"] = capo_iam.types.action_name_list_type.deserialize_query(
            child_action_names
        )
    else:
        raise DeserializationError(
            "SimulatePrincipalPolicyRequest.action_names required"
        )
    child_resource_arns = el.find("ResourceArns")
    if child_resource_arns is not None:
        import capo_iam.types.resource_name_list_type

        out["resource_arns"] = capo_iam.types.resource_name_list_type.deserialize_query(
            child_resource_arns
        )
    child_resource_policy = el.find("ResourcePolicy")
    if child_resource_policy is not None:
        out["resource_policy"] = str(child_resource_policy.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    child_caller_arn = el.find("CallerArn")
    if child_caller_arn is not None:
        out["caller_arn"] = str(child_caller_arn.text or "")
    child_context_entries = el.find("ContextEntries")
    if child_context_entries is not None:
        import capo_iam.types.context_entry_list_type

        out["context_entries"] = (
            capo_iam.types.context_entry_list_type.deserialize_query(
                child_context_entries
            )
        )
    child_resource_handling_option = el.find("ResourceHandlingOption")
    if child_resource_handling_option is not None:
        out["resource_handling_option"] = str(child_resource_handling_option.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
