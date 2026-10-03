"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.as2_id
    import capo_transfer.types.certificate_ids
    import capo_transfer.types.profile_id
    import capo_transfer.types.profile_type
    import capo_transfer.types.tags


class DescribedProfile(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) for the profile.</p>"""
    profile_id: NotRequired["capo_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the local or partner AS2 profile.</p>"""
    profile_type: NotRequired["capo_transfer.types.profile_type.ProfileType"]
    """<p>Indicates whether to list only <code>LOCAL</code> type profiles or only <code>PARTNER</code> type profiles. If not supplied in the request, the command lists all types of profiles.</p>"""
    as2_id: NotRequired["capo_transfer.types.as2_id.As2Id"]
    """<p>The <code>As2Id</code> is the <i>AS2-name</i>, as defined in the <a href="https://datatracker.ietf.org/doc/html/rfc4130">RFC 4130</a>. For inbound transfers, this is the <code>AS2-From</code> header for the AS2 messages sent from the partner. For outbound connectors, this is the <code>AS2-To</code> header for the AS2 messages sent to the partner using the <code>StartFileTransfer</code> API operation. This ID cannot include spaces.</p>"""
    certificate_ids: NotRequired["capo_transfer.types.certificate_ids.CertificateIds"]
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedProfile) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "profile_type" in value:
        import capo_transfer.types.profile_type

        out["ProfileType"] = capo_transfer.types.profile_type.serialize_aws_json_1_1(
            value["profile_type"]
        )
    if "as2_id" in value:
        out["As2Id"] = value["as2_id"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribedProfile:
    out: DescribedProfile = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedProfile.arn required")
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("ProfileType") is not None:
        import capo_transfer.types.profile_type

        out["profile_type"] = capo_transfer.types.profile_type.deserialize_aws_json_1_1(
            data["ProfileType"]
        )
    if data.get("As2Id") is not None:
        out["as2_id"] = data["As2Id"]
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
