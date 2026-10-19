"""Generated from Smithy shape ``com.amazonaws.glue#CreateSecurityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.encryption_configuration
    import capo_glue.types.name_string


class CreateSecurityConfigurationRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name for the new security configuration.</p>"""
    encryption_configuration: (
        "capo_glue.types.encryption_configuration.EncryptionConfiguration"
    )
    """<p>The encryption configuration for the new security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSecurityConfigurationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.encryption_configuration

    out["EncryptionConfiguration"] = (
        capo_glue.types.encryption_configuration.serialize_aws_json_1_1(
            value["encryption_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSecurityConfigurationRequest:
    out: CreateSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("EncryptionConfiguration") is not None:
        import capo_glue.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_glue.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSecurityConfigurationRequest.encryption_configuration required"
        )
    return out
