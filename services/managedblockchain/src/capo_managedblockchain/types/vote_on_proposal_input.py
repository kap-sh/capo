"""Generated from Smithy shape ``com.amazonaws.managedblockchain#VoteOnProposalInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.vote_value


class VoteOnProposalInput(TypedDict, closed=True):
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the network. </p>"""
    proposal_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the proposal. </p>"""
    voter_member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member casting the vote. </p>"""
    vote: "capo_managedblockchain.types.vote_value.VoteValue"
    """<p> The value of the vote. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoteOnProposalInput) -> dict:
    out: dict = {}
    out["VoterMemberId"] = value["voter_member_id"]
    import capo_managedblockchain.types.vote_value

    out["Vote"] = capo_managedblockchain.types.vote_value.serialize_json(value["vote"])
    return out


def deserialize_json(data: dict) -> VoteOnProposalInput:
    out: VoteOnProposalInput = {}  # type: ignore[typeddict-item]
    if data.get("VoterMemberId") is not None:
        out["voter_member_id"] = data["VoterMemberId"]
    else:
        out["voter_member_id"] = ""
    if data.get("Vote") is not None:
        import capo_managedblockchain.types.vote_value

        out["vote"] = capo_managedblockchain.types.vote_value.deserialize_json(
            data["Vote"]
        )
    else:
        import typing

        out["vote"] = typing.cast(
            "capo_managedblockchain.types.vote_value.VoteValue", ""
        )
    return out
