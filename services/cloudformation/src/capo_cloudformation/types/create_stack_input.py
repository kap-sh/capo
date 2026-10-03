"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateStackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.deployment_config
    import capo_cloudformation.types.disable_rollback
    import capo_cloudformation.types.disable_validation
    import capo_cloudformation.types.enable_termination_protection
    import capo_cloudformation.types.notification_ar_ns
    import capo_cloudformation.types.on_failure
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.resource_types
    import capo_cloudformation.types.retain_except_on_create
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.rollback_configuration
    import capo_cloudformation.types.stack_name
    import capo_cloudformation.types.stack_policy_body
    import capo_cloudformation.types.stack_policy_url
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.template_body
    import capo_cloudformation.types.template_url
    import capo_cloudformation.types.timeout_minutes


class CreateStackInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack.</p> <note> <p>A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can't be longer than 128 characters.</p> </note>"""
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify either <code>TemplateBody</code> or <code>TemplateURL</code>, but not both.</p>"""
    template_url: NotRequired["capo_cloudformation.types.template_url.TemplateURL"]
    """<p>The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.</p>"""
    disable_rollback: NotRequired[
        "capo_cloudformation.types.disable_rollback.DisableRollback"
    ]
    """<p>Set to <code>true</code> to disable rollback of the stack if stack creation failed. You can specify either <code>DisableRollback</code> or <code>OnFailure</code>, but not both.</p> <p>Default: <code>false</code> </p>"""
    rollback_configuration: NotRequired[
        "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
    ]
    """<p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>"""
    timeout_in_minutes: NotRequired[
        "capo_cloudformation.types.timeout_minutes.TimeoutMinutes"
    ]
    """<p>The amount of time that can pass before the stack status becomes <code>CREATE_FAILED</code>; if <code>DisableRollback</code> is not set or is set to <code>false</code>, the stack will be rolled back.</p>"""
    notification_ar_ns: NotRequired[
        "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
    ]
    """<p>The Amazon SNS topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html">AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html">AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html"> AWS::IAM::ManagedPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html">AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html">AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create the stack directly from the template using this capability.</p> <important> <p>You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> </li> </ul> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>"""
    resource_types: NotRequired[
        "capo_cloudformation.types.resource_types.ResourceTypes"
    ]
    """<p>Specifies which resource types you can work with, such as <code>AWS::EC2::Instance</code> or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html">Control CloudFormation access with Identity and Access Management</a>.</p> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>"""
    role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>"""
    on_failure: NotRequired["capo_cloudformation.types.on_failure.OnFailure"]
    """<p>Determines what action will be taken if stack creation fails. This must be one of: <code>DO_NOTHING</code>, <code>ROLLBACK</code>, or <code>DELETE</code>. You can specify either <code>OnFailure</code> or <code>DisableRollback</code>, but not both.</p> <note> <p>Although the default setting is <code>ROLLBACK</code>, there is one exception. This exception occurs when a StackSet attempts to deploy a stack instance and the stack instance fails to create successfully. In this case, the <code>CreateStack</code> call overrides the default setting and sets the value of <code>OnFailure</code> to <code>DELETE</code>.</p> </note> <p>Default: <code>ROLLBACK</code> </p>"""
    stack_policy_body: NotRequired[
        "capo_cloudformation.types.stack_policy_body.StackPolicyBody"
    ]
    """<p>Structure that contains the stack policy body. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html">Prevent updates to stack resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>"""
    stack_policy_url: NotRequired[
        "capo_cloudformation.types.stack_policy_url.StackPolicyURL"
    ]
    """<p>Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.</p>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>CreateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create a stack with the same name. You might retry <code>CreateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>"""
    enable_termination_protection: NotRequired[
        "capo_cloudformation.types.enable_termination_protection.EnableTerminationProtection"
    ]
    """<p>Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protect CloudFormation stacks from being deleted</a> in the <i>CloudFormation User Guide</i>. Termination protection is deactivated on stacks by default.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>"""
    retain_except_on_create: NotRequired[
        "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
    ]
    """<p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>"""
    deployment_config: NotRequired[
        "capo_cloudformation.types.deployment_config.DeploymentConfig"
    ]
    """<p>The deployment configuration for this stack operation, including the deployment mode.</p>"""
    disable_validation: NotRequired[
        "capo_cloudformation.types.disable_validation.DisableValidation"
    ]
    """<p> Set to <code>true</code> to disable pre-deployment validations in changeset or stack operations. </p> <p> Default: <code>false</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateStackInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "template_body" in value:
        pairs.append((f"{key_prefix}TemplateBody", str(value["template_body"])))
    if "template_url" in value:
        pairs.append((f"{key_prefix}TemplateURL", str(value["template_url"])))
    if "parameters" in value:
        import capo_cloudformation.types.parameters

        capo_cloudformation.types.parameters.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "disable_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}DisableRollback",
                "true" if value["disable_rollback"] else "false",
            )
        )
    if "rollback_configuration" in value:
        import capo_cloudformation.types.rollback_configuration

        capo_cloudformation.types.rollback_configuration.serialize_query(
            value["rollback_configuration"], pairs, f"{key_prefix}RollbackConfiguration"
        )
    if "timeout_in_minutes" in value:
        pairs.append(
            (f"{key_prefix}TimeoutInMinutes", str(value["timeout_in_minutes"]))
        )
    if "notification_ar_ns" in value:
        import capo_cloudformation.types.notification_ar_ns

        capo_cloudformation.types.notification_ar_ns.serialize_query(
            value["notification_ar_ns"], pairs, f"{key_prefix}NotificationARNs"
        )
    if "capabilities" in value:
        import capo_cloudformation.types.capabilities

        capo_cloudformation.types.capabilities.serialize_query(
            value["capabilities"], pairs, f"{key_prefix}Capabilities"
        )
    if "resource_types" in value:
        import capo_cloudformation.types.resource_types

        capo_cloudformation.types.resource_types.serialize_query(
            value["resource_types"], pairs, f"{key_prefix}ResourceTypes"
        )
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleARN", str(value["role_arn"])))
    if "on_failure" in value:
        import capo_cloudformation.types.on_failure

        capo_cloudformation.types.on_failure.serialize_query(
            value["on_failure"], pairs, f"{key_prefix}OnFailure"
        )
    if "stack_policy_body" in value:
        pairs.append((f"{key_prefix}StackPolicyBody", str(value["stack_policy_body"])))
    if "stack_policy_url" in value:
        pairs.append((f"{key_prefix}StackPolicyURL", str(value["stack_policy_url"])))
    if "tags" in value:
        import capo_cloudformation.types.tags

        capo_cloudformation.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )
    if "enable_termination_protection" in value:
        pairs.append(
            (
                f"{key_prefix}EnableTerminationProtection",
                "true" if value["enable_termination_protection"] else "false",
            )
        )
    if "retain_except_on_create" in value:
        pairs.append(
            (
                f"{key_prefix}RetainExceptOnCreate",
                "true" if value["retain_except_on_create"] else "false",
            )
        )
    if "deployment_config" in value:
        import capo_cloudformation.types.deployment_config

        capo_cloudformation.types.deployment_config.serialize_query(
            value["deployment_config"], pairs, f"{key_prefix}DeploymentConfig"
        )
    if "disable_validation" in value:
        pairs.append(
            (
                f"{key_prefix}DisableValidation",
                "true" if value["disable_validation"] else "false",
            )
        )


def deserialize_query(el: Element) -> CreateStackInput:
    out: CreateStackInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_template_url = el.find("TemplateURL")
    if child_template_url is not None:
        out["template_url"] = str(child_template_url.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudformation.types.parameters

        out["parameters"] = capo_cloudformation.types.parameters.deserialize_query(
            child_parameters
        )
    child_disable_rollback = el.find("DisableRollback")
    if child_disable_rollback is not None:
        out["disable_rollback"] = (child_disable_rollback.text or "").lower() == "true"
    child_rollback_configuration = el.find("RollbackConfiguration")
    if child_rollback_configuration is not None:
        import capo_cloudformation.types.rollback_configuration

        out["rollback_configuration"] = (
            capo_cloudformation.types.rollback_configuration.deserialize_query(
                child_rollback_configuration
            )
        )
    child_timeout_in_minutes = el.find("TimeoutInMinutes")
    if child_timeout_in_minutes is not None:
        out["timeout_in_minutes"] = int(child_timeout_in_minutes.text or "")
    child_notification_ar_ns = el.find("NotificationARNs")
    if child_notification_ar_ns is not None:
        import capo_cloudformation.types.notification_ar_ns

        out["notification_ar_ns"] = (
            capo_cloudformation.types.notification_ar_ns.deserialize_query(
                child_notification_ar_ns
            )
        )
    child_capabilities = el.find("Capabilities")
    if child_capabilities is not None:
        import capo_cloudformation.types.capabilities

        out["capabilities"] = capo_cloudformation.types.capabilities.deserialize_query(
            child_capabilities
        )
    child_resource_types = el.find("ResourceTypes")
    if child_resource_types is not None:
        import capo_cloudformation.types.resource_types

        out["resource_types"] = (
            capo_cloudformation.types.resource_types.deserialize_query(
                child_resource_types
            )
        )
    child_role_arn = el.find("RoleARN")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_on_failure = el.find("OnFailure")
    if child_on_failure is not None:
        import capo_cloudformation.types.on_failure

        out["on_failure"] = capo_cloudformation.types.on_failure.deserialize_query(
            child_on_failure
        )
    child_stack_policy_body = el.find("StackPolicyBody")
    if child_stack_policy_body is not None:
        out["stack_policy_body"] = str(child_stack_policy_body.text or "")
    child_stack_policy_url = el.find("StackPolicyURL")
    if child_stack_policy_url is not None:
        out["stack_policy_url"] = str(child_stack_policy_url.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudformation.types.tags

        out["tags"] = capo_cloudformation.types.tags.deserialize_query(child_tags)
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_enable_termination_protection = el.find("EnableTerminationProtection")
    if child_enable_termination_protection is not None:
        out["enable_termination_protection"] = (
            child_enable_termination_protection.text or ""
        ).lower() == "true"
    child_retain_except_on_create = el.find("RetainExceptOnCreate")
    if child_retain_except_on_create is not None:
        out["retain_except_on_create"] = (
            child_retain_except_on_create.text or ""
        ).lower() == "true"
    child_deployment_config = el.find("DeploymentConfig")
    if child_deployment_config is not None:
        import capo_cloudformation.types.deployment_config

        out["deployment_config"] = (
            capo_cloudformation.types.deployment_config.deserialize_query(
                child_deployment_config
            )
        )
    child_disable_validation = el.find("DisableValidation")
    if child_disable_validation is not None:
        out["disable_validation"] = (
            child_disable_validation.text or ""
        ).lower() == "true"
    return out
