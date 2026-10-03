"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFabricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.edition


class NetworkFabricConfiguration(TypedDict, closed=True):
    edition: "capo_managedblockchain.types.edition.Edition"
    """<p>The edition of Amazon Managed Blockchain that the network uses. For more information, see <a href="http://aws.amazon.com/managed-blockchain/pricing/">Amazon Managed Blockchain Pricing</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFabricConfiguration) -> dict:
    out: dict = {}
    import capo_managedblockchain.types.edition

    out["Edition"] = capo_managedblockchain.types.edition.serialize_json(
        value["edition"]
    )
    return out


def deserialize_json(data: dict) -> NetworkFabricConfiguration:
    out: NetworkFabricConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Edition") is not None:
        import capo_managedblockchain.types.edition

        out["edition"] = capo_managedblockchain.types.edition.deserialize_json(
            data["Edition"]
        )
    else:
        raise DeserializationError("NetworkFabricConfiguration.edition required")
    return out
