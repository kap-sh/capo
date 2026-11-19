"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementContactsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.acceptor_contact


class GetAgreementContactsOutput(TypedDict, closed=True):
    acceptor_contact: NotRequired[
        "capo_marketplace_agreement.types.acceptor_contact.AcceptorContact"
    ]
    """<p>The contact information that the acceptor provided when creating the agreement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementContactsOutput) -> dict:
    out: dict = {}
    if "acceptor_contact" in value:
        import capo_marketplace_agreement.types.acceptor_contact

        out["acceptorContact"] = (
            capo_marketplace_agreement.types.acceptor_contact.serialize_aws_json_1_0(
                value["acceptor_contact"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementContactsOutput:
    out: GetAgreementContactsOutput = {}  # type: ignore[typeddict-item]
    if data.get("acceptorContact") is not None:
        import capo_marketplace_agreement.types.acceptor_contact

        out["acceptor_contact"] = (
            capo_marketplace_agreement.types.acceptor_contact.deserialize_aws_json_1_0(
                data["acceptorContact"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAgreementContactsOutput) -> dict:
    out: dict = {}
    if "acceptor_contact" in value:
        import capo_marketplace_agreement.types.acceptor_contact

        out["acceptorContact"] = (
            capo_marketplace_agreement.types.acceptor_contact.serialize_cbor(
                value["acceptor_contact"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetAgreementContactsOutput:
    out: GetAgreementContactsOutput = {}  # type: ignore[typeddict-item]
    if data.get("acceptorContact") is not None:
        import capo_marketplace_agreement.types.acceptor_contact

        out["acceptor_contact"] = (
            capo_marketplace_agreement.types.acceptor_contact.deserialize_cbor(
                data["acceptorContact"]
            )
        )
    return out


def redact_sensitive(value: GetAgreementContactsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "acceptor_contact" in value:
        out["acceptor_contact"] = "*** Sensitive Data Redacted ***"
    return out
