"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.base_resource_id
    import capo_config_service.types.resource_configuration
    import capo_config_service.types.resource_configuration_schema_type
    import capo_config_service.types.string_with_char_limit256


class ResourceDetails(TypedDict, closed=True):
    resource_id: "capo_config_service.types.base_resource_id.BaseResourceId"
    """<p>A unique resource ID for an evaluation.</p>"""
    resource_type: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The type of resource being evaluated.</p>"""
    resource_configuration: (
        "capo_config_service.types.resource_configuration.ResourceConfiguration"
    )
    """<p>The resource definition to be evaluated as per the resource configuration schema type.</p>"""
    resource_configuration_schema_type: NotRequired[
        "capo_config_service.types.resource_configuration_schema_type.ResourceConfigurationSchemaType"
    ]
    """<p>The schema type of the resource configuration.</p> <note> <p>You can find the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">Resource type schema</a>, or <code>CFN_RESOURCE_SCHEMA</code>, in "<i>Amazon Web Services public extensions</i>" within the CloudFormation registry or with the following CLI commmand: <code>aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view">Managing extensions through the CloudFormation registry</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the CloudFormation User Guide.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetails) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    out["ResourceConfiguration"] = value["resource_configuration"]
    if "resource_configuration_schema_type" in value:
        import capo_config_service.types.resource_configuration_schema_type

        out["ResourceConfigurationSchemaType"] = (
            capo_config_service.types.resource_configuration_schema_type.serialize_aws_json_1_1(
                value["resource_configuration_schema_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ResourceDetails.resource_id required")
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceDetails.resource_type required")
    if data.get("ResourceConfiguration") is not None:
        out["resource_configuration"] = data["ResourceConfiguration"]
    else:
        raise DeserializationError("ResourceDetails.resource_configuration required")
    if data.get("ResourceConfigurationSchemaType") is not None:
        import capo_config_service.types.resource_configuration_schema_type

        out["resource_configuration_schema_type"] = (
            capo_config_service.types.resource_configuration_schema_type.deserialize_aws_json_1_1(
                data["ResourceConfigurationSchemaType"]
            )
        )
    return out
