"""Generated from Smithy shape ``com.amazonaws.organizations#InviteAccountToOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.handshake_notes
    import capo_organizations.types.handshake_party
    import capo_organizations.types.tags


class InviteAccountToOrganizationRequest(TypedDict, closed=True):
    target: "capo_organizations.types.handshake_party.HandshakeParty"
    """<p>The identifier (ID) of the Amazon Web Services account that you want to invite to join your organization. This is a JSON object that contains the following elements:</p> <p> <code>{ "Type": "ACCOUNT", "Id": "<<i> <b>account id number</b> </i>>" }</code> </p> <p>If you use the CLI, you can submit this as a single string, similar to the following example:</p> <p> <code>--target Id=123456789012,Type=ACCOUNT</code> </p> <p>If you specify <code>"Type": "ACCOUNT"</code>, you must provide the Amazon Web Services account ID number as the <code>Id</code>. If you specify <code>"Type": "EMAIL"</code>, you must specify the email address that is associated with the account.</p> <p> <code>--target Id=diego@example.com,Type=EMAIL</code> </p>"""
    notes: NotRequired["capo_organizations.types.handshake_notes.HandshakeNotes"]
    """<p>Additional information that you want to include in the generated email to the recipient account owner.</p>"""
    tags: NotRequired["capo_organizations.types.tags.Tags"]
    """<p>A list of tags that you want to attach to the account when it becomes a member of the organization. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to <code>null</code>. For more information about tagging, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html">Tagging Organizations resources</a> in the Organizations User Guide.</p> <important> <p>Any tags in the request are checked for compliance with any applicable tag policies when the request is made. The request is rejected if the tags in the request don't match the requirements of the policy at that time. Tag policy compliance is <i> <b>not</b> </i> checked again when the invitation is accepted and the tags are actually attached to the account. That means that if the tag policy changes between the invitation and the acceptance, then that tags could potentially be non-compliant.</p> </important> <note> <p>If any one of the tags is not valid or if you exceed the allowed number of tags for an account, then the entire request fails and invitations are not sent.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InviteAccountToOrganizationRequest) -> dict:
    out: dict = {}
    import capo_organizations.types.handshake_party

    out["Target"] = capo_organizations.types.handshake_party.serialize_aws_json_1_1(
        value["target"]
    )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "tags" in value:
        import capo_organizations.types.tags

        out["Tags"] = capo_organizations.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InviteAccountToOrganizationRequest:
    out: InviteAccountToOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        import capo_organizations.types.handshake_party

        out["target"] = (
            capo_organizations.types.handshake_party.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    else:
        raise DeserializationError("InviteAccountToOrganizationRequest.target required")
    if data.get("Notes") is not None:
        out["notes"] = data["Notes"]
    if data.get("Tags") is not None:
        import capo_organizations.types.tags

        out["tags"] = capo_organizations.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
