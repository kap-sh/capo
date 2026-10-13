"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateConfigurationProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.kms_key_identifier_or_empty
    import capo_appconfig.types.long_name
    import capo_appconfig.types.name
    import capo_appconfig.types.role_arn
    import capo_appconfig.types.validator_list


class UpdateConfigurationProfileRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.name.Name"
    """<p>The application ID.</p>"""
    configuration_profile_id: "capo_appconfig.types.long_name.LongName"
    """<p>The ID of the configuration profile.</p>"""
    name: NotRequired["capo_appconfig.types.long_name.LongName"]
    """<p>The name of the configuration profile.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the configuration profile.</p>"""
    retrieval_role_arn: NotRequired["capo_appconfig.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p> <important> <p>A retrieval role ARN is not required for configurations stored in CodePipeline or the AppConfig hosted configuration store. It is required for all other sources that store your configuration. </p> </important>"""
    validators: NotRequired["capo_appconfig.types.validator_list.ValidatorList"]
    """<p>A list of methods for validating the configuration.</p>"""
    kms_key_identifier: NotRequired[
        "capo_appconfig.types.kms_key_identifier_or_empty.KmsKeyIdentifierOrEmpty"
    ]
    """<p>The identifier for a Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. The identifier can be an KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "retrieval_role_arn" in value:
        out["RetrievalRoleArn"] = value["retrieval_role_arn"]
    if "validators" in value:
        import capo_appconfig.types.validator_list

        out["Validators"] = capo_appconfig.types.validator_list.serialize_json(
            value["validators"]
        )
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationProfileRequest:
    out: UpdateConfigurationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RetrievalRoleArn") is not None:
        out["retrieval_role_arn"] = data["RetrievalRoleArn"]
    if data.get("Validators") is not None:
        import capo_appconfig.types.validator_list

        out["validators"] = capo_appconfig.types.validator_list.deserialize_json(
            data["Validators"]
        )
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out


def redact_sensitive(value: UpdateConfigurationProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "validators" in value:
        import capo_appconfig.types.validator_list

        out["validators"] = capo_appconfig.types.validator_list.redact_sensitive(
            value["validators"]
        )
    return out
