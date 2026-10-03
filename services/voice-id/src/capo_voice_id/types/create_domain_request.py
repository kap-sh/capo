"""Generated from Smithy shape ``com.amazonaws.voiceid#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.client_token_string
    import capo_voice_id.types.description
    import capo_voice_id.types.domain_name
    import capo_voice_id.types.server_side_encryption_configuration
    import capo_voice_id.types.tag_list


class CreateDomainRequest(TypedDict, closed=True):
    name: "capo_voice_id.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    description: NotRequired["capo_voice_id.types.description.Description"]
    """<p>A brief description of this domain.</p>"""
    server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    """<p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to <a href="https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid"> Amazon Connect Voice ID encryption at rest</a> for more details on how the KMS key is used. </p>"""
    client_token: NotRequired[
        "capo_voice_id.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_voice_id.types.tag_list.TagList"]
    """<p>A list of tags you want added to the domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDomainRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_voice_id.types.server_side_encryption_configuration

    out["ServerSideEncryptionConfiguration"] = (
        capo_voice_id.types.server_side_encryption_configuration.serialize_aws_json_1_0(
            value["server_side_encryption_configuration"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_voice_id.types.tag_list

        out["Tags"] = capo_voice_id.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDomainRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ServerSideEncryptionConfiguration") is not None:
        import capo_voice_id.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_voice_id.types.server_side_encryption_configuration.deserialize_aws_json_1_0(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDomainRequest.server_side_encryption_configuration required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_voice_id.types.tag_list

        out["tags"] = capo_voice_id.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
