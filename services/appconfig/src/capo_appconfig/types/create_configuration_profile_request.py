"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateConfigurationProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.configuration_profile_type
    import capo_appconfig.types.description
    import capo_appconfig.types.kms_key_identifier
    import capo_appconfig.types.long_name
    import capo_appconfig.types.name
    import capo_appconfig.types.role_arn
    import capo_appconfig.types.tag_map
    import capo_appconfig.types.uri
    import capo_appconfig.types.validator_list


class CreateConfigurationProfileRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.name.Name"
    """<p>The application ID.</p>"""
    name: "capo_appconfig.types.long_name.LongName"
    """<p>A name for the configuration profile.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the configuration profile.</p>"""
    location_uri: "capo_appconfig.types.uri.Uri"
    """<p>A URI to locate the configuration. You can specify the following:</p> <ul> <li> <p>For the AppConfig hosted configuration store and for feature flags, specify <code>hosted</code>.</p> </li> <li> <p>For an Amazon Web Services Systems Manager Parameter Store parameter, specify either the parameter name in the format <code>ssm-parameter://<parameter name></code> or the ARN.</p> </li> <li> <p>For an Amazon Web Services CodePipeline pipeline, specify the URI in the following format: <code>codepipeline</code>://<pipeline name>.</p> </li> <li> <p>For an Secrets Manager secret, specify the URI in the following format: <code>secretsmanager</code>://<secret name>.</p> </li> <li> <p>For an Amazon S3 object, specify the URI in the following format: <code>s3://<bucket>/<objectKey> </code>. Here is an example: <code>s3://amzn-s3-demo-bucket/my-app/us-east-1/my-config.json</code> </p> </li> <li> <p>For an SSM document, specify either the document name in the format <code>ssm-document://<document name></code> or the Amazon Resource Name (ARN).</p> </li> </ul>"""
    retrieval_role_arn: NotRequired["capo_appconfig.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p> <important> <p>A retrieval role ARN is not required for configurations stored in CodePipeline or the AppConfig hosted configuration store. It is required for all other sources that store your configuration. </p> </important>"""
    validators: NotRequired["capo_appconfig.types.validator_list.ValidatorList"]
    """<p>A list of methods for validating the configuration.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the configuration profile. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""
    type: NotRequired[
        "capo_appconfig.types.configuration_profile_type.ConfigurationProfileType"
    ]
    """<p>The type of configurations contained in the profile. AppConfig supports <code>feature flags</code> and <code>freeform</code> configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for <code>Type</code>:</p> <p> <code>AWS.AppConfig.FeatureFlags</code> </p> <p> <code>AWS.Freeform</code> </p>"""
    kms_key_identifier: NotRequired[
        "capo_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier for an Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. The identifier can be an KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationProfileRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["LocationUri"] = value["location_uri"]
    if "retrieval_role_arn" in value:
        out["RetrievalRoleArn"] = value["retrieval_role_arn"]
    if "validators" in value:
        import capo_appconfig.types.validator_list

        out["Validators"] = capo_appconfig.types.validator_list.serialize_json(
            value["validators"]
        )
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    if "type" in value:
        out["Type"] = value["type"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> CreateConfigurationProfileRequest:
    out: CreateConfigurationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    else:
        out["location_uri"] = ""
    if data.get("RetrievalRoleArn") is not None:
        out["retrieval_role_arn"] = data["RetrievalRoleArn"]
    if data.get("Validators") is not None:
        import capo_appconfig.types.validator_list

        out["validators"] = capo_appconfig.types.validator_list.deserialize_json(
            data["Validators"]
        )
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out


def redact_sensitive(value: CreateConfigurationProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "validators" in value:
        import capo_appconfig.types.validator_list

        out["validators"] = capo_appconfig.types.validator_list.redact_sensitive(
            value["validators"]
        )
    return out
