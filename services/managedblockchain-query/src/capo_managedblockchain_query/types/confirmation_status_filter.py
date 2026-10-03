"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ConfirmationStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.confirmation_status_include_list


class ConfirmationStatusFilter(TypedDict, closed=True):
    include: "capo_managedblockchain_query.types.confirmation_status_include_list.ConfirmationStatusIncludeList"
    """<p>The container to determine whether to list results that have only reached <a href="https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality"> <i>finality</i> </a>. Transactions that have reached finality are always part of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmationStatusFilter) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.confirmation_status_include_list

    out["include"] = (
        capo_managedblockchain_query.types.confirmation_status_include_list.serialize_json(
            value["include"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfirmationStatusFilter:
    out: ConfirmationStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("include") is not None:
        import capo_managedblockchain_query.types.confirmation_status_include_list

        out["include"] = (
            capo_managedblockchain_query.types.confirmation_status_include_list.deserialize_json(
                data["include"]
            )
        )
    else:
        raise DeserializationError("ConfirmationStatusFilter.include required")
    return out
