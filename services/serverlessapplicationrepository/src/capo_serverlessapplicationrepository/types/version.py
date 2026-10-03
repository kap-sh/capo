"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#Version``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__boolean
    import capo_serverlessapplicationrepository.types.__list_of_capability
    import capo_serverlessapplicationrepository.types.__list_of_parameter_definition
    import capo_serverlessapplicationrepository.types.__string


class Version(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    creation_time: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The date and time this resource was created.</p>"""
    parameter_definitions: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_parameter_definition.__listOfParameterDefinition"
    ]
    """<p>An array of parameter types supported by the application.</p>"""
    required_capabilities: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_capability.__listOfCapability"
    ]
    """<p>A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.</p><p>The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.</p><p>The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html">AWS::IAM::Group</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM::Policy</a>, and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html">AWS::IAM::Role</a>. If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.</p><p>The following resources require you to specify CAPABILITY_RESOURCE_POLICY: <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html">AWS::Lambda::Permission</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM:Policy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html">AWS::ApplicationAutoScaling::ScalingPolicy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html">AWS::S3::BucketPolicy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html">AWS::SQS::QueuePolicy</a>, and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html">AWS::SNS::TopicPolicy</a>.</p><p>Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.</p><p>If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don't specify this parameter for an application that requires capabilities, the call will fail.</p>"""
    resources_supported: NotRequired[
        "capo_serverlessapplicationrepository.types.__boolean.__boolean"
    ]
    """<p>Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.</p>"""
    semantic_version: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>"""
    source_code_archive_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>"""
    source_code_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.</p>"""
    template_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the packaged AWS SAM template of your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Version) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "parameter_definitions" in value:
        import capo_serverlessapplicationrepository.types.__list_of_parameter_definition

        out["parameterDefinitions"] = (
            capo_serverlessapplicationrepository.types.__list_of_parameter_definition.serialize_json(
                value["parameter_definitions"]
            )
        )
    if "required_capabilities" in value:
        import capo_serverlessapplicationrepository.types.__list_of_capability

        out["requiredCapabilities"] = (
            capo_serverlessapplicationrepository.types.__list_of_capability.serialize_json(
                value["required_capabilities"]
            )
        )
    if "resources_supported" in value:
        out["resourcesSupported"] = value["resources_supported"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "source_code_archive_url" in value:
        out["sourceCodeArchiveUrl"] = value["source_code_archive_url"]
    if "source_code_url" in value:
        out["sourceCodeUrl"] = value["source_code_url"]
    if "template_url" in value:
        out["templateUrl"] = value["template_url"]
    return out


def deserialize_json(data: dict) -> Version:
    out: Version = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    if data.get("parameterDefinitions") is not None:
        import capo_serverlessapplicationrepository.types.__list_of_parameter_definition

        out["parameter_definitions"] = (
            capo_serverlessapplicationrepository.types.__list_of_parameter_definition.deserialize_json(
                data["parameterDefinitions"]
            )
        )
    if data.get("requiredCapabilities") is not None:
        import capo_serverlessapplicationrepository.types.__list_of_capability

        out["required_capabilities"] = (
            capo_serverlessapplicationrepository.types.__list_of_capability.deserialize_json(
                data["requiredCapabilities"]
            )
        )
    if data.get("resourcesSupported") is not None:
        out["resources_supported"] = data["resourcesSupported"]
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    if data.get("sourceCodeArchiveUrl") is not None:
        out["source_code_archive_url"] = data["sourceCodeArchiveUrl"]
    if data.get("sourceCodeUrl") is not None:
        out["source_code_url"] = data["sourceCodeUrl"]
    if data.get("templateUrl") is not None:
        out["template_url"] = data["templateUrl"]
    return out
