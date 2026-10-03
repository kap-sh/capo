"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#CreateCloudFormationChangeSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__list_of_parameter_value
    import capo_serverlessapplicationrepository.types.__list_of_tag
    import capo_serverlessapplicationrepository.types.__string
    import capo_serverlessapplicationrepository.types.rollback_configuration


class CreateCloudFormationChangeSetRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    capabilities: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.</p><p>The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.</p><p>The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html">AWS::IAM::Group</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM::Policy</a>, and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html">AWS::IAM::Role</a>. If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.</p><p>The following resources require you to specify CAPABILITY_RESOURCE_POLICY: <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html">AWS::Lambda::Permission</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM:Policy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html">AWS::ApplicationAutoScaling::ScalingPolicy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html">AWS::S3::BucketPolicy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html">AWS::SQS::QueuePolicy</a>, and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html">AWS::SNS:TopicPolicy</a>.</p><p>Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.</p><p>If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don't specify this parameter for an application that requires capabilities, the call will fail.</p>"""
    change_set_name: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    client_token: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    description: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    notification_arns: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    parameter_overrides: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_parameter_value.__listOfParameterValue"
    ]
    """<p>A list of parameter values for the parameters of the application.</p>"""
    resource_types: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    rollback_configuration: NotRequired[
        "capo_serverlessapplicationrepository.types.rollback_configuration.RollbackConfiguration"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>"""
    stack_name: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    tags: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_tag.__listOfTag"
    ]
    """<p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>"""
    template_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    r"""<p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudFormationChangeSetRequest) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["capabilities"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["capabilities"]
            )
        )
    if "change_set_name" in value:
        out["changeSetName"] = value["change_set_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "notification_arns" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["notificationArns"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["notification_arns"]
            )
        )
    if "parameter_overrides" in value:
        import capo_serverlessapplicationrepository.types.__list_of_parameter_value

        out["parameterOverrides"] = (
            capo_serverlessapplicationrepository.types.__list_of_parameter_value.serialize_json(
                value["parameter_overrides"]
            )
        )
    if "resource_types" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["resourceTypes"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["resource_types"]
            )
        )
    if "rollback_configuration" in value:
        import capo_serverlessapplicationrepository.types.rollback_configuration

        out["rollbackConfiguration"] = (
            capo_serverlessapplicationrepository.types.rollback_configuration.serialize_json(
                value["rollback_configuration"]
            )
        )
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "stack_name" in value:
        out["stackName"] = value["stack_name"]
    if "tags" in value:
        import capo_serverlessapplicationrepository.types.__list_of_tag

        out["tags"] = (
            capo_serverlessapplicationrepository.types.__list_of_tag.serialize_json(
                value["tags"]
            )
        )
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> CreateCloudFormationChangeSetRequest:
    out: CreateCloudFormationChangeSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("capabilities") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["capabilities"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["capabilities"]
            )
        )
    if data.get("changeSetName") is not None:
        out["change_set_name"] = data["changeSetName"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("notificationArns") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["notification_arns"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["notificationArns"]
            )
        )
    if data.get("parameterOverrides") is not None:
        import capo_serverlessapplicationrepository.types.__list_of_parameter_value

        out["parameter_overrides"] = (
            capo_serverlessapplicationrepository.types.__list_of_parameter_value.deserialize_json(
                data["parameterOverrides"]
            )
        )
    if data.get("resourceTypes") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["resource_types"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["resourceTypes"]
            )
        )
    if data.get("rollbackConfiguration") is not None:
        import capo_serverlessapplicationrepository.types.rollback_configuration

        out["rollback_configuration"] = (
            capo_serverlessapplicationrepository.types.rollback_configuration.deserialize_json(
                data["rollbackConfiguration"]
            )
        )
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    if data.get("stackName") is not None:
        out["stack_name"] = data["stackName"]
    if data.get("tags") is not None:
        import capo_serverlessapplicationrepository.types.__list_of_tag

        out["tags"] = (
            capo_serverlessapplicationrepository.types.__list_of_tag.deserialize_json(
                data["tags"]
            )
        )
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    return out
