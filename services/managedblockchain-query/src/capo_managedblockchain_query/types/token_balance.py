"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TokenBalance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.owner_identifier
    import capo_managedblockchain_query.types.token_identifier


class TokenBalance(TypedDict, closed=True):
    owner_identifier: NotRequired[
        "capo_managedblockchain_query.types.owner_identifier.OwnerIdentifier"
    ]
    """<p>The container for the identifier of the owner.</p>"""
    token_identifier: NotRequired[
        "capo_managedblockchain_query.types.token_identifier.TokenIdentifier"
    ]
    """<p>The identifier for the token, including the unique token ID and its blockchain network.</p>"""
    balance: "str"
    """<p>The container of the token balance.</p>"""
    at_blockchain_instant: (
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    )
    """<p>The time for when the TokenBalance is requested or the current time if a time is not provided in the request.</p> <note> <p>This time will only be recorded up to the second.</p> </note>"""
    last_updated_time: NotRequired[
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]
    """<p>The <code>Timestamp</code> of the last transaction at which the balance for the token in the wallet was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenBalance) -> dict:
    out: dict = {}
    if "owner_identifier" in value:
        import capo_managedblockchain_query.types.owner_identifier

        out["ownerIdentifier"] = (
            capo_managedblockchain_query.types.owner_identifier.serialize_json(
                value["owner_identifier"]
            )
        )
    if "token_identifier" in value:
        import capo_managedblockchain_query.types.token_identifier

        out["tokenIdentifier"] = (
            capo_managedblockchain_query.types.token_identifier.serialize_json(
                value["token_identifier"]
            )
        )
    out["balance"] = value["balance"]
    import capo_managedblockchain_query.types.blockchain_instant

    out["atBlockchainInstant"] = (
        capo_managedblockchain_query.types.blockchain_instant.serialize_json(
            value["at_blockchain_instant"]
        )
    )
    if "last_updated_time" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["lastUpdatedTime"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> TokenBalance:
    out: TokenBalance = {}  # type: ignore[typeddict-item]
    if data.get("ownerIdentifier") is not None:
        import capo_managedblockchain_query.types.owner_identifier

        out["owner_identifier"] = (
            capo_managedblockchain_query.types.owner_identifier.deserialize_json(
                data["ownerIdentifier"]
            )
        )
    if data.get("tokenIdentifier") is not None:
        import capo_managedblockchain_query.types.token_identifier

        out["token_identifier"] = (
            capo_managedblockchain_query.types.token_identifier.deserialize_json(
                data["tokenIdentifier"]
            )
        )
    if data.get("balance") is not None:
        out["balance"] = data["balance"]
    else:
        out["balance"] = ""
    if data.get("atBlockchainInstant") is not None:
        import capo_managedblockchain_query.types.blockchain_instant

        out["at_blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["atBlockchainInstant"]
            )
        )
    else:
        raise DeserializationError("TokenBalance.at_blockchain_instant required")
    if data.get("lastUpdatedTime") is not None:
        import capo_managedblockchain_query.types.blockchain_instant

        out["last_updated_time"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    return out
