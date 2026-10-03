"""Generated from Smithy shape ``com.amazonaws.organizations#InviteOrganizationToTransferResponsibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.handshake_notes
    import capo_organizations.types.handshake_party
    import capo_organizations.types.responsibility_transfer_name
    import capo_organizations.types.responsibility_transfer_type
    import capo_organizations.types.tags
    import capo_organizations.types.timestamp


class InviteOrganizationToTransferResponsibilityRequest(TypedDict, closed=True):
    type: "capo_organizations.types.responsibility_transfer_type.ResponsibilityTransferType"
    """<p>The type of responsibility you want to designate to your organization. Currently, only <code>BILLING</code> is supported.</p>"""
    target: "capo_organizations.types.handshake_party.HandshakeParty"
    """<p>A <code>HandshakeParty</code> object. Contains details for the account you want to invite. Currently, only <code>ACCOUNT</code> and <code>EMAIL</code> are supported.</p>"""
    notes: NotRequired["capo_organizations.types.handshake_notes.HandshakeNotes"]
    """<p>Additional information that you want to include in the invitation.</p>"""
    start_timestamp: "capo_organizations.types.timestamp.Timestamp"
    """<p>Timestamp when the recipient will begin managing the specified responsibilities.</p>"""
    source_name: "capo_organizations.types.responsibility_transfer_name.ResponsibilityTransferName"
    """<p>Name you want to assign to the transfer.</p>"""
    tags: NotRequired["capo_organizations.types.tags.Tags"]
    """<p>A list of tags that you want to attach to the transfer. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to <code>null</code>. For more information about tagging, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html">Tagging Organizations resources</a> in the Organizations User Guide.</p> <important> <p>Any tags in the request are checked for compliance with any applicable tag policies when the request is made. The request is rejected if the tags in the request don't match the requirements of the policy at that time. Tag policy compliance is <i> <b>not</b> </i> checked again when the invitation is accepted and the tags are actually attached to the transfer. That means that if the tag policy changes between the invitation and the acceptance, then that tags could potentially be non-compliant.</p> </important> <note> <p>If any one of the tags is not valid or if you exceed the allowed number of tags for a transfer, then the entire request fails and invitations are not sent.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InviteOrganizationToTransferResponsibilityRequest,
) -> dict:
    out: dict = {}
    import capo_organizations.types.responsibility_transfer_type

    out["Type"] = (
        capo_organizations.types.responsibility_transfer_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    import capo_organizations.types.handshake_party

    out["Target"] = capo_organizations.types.handshake_party.serialize_aws_json_1_1(
        value["target"]
    )
    if "notes" in value:
        out["Notes"] = value["notes"]
    import capo_organizations.types.timestamp

    out["StartTimestamp"] = capo_organizations.types.timestamp.serialize_aws_json_1_1(
        value["start_timestamp"]
    )
    out["SourceName"] = value["source_name"]
    if "tags" in value:
        import capo_organizations.types.tags

        out["Tags"] = capo_organizations.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InviteOrganizationToTransferResponsibilityRequest:
    out: InviteOrganizationToTransferResponsibilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_organizations.types.responsibility_transfer_type

        out["type"] = (
            capo_organizations.types.responsibility_transfer_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError(
            "InviteOrganizationToTransferResponsibilityRequest.type required"
        )
    if data.get("Target") is not None:
        import capo_organizations.types.handshake_party

        out["target"] = (
            capo_organizations.types.handshake_party.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    else:
        raise DeserializationError(
            "InviteOrganizationToTransferResponsibilityRequest.target required"
        )
    if data.get("Notes") is not None:
        out["notes"] = data["Notes"]
    if data.get("StartTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["start_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "InviteOrganizationToTransferResponsibilityRequest.start_timestamp required"
        )
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    else:
        raise DeserializationError(
            "InviteOrganizationToTransferResponsibilityRequest.source_name required"
        )
    if data.get("Tags") is not None:
        import capo_organizations.types.tags

        out["tags"] = capo_organizations.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
