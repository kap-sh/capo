"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.error_type
    import capo_managedblockchain_query.types.owner_identifier
    import capo_managedblockchain_query.types.token_identifier


class BatchGetTokenBalanceErrorItem(TypedDict, closed=True):
    token_identifier: NotRequired[
        "capo_managedblockchain_query.types.token_identifier.TokenIdentifier"
    ]
    owner_identifier: NotRequired[
        "capo_managedblockchain_query.types.owner_identifier.OwnerIdentifier"
    ]
    at_blockchain_instant: NotRequired[
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]
    error_code: "str"
    """<p>The error code associated with the error.</p>"""
    error_message: "str"
    """<p>The message associated with the error.</p>"""
    error_type: "capo_managedblockchain_query.types.error_type.ErrorType"
    """<p>The type of error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceErrorItem) -> dict:
    out: dict = {}
    if "token_identifier" in value:
        import capo_managedblockchain_query.types.token_identifier

        out["tokenIdentifier"] = (
            capo_managedblockchain_query.types.token_identifier.serialize_json(
                value["token_identifier"]
            )
        )
    if "owner_identifier" in value:
        import capo_managedblockchain_query.types.owner_identifier

        out["ownerIdentifier"] = (
            capo_managedblockchain_query.types.owner_identifier.serialize_json(
                value["owner_identifier"]
            )
        )
    if "at_blockchain_instant" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["atBlockchainInstant"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["at_blockchain_instant"]
            )
        )
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    out["errorType"] = value["error_type"]
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceErrorItem:
    out: BatchGetTokenBalanceErrorItem = {}  # type: ignore[typeddict-item]
    if data.get("tokenIdentifier") is not None:
        import capo_managedblockchain_query.types.token_identifier

        out["token_identifier"] = (
            capo_managedblockchain_query.types.token_identifier.deserialize_json(
                data["tokenIdentifier"]
            )
        )
    if data.get("ownerIdentifier") is not None:
        import capo_managedblockchain_query.types.owner_identifier

        out["owner_identifier"] = (
            capo_managedblockchain_query.types.owner_identifier.deserialize_json(
                data["ownerIdentifier"]
            )
        )
    if data.get("atBlockchainInstant") is not None:
        import capo_managedblockchain_query.types.blockchain_instant

        out["at_blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["atBlockchainInstant"]
            )
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    if data.get("errorType") is not None:
        out["error_type"] = data["errorType"]
    else:
        out["error_type"] = ""
    return out
