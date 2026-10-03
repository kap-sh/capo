"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateStackSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.auto_deployment
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.description
    import capo_cloudformation.types.execution_role_name
    import capo_cloudformation.types.managed_execution
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.permission_models
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_set_name
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.template_body
    import capo_cloudformation.types.template_url


class CreateStackSetInput(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name to associate with the StackSet. The name must be unique in the Region where you create your StackSet.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A description of the StackSet. You can use the description to identify the StackSet's purpose or other important information.</p>"""
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>"""
    template_url: NotRequired["capo_cloudformation.types.template_url.TemplateURL"]
    """<p>The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. S3 static website URLs are not supported.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>"""
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The stack ID you are importing into a new StackSet. Specify the Amazon Resource Name (ARN) of the stack.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>The input parameters for the StackSet template.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>In some cases, you must explicitly acknowledge that your StackSet template contains certain capabilities in order for CloudFormation to create the StackSet and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new IAM users. For those StackSets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html">AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html">AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html">AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html">AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your StackSet template references one or more macros, you must create the StackSet directly from the processed template, without first reviewing the resulting changes in a change set. To create the StackSet directly, you must acknowledge this capability. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> <important> <p>StackSets with service-managed permissions don't currently support the use of macros in templates. (This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a StackSet with service-managed permissions, if you reference a macro in your template the StackSet operation will fail.</p> </important> </li> </ul>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>The key-value pairs to associate with this StackSet and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the StackSet is not created.</p>"""
    administration_role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to use to create this StackSet.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Valid only if the permissions model is <code>SELF_MANAGED</code>.</p>"""
    execution_role_name: NotRequired[
        "capo_cloudformation.types.execution_role_name.ExecutionRoleName"
    ]
    """<p>The name of the IAM execution role to use to create the StackSet. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the StackSet operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their StackSets.</p> <p>Valid only if the permissions model is <code>SELF_MANAGED</code>.</p>"""
    permission_model: NotRequired[
        "capo_cloudformation.types.permission_models.PermissionModels"
    ]
    """<p>Describes how the IAM roles required for StackSet operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html">Activate trusted access for StackSets with Organizations</a>.</p> </li> </ul>"""
    auto_deployment: NotRequired[
        "capo_cloudformation.types.auto_deployment.AutoDeployment"
    ]
    """<p>Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html">Enable or disable automatic deployments for StackSets in Organizations</a> in the <i>CloudFormation User Guide</i>.</p> <p>Required if the permissions model is <code>SERVICE_MANAGED</code>. (Not used with self-managed permissions.)</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>To create a StackSet with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a StackSet with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>StackSets with service-managed permissions are created in the management account, including StackSets that are created by delegated administrators.</p> <p>Valid only if the permissions model is <code>SERVICE_MANAGED</code>.</p>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another StackSet with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>"""
    managed_execution: NotRequired[
        "capo_cloudformation.types.managed_execution.ManagedExecution"
    ]
    """<p>Describes whether CloudFormation performs non-conflicting operations concurrently and queues conflicting operations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateStackSetInput, pairs: list[tuple[str, str]], prefix: str
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
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
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
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )
    if "managed_execution" in value:
        import capo_cloudformation.types.managed_execution

        capo_cloudformation.types.managed_execution.serialize_query(
            value["managed_execution"], pairs, f"{key_prefix}ManagedExecution"
        )


def deserialize_query(el: Element) -> CreateStackSetInput:
    out: CreateStackSetInput = {}  # type: ignore[typeddict-item]
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
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
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
    child_administration_role_arn = el.find("AdministrationRoleARN")
    if child_administration_role_arn is not None:
        out["administration_role_arn"] = str(child_administration_role_arn.text or "")
    child_execution_role_name = el.find("ExecutionRoleName")
    if child_execution_role_name is not None:
        out["execution_role_name"] = str(child_execution_role_name.text or "")
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
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_managed_execution = el.find("ManagedExecution")
    if child_managed_execution is not None:
        import capo_cloudformation.types.managed_execution

        out["managed_execution"] = (
            capo_cloudformation.types.managed_execution.deserialize_query(
                child_managed_execution
            )
        )
    return out
