"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTrunkInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.trunk_interface_association


class AssociateTrunkInterfaceResult(TypedDict, closed=True):
    interface_association: NotRequired[
        "capo_ec2.types.trunk_interface_association.TrunkInterfaceAssociation"
    ]
    """<p>Information about the association between the trunk network interface and branch network interface.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateTrunkInterfaceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "interface_association" in value:
        import capo_ec2.types.trunk_interface_association

        capo_ec2.types.trunk_interface_association.serialize_ec2_query(
            value["interface_association"], pairs, f"{key_prefix}InterfaceAssociation"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> AssociateTrunkInterfaceResult:
    out: AssociateTrunkInterfaceResult = {}  # type: ignore[typeddict-item]
    child_interface_association = el.find("interfaceAssociation")
    if child_interface_association is not None:
        import capo_ec2.types.trunk_interface_association

        out["interface_association"] = (
            capo_ec2.types.trunk_interface_association.deserialize_ec2_query(
                child_interface_association
            )
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
