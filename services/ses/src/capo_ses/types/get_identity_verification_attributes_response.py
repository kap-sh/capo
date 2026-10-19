"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityVerificationAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.verification_attributes


class GetIdentityVerificationAttributesResponse(TypedDict, closed=True):
    verification_attributes: (
        "capo_ses.types.verification_attributes.VerificationAttributes"
    )
    """<p>A map of Identities to IdentityVerificationAttributes objects.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityVerificationAttributesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.verification_attributes

    capo_ses.types.verification_attributes.serialize_query(
        value["verification_attributes"], pairs, f"{key_prefix}VerificationAttributes"
    )


def deserialize_query(el: Element) -> GetIdentityVerificationAttributesResponse:
    out: GetIdentityVerificationAttributesResponse = {}  # type: ignore[typeddict-item]
    child_verification_attributes = el.find("VerificationAttributes")
    if child_verification_attributes is not None:
        import capo_ses.types.verification_attributes

        out["verification_attributes"] = (
            capo_ses.types.verification_attributes.deserialize_query(
                child_verification_attributes
            )
        )
    else:
        out["verification_attributes"] = {}
    return out
