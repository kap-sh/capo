"""Generated from Smithy shape ``com.amazonaws.transfer#ListedProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.as2_id
    import capo_transfer.types.profile_id
    import capo_transfer.types.profile_type


class ListedProfile(TypedDict, closed=True):
    arn: NotRequired["capo_transfer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the specified profile.</p>"""
    profile_id: NotRequired["capo_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the local or partner AS2 profile.</p>"""
    as2_id: NotRequired["capo_transfer.types.as2_id.As2Id"]
    """<p>The <code>As2Id</code> is the <i>AS2-name</i>, as defined in the <a href="https://datatracker.ietf.org/doc/html/rfc4130">RFC 4130</a>. For inbound transfers, this is the <code>AS2-From</code> header for the AS2 messages sent from the partner. For outbound connectors, this is the <code>AS2-To</code> header for the AS2 messages sent to the partner using the <code>StartFileTransfer</code> API operation. This ID cannot include spaces.</p>"""
    profile_type: NotRequired["capo_transfer.types.profile_type.ProfileType"]
    """<p>Indicates whether to list only <code>LOCAL</code> type profiles or only <code>PARTNER</code> type profiles. If not supplied in the request, the command lists all types of profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "as2_id" in value:
        out["As2Id"] = value["as2_id"]
    if "profile_type" in value:
        import capo_transfer.types.profile_type

        out["ProfileType"] = capo_transfer.types.profile_type.serialize_aws_json_1_1(
            value["profile_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedProfile:
    out: ListedProfile = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("As2Id") is not None:
        out["as2_id"] = data["As2Id"]
    if data.get("ProfileType") is not None:
        import capo_transfer.types.profile_type

        out["profile_type"] = capo_transfer.types.profile_type.deserialize_aws_json_1_1(
            data["ProfileType"]
        )
    return out
