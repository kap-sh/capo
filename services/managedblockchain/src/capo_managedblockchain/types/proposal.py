"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Proposal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.network_member_name_string
    import capo_managedblockchain.types.output_tag_map
    import capo_managedblockchain.types.proposal_actions
    import capo_managedblockchain.types.proposal_status
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.timestamp
    import capo_managedblockchain.types.vote_count


class Proposal(TypedDict, closed=True):
    proposal_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the proposal.</p>"""
    network_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the network for which the proposal is made.</p>"""
    description: NotRequired[
        "capo_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>The description of the proposal.</p>"""
    actions: NotRequired[
        "capo_managedblockchain.types.proposal_actions.ProposalActions"
    ]
    """<p>The actions to perform on the network if the proposal is <code>APPROVED</code>.</p>"""
    proposed_by_member_id: NotRequired[
        "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member that created the proposal.</p>"""
    proposed_by_member_name: NotRequired[
        "capo_managedblockchain.types.network_member_name_string.NetworkMemberNameString"
    ]
    """<p>The name of the member that created the proposal.</p>"""
    status: NotRequired["capo_managedblockchain.types.proposal_status.ProposalStatus"]
    """<p>The status of the proposal. Values are as follows:</p> <ul> <li> <p> <code>IN_PROGRESS</code> - The proposal is active and open for member voting.</p> </li> <li> <p> <code>APPROVED</code> - The proposal was approved with sufficient <code>YES</code> votes among members according to the <code>VotingPolicy</code> specified for the <code>Network</code>. The specified proposal actions are carried out.</p> </li> <li> <p> <code>REJECTED</code> - The proposal was rejected with insufficient <code>YES</code> votes among members according to the <code>VotingPolicy</code> specified for the <code>Network</code>. The specified <code>ProposalActions</code> aren't carried out.</p> </li> <li> <p> <code>EXPIRED</code> - Members didn't cast the number of votes required to determine the proposal outcome before the proposal expired. The specified <code>ProposalActions</code> aren't carried out.</p> </li> <li> <p> <code>ACTION_FAILED</code> - One or more of the specified <code>ProposalActions</code> in a proposal that was approved couldn't be completed because of an error. The <code>ACTION_FAILED</code> status occurs even if only one ProposalAction fails and other actions are successful.</p> </li> </ul>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p> The date and time that the proposal was created. </p>"""
    expiration_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p> The date and time that the proposal expires. This is the <code>CreationDate</code> plus the <code>ProposalDurationInHours</code> that is specified in the <code>ProposalThresholdPolicy</code>. After this date and time, if members haven't cast enough votes to determine the outcome according to the voting policy, the proposal is <code>EXPIRED</code> and <code>Actions</code> aren't carried out. </p>"""
    yes_vote_count: NotRequired["capo_managedblockchain.types.vote_count.VoteCount"]
    """<p> The current total of <code>YES</code> votes cast on the proposal by members. </p>"""
    no_vote_count: NotRequired["capo_managedblockchain.types.vote_count.VoteCount"]
    """<p> The current total of <code>NO</code> votes cast on the proposal by members. </p>"""
    outstanding_vote_count: NotRequired[
        "capo_managedblockchain.types.vote_count.VoteCount"
    ]
    """<p> The number of votes remaining to be cast on the proposal by members. In other words, the number of members minus the sum of <code>YES</code> votes and <code>NO</code> votes. </p>"""
    tags: NotRequired["capo_managedblockchain.types.output_tag_map.OutputTagMap"]
    """<p>Tags assigned to the proposal. Each tag consists of a key and optional value.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href="https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the proposal. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Proposal) -> dict:
    out: dict = {}
    if "proposal_id" in value:
        out["ProposalId"] = value["proposal_id"]
    if "network_id" in value:
        out["NetworkId"] = value["network_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import capo_managedblockchain.types.proposal_actions

        out["Actions"] = capo_managedblockchain.types.proposal_actions.serialize_json(
            value["actions"]
        )
    if "proposed_by_member_id" in value:
        out["ProposedByMemberId"] = value["proposed_by_member_id"]
    if "proposed_by_member_name" in value:
        out["ProposedByMemberName"] = value["proposed_by_member_name"]
    if "status" in value:
        import capo_managedblockchain.types.proposal_status

        out["Status"] = capo_managedblockchain.types.proposal_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "expiration_date" in value:
        import capo_managedblockchain.types.timestamp

        out["ExpirationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["expiration_date"]
        )
    if "yes_vote_count" in value:
        out["YesVoteCount"] = value["yes_vote_count"]
    if "no_vote_count" in value:
        out["NoVoteCount"] = value["no_vote_count"]
    if "outstanding_vote_count" in value:
        out["OutstandingVoteCount"] = value["outstanding_vote_count"]
    if "tags" in value:
        import capo_managedblockchain.types.output_tag_map

        out["Tags"] = capo_managedblockchain.types.output_tag_map.serialize_json(
            value["tags"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> Proposal:
    out: Proposal = {}  # type: ignore[typeddict-item]
    if data.get("ProposalId") is not None:
        out["proposal_id"] = data["ProposalId"]
    if data.get("NetworkId") is not None:
        out["network_id"] = data["NetworkId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Actions") is not None:
        import capo_managedblockchain.types.proposal_actions

        out["actions"] = capo_managedblockchain.types.proposal_actions.deserialize_json(
            data["Actions"]
        )
    if data.get("ProposedByMemberId") is not None:
        out["proposed_by_member_id"] = data["ProposedByMemberId"]
    if data.get("ProposedByMemberName") is not None:
        out["proposed_by_member_name"] = data["ProposedByMemberName"]
    if data.get("Status") is not None:
        import capo_managedblockchain.types.proposal_status

        out["status"] = capo_managedblockchain.types.proposal_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("ExpirationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["expiration_date"] = (
            capo_managedblockchain.types.timestamp.deserialize_json(
                data["ExpirationDate"]
            )
        )
    if data.get("YesVoteCount") is not None:
        out["yes_vote_count"] = data["YesVoteCount"]
    if data.get("NoVoteCount") is not None:
        out["no_vote_count"] = data["NoVoteCount"]
    if data.get("OutstandingVoteCount") is not None:
        out["outstanding_vote_count"] = data["OutstandingVoteCount"]
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.output_tag_map

        out["tags"] = capo_managedblockchain.types.output_tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
