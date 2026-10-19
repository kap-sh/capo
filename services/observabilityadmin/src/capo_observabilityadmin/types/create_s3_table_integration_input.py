"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateS3TableIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.encryption
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.tag_map_input


class CreateS3TableIntegrationInput(TypedDict, closed=True):
    encryption: "capo_observabilityadmin.types.encryption.Encryption"
    """<p>The encryption configuration for the S3 Table integration, including the encryption algorithm and KMS key settings.</p>"""
    role_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.</p>"""
    tags: NotRequired["capo_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateS3TableIntegrationInput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.encryption

    out["Encryption"] = capo_observabilityadmin.types.encryption.serialize_json(
        value["encryption"]
    )
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_observabilityadmin.types.tag_map_input

        out["Tags"] = capo_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateS3TableIntegrationInput:
    out: CreateS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("Encryption") is not None:
        import capo_observabilityadmin.types.encryption

        out["encryption"] = capo_observabilityadmin.types.encryption.deserialize_json(
            data["Encryption"]
        )
    else:
        raise DeserializationError("CreateS3TableIntegrationInput.encryption required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_input

        out["tags"] = capo_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
