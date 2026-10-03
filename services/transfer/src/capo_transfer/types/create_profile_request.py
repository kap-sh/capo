"""Generated from Smithy shape ``com.amazonaws.transfer#CreateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.as2_id
    import capo_transfer.types.certificate_ids
    import capo_transfer.types.profile_type
    import capo_transfer.types.tags


class CreateProfileRequest(TypedDict, closed=True):
    as2_id: "capo_transfer.types.as2_id.As2Id"
    """<p>The <code>As2Id</code> is the <i>AS2-name</i>, as defined in the <a href="https://datatracker.ietf.org/doc/html/rfc4130">RFC 4130</a>. For inbound transfers, this is the <code>AS2-From</code> header for the AS2 messages sent from the partner. For outbound connectors, this is the <code>AS2-To</code> header for the AS2 messages sent to the partner using the <code>StartFileTransfer</code> API operation. This ID cannot include spaces.</p>"""
    profile_type: "capo_transfer.types.profile_type.ProfileType"
    """<p>Determines the type of profile to create:</p> <ul> <li> <p>Specify <code>LOCAL</code> to create a local profile. A local profile represents the AS2-enabled Transfer Family server organization or party.</p> </li> <li> <p>Specify <code>PARTNER</code> to create a partner profile. A partner profile represents a remote organization, external to Transfer Family.</p> </li> </ul>"""
    certificate_ids: NotRequired["capo_transfer.types.certificate_ids.CertificateIds"]
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for AS2 profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProfileRequest) -> dict:
    out: dict = {}
    out["As2Id"] = value["as2_id"]
    import capo_transfer.types.profile_type

    out["ProfileType"] = capo_transfer.types.profile_type.serialize_aws_json_1_1(
        value["profile_type"]
    )
    if "certificate_ids" in value:
        import capo_transfer.types.certificate_ids

        out["CertificateIds"] = (
            capo_transfer.types.certificate_ids.serialize_aws_json_1_1(
                value["certificate_ids"]
            )
        )
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProfileRequest:
    out: CreateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("As2Id") is not None:
        out["as2_id"] = data["As2Id"]
    else:
        raise DeserializationError("CreateProfileRequest.as2_id required")
    if data.get("ProfileType") is not None:
        import capo_transfer.types.profile_type

        out["profile_type"] = capo_transfer.types.profile_type.deserialize_aws_json_1_1(
            data["ProfileType"]
        )
    else:
        raise DeserializationError("CreateProfileRequest.profile_type required")
    if data.get("CertificateIds") is not None:
        import capo_transfer.types.certificate_ids

        out["certificate_ids"] = (
            capo_transfer.types.certificate_ids.deserialize_aws_json_1_1(
                data["CertificateIds"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
