"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.provider
    import capo_securityagent.types.provider_input
    import capo_securityagent.types.tag_map


class CreateIntegrationInput(TypedDict, closed=True):
    provider: "capo_securityagent.types.provider.Provider"
    """<p>The integration provider.</p>"""
    input: "capo_securityagent.types.provider_input.ProviderInput"
    """<p>The provider-specific input required to create the integration.</p>"""
    integration_display_name: "str"
    """<p>The display name for the integration.</p>"""
    kms_key_id: NotRequired["capo_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>"""
    tags: NotRequired["capo_securityagent.types.tag_map.TagMap"]
    """<p>The tags to associate with the integration.</p>"""
    private_connection_name: NotRequired[
        "capo_securityagent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of an active private connection used to reach a self-hosted provider instance over private networking. Specify this when the instance is not publicly reachable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.provider

    out["provider"] = capo_securityagent.types.provider.serialize_json(
        value["provider"]
    )
    import capo_securityagent.types.provider_input

    out["input"] = capo_securityagent.types.provider_input.serialize_json(
        value["input"]
    )
    out["integrationDisplayName"] = value["integration_display_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.serialize_json(value["tags"])
    if "private_connection_name" in value:
        out["privateConnectionName"] = value["private_connection_name"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationInput:
    out: CreateIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_securityagent.types.provider

        out["provider"] = capo_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    else:
        raise DeserializationError("CreateIntegrationInput.provider required")
    if data.get("input") is not None:
        import capo_securityagent.types.provider_input

        out["input"] = capo_securityagent.types.provider_input.deserialize_json(
            data["input"]
        )
    else:
        raise DeserializationError("CreateIntegrationInput.input required")
    if data.get("integrationDisplayName") is not None:
        out["integration_display_name"] = data["integrationDisplayName"]
    else:
        raise DeserializationError(
            "CreateIntegrationInput.integration_display_name required"
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.deserialize_json(data["tags"])
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    return out
