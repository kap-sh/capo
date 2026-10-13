"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFrameworkConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.member_fabric_configuration


class MemberFrameworkConfiguration(TypedDict, closed=True):
    fabric: NotRequired[
        "capo_managedblockchain.types.member_fabric_configuration.MemberFabricConfiguration"
    ]
    """<p>Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses Hyperledger Fabric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFrameworkConfiguration) -> dict:
    out: dict = {}
    if "fabric" in value:
        import capo_managedblockchain.types.member_fabric_configuration

        out["Fabric"] = (
            capo_managedblockchain.types.member_fabric_configuration.serialize_json(
                value["fabric"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberFrameworkConfiguration:
    out: MemberFrameworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Fabric") is not None:
        import capo_managedblockchain.types.member_fabric_configuration

        out["fabric"] = (
            capo_managedblockchain.types.member_fabric_configuration.deserialize_json(
                data["Fabric"]
            )
        )
    return out


def redact_sensitive(value: MemberFrameworkConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fabric" in value:
        import capo_managedblockchain.types.member_fabric_configuration

        out["fabric"] = (
            capo_managedblockchain.types.member_fabric_configuration.redact_sensitive(
                value["fabric"]
            )
        )
    return out
