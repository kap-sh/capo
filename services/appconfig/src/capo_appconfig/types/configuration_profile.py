"""Generated from Smithy shape ``com.amazonaws.appconfig#ConfigurationProfile``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.configuration_profile_type
    import capo_appconfig.types.description
    import capo_appconfig.types.id
    import capo_appconfig.types.kms_key_identifier
    import capo_appconfig.types.long_name
    import capo_appconfig.types.role_arn
    import capo_appconfig.types.uri
    import capo_appconfig.types.validator_list


class ConfigurationProfile(TypedDict, closed=True):
    application_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The configuration profile ID.</p>"""
    name: NotRequired["capo_appconfig.types.long_name.LongName"]
    """<p>The name of the configuration profile.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The configuration profile description.</p>"""
    location_uri: NotRequired["capo_appconfig.types.uri.Uri"]
    """<p>The URI location of the configuration.</p>"""
    retrieval_role_arn: NotRequired["capo_appconfig.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p>"""
    validators: NotRequired["capo_appconfig.types.validator_list.ValidatorList"]
    """<p>A list of methods for validating the configuration.</p>"""
    type: NotRequired[
        "capo_appconfig.types.configuration_profile_type.ConfigurationProfileType"
    ]
    """<p>The type of configurations contained in the profile. AppConfig supports <code>feature flags</code> and <code>freeform</code> configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for <code>Type</code>:</p> <p> <code>AWS.AppConfig.FeatureFlags</code> </p> <p> <code>AWS.Freeform</code> </p>"""
    kms_key_arn: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>"""
    kms_key_identifier: NotRequired[
        "capo_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationProfile) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "retrieval_role_arn" in value:
        out["RetrievalRoleArn"] = value["retrieval_role_arn"]
    if "validators" in value:
        import capo_appconfig.types.validator_list

        out["Validators"] = capo_appconfig.types.validator_list.serialize_json(
            value["validators"]
        )
    if "type" in value:
        out["Type"] = value["type"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> ConfigurationProfile:
    out: ConfigurationProfile = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("RetrievalRoleArn") is not None:
        out["retrieval_role_arn"] = data["RetrievalRoleArn"]
    if data.get("Validators") is not None:
        import capo_appconfig.types.validator_list

        out["validators"] = capo_appconfig.types.validator_list.deserialize_json(
            data["Validators"]
        )
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out


def redact_sensitive(value: ConfigurationProfile) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "validators" in value:
        import capo_appconfig.types.validator_list

        out["validators"] = capo_appconfig.types.validator_list.redact_sensitive(
            value["validators"]
        )
    return out
