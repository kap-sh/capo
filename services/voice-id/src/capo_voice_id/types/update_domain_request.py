"""Generated from Smithy shape ``com.amazonaws.voiceid#UpdateDomainRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.description
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.domain_name
    import capo_voice_id.types.server_side_encryption_configuration


class UpdateDomainRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain to be updated.</p>"""
    name: "capo_voice_id.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    description: NotRequired["capo_voice_id.types.description.Description"]
    """<p>A brief description about this domain.</p>"""
    server_side_encryption_configuration: "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    """<p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Changing the domain's associated KMS key immediately triggers an asynchronous process to remove dependency on the old KMS key, such that the domain's data can only be accessed using the new KMS key. The domain's <code>ServerSideEncryptionUpdateDetails</code> contains the details for this process.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDomainRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_voice_id.types.server_side_encryption_configuration

    out["ServerSideEncryptionConfiguration"] = (
        capo_voice_id.types.server_side_encryption_configuration.serialize_aws_json_1_0(
            value["server_side_encryption_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDomainRequest:
    out: UpdateDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("UpdateDomainRequest.domain_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDomainRequest.name required")
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
            "UpdateDomainRequest.server_side_encryption_configuration required"
        )
    return out


def redact_sensitive(value: UpdateDomainRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
