"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateStackSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account_list
    import capo_cloudformation.types.auto_deployment
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.deployment_targets
    import capo_cloudformation.types.description
    import capo_cloudformation.types.execution_role_name
    import capo_cloudformation.types.managed_execution
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.permission_models
    import capo_cloudformation.types.region_list
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.stack_set_name
    import capo_cloudformation.types.stack_set_operation_preferences
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.template_body
    import capo_cloudformation.types.template_url
    import capo_cloudformation.types.use_previous_template


class UpdateStackSetInput(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name or unique ID of the StackSet that you want to update.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A brief description of updates that you are making.</p>"""
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>"""
    template_url: NotRequired["capo_cloudformation.types.template_url.TemplateURL"]
    """<p>The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. S3 static website URLs are not supported.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>"""
    use_previous_template: NotRequired[
        "capo_cloudformation.types.use_previous_template.UsePreviousTemplate"
    ]
    """<p>Use the existing template that's associated with the StackSet that you're updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>A list of input parameters for the StackSet template.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the StackSet and its associated stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html">AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html">AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html">AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html">AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your StackSet template references one or more macros, you must update the StackSet directly from the processed template, without first reviewing the resulting changes in a change set. To update the StackSet directly, you must acknowledge this capability. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> <important> <p>StackSets with service-managed permissions do not currently support the use of macros in templates. (This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a StackSet with service-managed permissions, if you reference a macro in your template the StackSet operation will fail.</p> </important> </li> </ul>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>The key-value pairs to associate with this StackSet and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.</p> <p>If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this StackSet. This means:</p> <ul> <li> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags.</p> </li> <li> <p>If you specify <i>any</i> tags using this parameter, you must specify <i>all</i> the tags that you want associated with this StackSet, even tags you've specified before (for example, when creating the StackSet or during a previous update of the StackSet.). Any tags that you don't include in the updated list of tags are removed from the StackSet, and therefore from the stacks and resources as well.</p> </li> <li> <p>If you specify an empty value, CloudFormation removes all currently associated tags.</p> </li> </ul> <p>If you specify new tags as part of an <code>UpdateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the StackSet from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the StackSet, and checks to see if you have permission to untag resources. If you don't have the necessary permission(s), the entire <code>UpdateStackSet</code> action fails with an <code>access denied</code> error, and the StackSet is not updated.</p>"""
    operation_preferences: NotRequired[
        "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
    ]
    """<p>Preferences for how CloudFormation performs this StackSet operation.</p>"""
    administration_role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>[Self-managed permissions] The Amazon Resource Name (ARN) of the IAM role to use to update this StackSet.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specified a customized administrator role when you created the StackSet, you must specify a customized administrator role, even if it is the same customized administrator role used with this StackSet previously.</p>"""
    execution_role_name: NotRequired[
        "capo_cloudformation.types.execution_role_name.ExecutionRoleName"
    ]
    """<p>[Self-managed permissions] The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the StackSet operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their StackSets.</p> <p>If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the StackSet, so long as you have permissions to perform operations on the StackSet.</p>"""
    deployment_targets: NotRequired[
        "capo_cloudformation.types.deployment_targets.DeploymentTargets"
    ]
    """<p>[Service-managed permissions] The Organizations accounts in which to update associated stack instances.</p> <p>To update all the stack instances associated with this StackSet, do not specify <code>DeploymentTargets</code> or <code>Regions</code>.</p> <p>If the StackSet update includes changes to the template (that is, if <code>TemplateBody</code> or <code>TemplateURL</code> is specified), or the <code>Parameters</code>, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the StackSet update doesn't include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>"""
    permission_model: NotRequired[
        "capo_cloudformation.types.permission_models.PermissionModels"
    ]
    """<p>Describes how the IAM roles required for StackSet operations are created. You cannot modify <code>PermissionModel</code> if there are stack instances associated with your stack set.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html">Activate trusted access for StackSets with Organizations</a>.</p> </li> </ul>"""
    auto_deployment: NotRequired[
        "capo_cloudformation.types.auto_deployment.AutoDeployment"
    ]
    """<p>[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU). For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html">Enable or disable automatic deployments for StackSets in Organizations</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specify <code>AutoDeployment</code>, don't specify <code>DeploymentTargets</code> or <code>Regions</code>.</p>"""
    operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique ID for this StackSet operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the StackSet operation only once, even if you retry the request multiple times. You might retry StackSet operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, CloudFormation generates one automatically.</p> <p>Repeating this StackSet operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>"""
    accounts: NotRequired["capo_cloudformation.types.account_list.AccountList"]
    """<p>[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update StackSet instances.</p> <p>To update <i>all</i> the stack instances associated with this StackSet, don't specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the StackSet update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the StackSet update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.</p>"""
    regions: NotRequired["capo_cloudformation.types.region_list.RegionList"]
    """<p>The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update StackSet instances.</p> <p>To update <i>all</i> the stack instances associated with this StackSet, do not specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the StackSet update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Regions. If the StackSet update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>"""
    managed_execution: NotRequired[
        "capo_cloudformation.types.managed_execution.ManagedExecution"
    ]
    """<p>Describes whether CloudFormation performs non-conflicting operations concurrently and queues conflicting operations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateStackSetInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "template_body" in value:
        pairs.append((f"{key_prefix}TemplateBody", str(value["template_body"])))
    if "template_url" in value:
        pairs.append((f"{key_prefix}TemplateURL", str(value["template_url"])))
    if "use_previous_template" in value:
        pairs.append(
            (
                f"{key_prefix}UsePreviousTemplate",
                "true" if value["use_previous_template"] else "false",
            )
        )
    if "parameters" in value:
        import capo_cloudformation.types.parameters

        capo_cloudformation.types.parameters.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "capabilities" in value:
        import capo_cloudformation.types.capabilities

        capo_cloudformation.types.capabilities.serialize_query(
            value["capabilities"], pairs, f"{key_prefix}Capabilities"
        )
    if "tags" in value:
        import capo_cloudformation.types.tags

        capo_cloudformation.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "operation_preferences" in value:
        import capo_cloudformation.types.stack_set_operation_preferences

        capo_cloudformation.types.stack_set_operation_preferences.serialize_query(
            value["operation_preferences"], pairs, f"{key_prefix}OperationPreferences"
        )
    if "administration_role_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AdministrationRoleARN",
                str(value["administration_role_arn"]),
            )
        )
    if "execution_role_name" in value:
        pairs.append(
            (f"{key_prefix}ExecutionRoleName", str(value["execution_role_name"]))
        )
    if "deployment_targets" in value:
        import capo_cloudformation.types.deployment_targets

        capo_cloudformation.types.deployment_targets.serialize_query(
            value["deployment_targets"], pairs, f"{key_prefix}DeploymentTargets"
        )
    if "permission_model" in value:
        import capo_cloudformation.types.permission_models

        capo_cloudformation.types.permission_models.serialize_query(
            value["permission_model"], pairs, f"{key_prefix}PermissionModel"
        )
    if "auto_deployment" in value:
        import capo_cloudformation.types.auto_deployment

        capo_cloudformation.types.auto_deployment.serialize_query(
            value["auto_deployment"], pairs, f"{key_prefix}AutoDeployment"
        )
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))
    if "accounts" in value:
        import capo_cloudformation.types.account_list

        capo_cloudformation.types.account_list.serialize_query(
            value["accounts"], pairs, f"{key_prefix}Accounts"
        )
    if "regions" in value:
        import capo_cloudformation.types.region_list

        capo_cloudformation.types.region_list.serialize_query(
            value["regions"], pairs, f"{key_prefix}Regions"
        )
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )
    if "managed_execution" in value:
        import capo_cloudformation.types.managed_execution

        capo_cloudformation.types.managed_execution.serialize_query(
            value["managed_execution"], pairs, f"{key_prefix}ManagedExecution"
        )


def deserialize_query(el: Element) -> UpdateStackSetInput:
    out: UpdateStackSetInput = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_template_url = el.find("TemplateURL")
    if child_template_url is not None:
        out["template_url"] = str(child_template_url.text or "")
    child_use_previous_template = el.find("UsePreviousTemplate")
    if child_use_previous_template is not None:
        out["use_previous_template"] = (
            child_use_previous_template.text or ""
        ).lower() == "true"
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudformation.types.parameters

        out["parameters"] = capo_cloudformation.types.parameters.deserialize_query(
            child_parameters
        )
    child_capabilities = el.find("Capabilities")
    if child_capabilities is not None:
        import capo_cloudformation.types.capabilities

        out["capabilities"] = capo_cloudformation.types.capabilities.deserialize_query(
            child_capabilities
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudformation.types.tags

        out["tags"] = capo_cloudformation.types.tags.deserialize_query(child_tags)
    child_operation_preferences = el.find("OperationPreferences")
    if child_operation_preferences is not None:
        import capo_cloudformation.types.stack_set_operation_preferences

        out["operation_preferences"] = (
            capo_cloudformation.types.stack_set_operation_preferences.deserialize_query(
                child_operation_preferences
            )
        )
    child_administration_role_arn = el.find("AdministrationRoleARN")
    if child_administration_role_arn is not None:
        out["administration_role_arn"] = str(child_administration_role_arn.text or "")
    child_execution_role_name = el.find("ExecutionRoleName")
    if child_execution_role_name is not None:
        out["execution_role_name"] = str(child_execution_role_name.text or "")
    child_deployment_targets = el.find("DeploymentTargets")
    if child_deployment_targets is not None:
        import capo_cloudformation.types.deployment_targets

        out["deployment_targets"] = (
            capo_cloudformation.types.deployment_targets.deserialize_query(
                child_deployment_targets
            )
        )
    child_permission_model = el.find("PermissionModel")
    if child_permission_model is not None:
        import capo_cloudformation.types.permission_models

        out["permission_model"] = (
            capo_cloudformation.types.permission_models.deserialize_query(
                child_permission_model
            )
        )
    child_auto_deployment = el.find("AutoDeployment")
    if child_auto_deployment is not None:
        import capo_cloudformation.types.auto_deployment

        out["auto_deployment"] = (
            capo_cloudformation.types.auto_deployment.deserialize_query(
                child_auto_deployment
            )
        )
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_accounts = el.find("Accounts")
    if child_accounts is not None:
        import capo_cloudformation.types.account_list

        out["accounts"] = capo_cloudformation.types.account_list.deserialize_query(
            child_accounts
        )
    child_regions = el.find("Regions")
    if child_regions is not None:
        import capo_cloudformation.types.region_list

        out["regions"] = capo_cloudformation.types.region_list.deserialize_query(
            child_regions
        )
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    child_managed_execution = el.find("ManagedExecution")
    if child_managed_execution is not None:
        import capo_cloudformation.types.managed_execution

        out["managed_execution"] = (
            capo_cloudformation.types.managed_execution.deserialize_query(
                child_managed_execution
            )
        )
    return out
