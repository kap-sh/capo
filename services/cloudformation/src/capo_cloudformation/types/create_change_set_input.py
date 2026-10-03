"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateChangeSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.change_set_name
    import capo_cloudformation.types.change_set_type
    import capo_cloudformation.types.client_token
    import capo_cloudformation.types.deployment_config
    import capo_cloudformation.types.deployment_mode
    import capo_cloudformation.types.description
    import capo_cloudformation.types.disable_validation
    import capo_cloudformation.types.import_existing_resources
    import capo_cloudformation.types.include_nested_stacks
    import capo_cloudformation.types.notification_ar_ns
    import capo_cloudformation.types.on_stack_failure
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.resource_types
    import capo_cloudformation.types.resources_to_import
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.rollback_configuration
    import capo_cloudformation.types.stack_name_or_id
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.template_body
    import capo_cloudformation.types.template_url
    import capo_cloudformation.types.use_previous_template


class CreateChangeSetInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.</p>"""
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>"""
    template_url: NotRequired["capo_cloudformation.types.template_url.TemplateURL"]
    """<p>The URL of the file that contains the revised template. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>"""
    use_previous_template: NotRequired[
        "capo_cloudformation.types.use_previous_template.UsePreviousTemplate"
    ]
    """<p>Whether to reuse the template that's associated with the stack to create the change set.</p> <p>When using templates with the <code>AWS::LanguageExtensions</code> transform, provide the template instead of using <code>UsePreviousTemplate</code> to ensure new parameter values and Systems Manager parameter updates are applied correctly. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-languageextensions.html">AWS::LanguageExtensions transform</a>.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>A list of <code>Parameter</code> structures that specify input parameters for the change set. For more information, see the <a>Parameter</a> data type.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html"> AWS::IAM::ManagedPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <note> <p>This capacity doesn't apply to creating change sets, and specifying it when creating change sets has no effect.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create or update the stack directly from the template using the <a>CreateStack</a> or <a>UpdateStack</a> action, and specifying this capability.</p> </note> <p>For more information about macros, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> </li> </ul> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>"""
    resource_types: NotRequired[
        "capo_cloudformation.types.resource_types.ResourceTypes"
    ]
    """<p>Specifies which resource types you can work with, such as <code>AWS::EC2::Instance</code> or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html">Control CloudFormation access with Identity and Access Management</a> in the <i>CloudFormation User Guide</i>.</p> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>"""
    role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when executing the change set. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>"""
    rollback_configuration: NotRequired[
        "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
    ]
    """<p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>"""
    notification_ar_ns: NotRequired[
        "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
    ]
    """<p>The Amazon Resource Names (ARNs) of Amazon SNS topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.</p>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.</p>"""
    change_set_name: NotRequired[
        "capo_cloudformation.types.change_set_name.ChangeSetName"
    ]
    """<p>The name of the change set. The name must be unique among all change sets that are associated with the specified stack.</p> <p>A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can't exceed 128 characters.</p>"""
    client_token: NotRequired["capo_cloudformation.types.client_token.ClientToken"]
    """<p>A unique identifier for this <code>CreateChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another change set with the same name. You might retry <code>CreateChangeSet</code> requests to ensure that CloudFormation successfully received them.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A description to help you identify this change set.</p>"""
    change_set_type: NotRequired[
        "capo_cloudformation.types.change_set_type.ChangeSetType"
    ]
    """<p>The type of change set operation. To create a change set for a new stack, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code>. To create a change set for an import operation, specify <code>IMPORT</code>.</p> <p>If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the <code>REVIEW_IN_PROGRESS</code> state until you execute the change set.</p> <p>By default, CloudFormation specifies <code>UPDATE</code>. You can't use the <code>UPDATE</code> type to create a change set for a new stack or the <code>CREATE</code> type to create a change set for an existing stack.</p>"""
    resources_to_import: NotRequired[
        "capo_cloudformation.types.resources_to_import.ResourcesToImport"
    ]
    """<p>The resources to import into your stack.</p>"""
    include_nested_stacks: NotRequired[
        "capo_cloudformation.types.include_nested_stacks.IncludeNestedStacks"
    ]
    """<p>Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to <code>False</code>. To include nested sets in a change set, specify <code>True</code>.</p>"""
    on_stack_failure: NotRequired[
        "capo_cloudformation.types.on_stack_failure.OnStackFailure"
    ]
    """<p>Determines what action will be taken if stack creation fails. If this parameter is specified, the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation must not be specified. This must be one of these values:</p> <ul> <li> <p> <code>DELETE</code> - Deletes the change set if the stack creation fails. This is only valid when the <code>ChangeSetType</code> parameter is set to <code>CREATE</code>. If the deletion of the stack fails, the status of the stack is <code>DELETE_FAILED</code>.</p> </li> <li> <p> <code>DO_NOTHING</code> - if the stack creation fails, do nothing. This is equivalent to specifying <code>true</code> for the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation.</p> </li> <li> <p> <code>ROLLBACK</code> - if the stack creation fails, roll back the stack. This is equivalent to specifying <code>false</code> for the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation.</p> </li> </ul> <p>For nested stacks, when the <code>OnStackFailure</code> parameter is set to <code>DELETE</code> for the change set for the parent stack, any failure in a child stack will cause the parent stack creation to fail and all stacks to be deleted.</p>"""
    import_existing_resources: NotRequired[
        "capo_cloudformation.types.import_existing_resources.ImportExistingResources"
    ]
    """<p>Indicates if the change set auto-imports resources that already exist. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources-automatically.html">Import Amazon Web Services resources into a CloudFormation stack automatically</a> in the <i>CloudFormation User Guide</i>.</p> <note> <p>This parameter can only import resources that have custom names in templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html">name type</a> in the <i>CloudFormation User Guide</i>. To import resources that do not accept custom names, such as EC2 instances, use the <code>ResourcesToImport</code> parameter instead.</p> </note>"""
    deployment_mode: NotRequired[
        "capo_cloudformation.types.deployment_mode.DeploymentMode"
    ]
    """<p>Determines how CloudFormation handles configuration drift during deployment.</p> <ul> <li> <p> <code>REVERT_DRIFT</code> – Creates a drift-aware change set that brings actual resource states in line with template definitions. Provides a three-way comparison between actual state, previous deployment state, and desired state.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/drift-aware-change-sets.html">Using drift-aware change sets</a> in the <i>CloudFormation User Guide</i>.</p>"""
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
    value: CreateChangeSetInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
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
    if "resource_types" in value:
        import capo_cloudformation.types.resource_types

        capo_cloudformation.types.resource_types.serialize_query(
            value["resource_types"], pairs, f"{key_prefix}ResourceTypes"
        )
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleARN", str(value["role_arn"])))
    if "rollback_configuration" in value:
        import capo_cloudformation.types.rollback_configuration

        capo_cloudformation.types.rollback_configuration.serialize_query(
            value["rollback_configuration"], pairs, f"{key_prefix}RollbackConfiguration"
        )
    if "notification_ar_ns" in value:
        import capo_cloudformation.types.notification_ar_ns

        capo_cloudformation.types.notification_ar_ns.serialize_query(
            value["notification_ar_ns"], pairs, f"{key_prefix}NotificationARNs"
        )
    if "tags" in value:
        import capo_cloudformation.types.tags

        capo_cloudformation.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "change_set_name" in value:
        pairs.append((f"{key_prefix}ChangeSetName", str(value["change_set_name"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "change_set_type" in value:
        import capo_cloudformation.types.change_set_type

        capo_cloudformation.types.change_set_type.serialize_query(
            value["change_set_type"], pairs, f"{key_prefix}ChangeSetType"
        )
    if "resources_to_import" in value:
        import capo_cloudformation.types.resources_to_import

        capo_cloudformation.types.resources_to_import.serialize_query(
            value["resources_to_import"], pairs, f"{key_prefix}ResourcesToImport"
        )
    if "include_nested_stacks" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeNestedStacks",
                "true" if value["include_nested_stacks"] else "false",
            )
        )
    if "on_stack_failure" in value:
        import capo_cloudformation.types.on_stack_failure

        capo_cloudformation.types.on_stack_failure.serialize_query(
            value["on_stack_failure"], pairs, f"{key_prefix}OnStackFailure"
        )
    if "import_existing_resources" in value:
        pairs.append(
            (
                f"{key_prefix}ImportExistingResources",
                "true" if value["import_existing_resources"] else "false",
            )
        )
    if "deployment_mode" in value:
        import capo_cloudformation.types.deployment_mode

        capo_cloudformation.types.deployment_mode.serialize_query(
            value["deployment_mode"], pairs, f"{key_prefix}DeploymentMode"
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


def deserialize_query(el: Element) -> CreateChangeSetInput:
    out: CreateChangeSetInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
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
    child_rollback_configuration = el.find("RollbackConfiguration")
    if child_rollback_configuration is not None:
        import capo_cloudformation.types.rollback_configuration

        out["rollback_configuration"] = (
            capo_cloudformation.types.rollback_configuration.deserialize_query(
                child_rollback_configuration
            )
        )
    child_notification_ar_ns = el.find("NotificationARNs")
    if child_notification_ar_ns is not None:
        import capo_cloudformation.types.notification_ar_ns

        out["notification_ar_ns"] = (
            capo_cloudformation.types.notification_ar_ns.deserialize_query(
                child_notification_ar_ns
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudformation.types.tags

        out["tags"] = capo_cloudformation.types.tags.deserialize_query(child_tags)
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_change_set_type = el.find("ChangeSetType")
    if child_change_set_type is not None:
        import capo_cloudformation.types.change_set_type

        out["change_set_type"] = (
            capo_cloudformation.types.change_set_type.deserialize_query(
                child_change_set_type
            )
        )
    child_resources_to_import = el.find("ResourcesToImport")
    if child_resources_to_import is not None:
        import capo_cloudformation.types.resources_to_import

        out["resources_to_import"] = (
            capo_cloudformation.types.resources_to_import.deserialize_query(
                child_resources_to_import
            )
        )
    child_include_nested_stacks = el.find("IncludeNestedStacks")
    if child_include_nested_stacks is not None:
        out["include_nested_stacks"] = (
            child_include_nested_stacks.text or ""
        ).lower() == "true"
    child_on_stack_failure = el.find("OnStackFailure")
    if child_on_stack_failure is not None:
        import capo_cloudformation.types.on_stack_failure

        out["on_stack_failure"] = (
            capo_cloudformation.types.on_stack_failure.deserialize_query(
                child_on_stack_failure
            )
        )
    child_import_existing_resources = el.find("ImportExistingResources")
    if child_import_existing_resources is not None:
        out["import_existing_resources"] = (
            child_import_existing_resources.text or ""
        ).lower() == "true"
    child_deployment_mode = el.find("DeploymentMode")
    if child_deployment_mode is not None:
        import capo_cloudformation.types.deployment_mode

        out["deployment_mode"] = (
            capo_cloudformation.types.deployment_mode.deserialize_query(
                child_deployment_mode
            )
        )
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
