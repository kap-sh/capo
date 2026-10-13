"""Generated from Smithy shape ``com.amazonaws.ec2#AttachVerifiedAccessTrustProviderResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_instance
    import capo_ec2.types.verified_access_trust_provider


class AttachVerifiedAccessTrustProviderResult(TypedDict, closed=True):
    verified_access_trust_provider: NotRequired[
        "capo_ec2.types.verified_access_trust_provider.VerifiedAccessTrustProvider"
    ]
    """<p>Details about the Verified Access trust provider.</p>"""
    verified_access_instance: NotRequired[
        "capo_ec2.types.verified_access_instance.VerifiedAccessInstance"
    ]
    """<p>Details about the Verified Access instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachVerifiedAccessTrustProviderResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_trust_provider" in value:
        import capo_ec2.types.verified_access_trust_provider

        capo_ec2.types.verified_access_trust_provider.serialize_ec2_query(
            value["verified_access_trust_provider"],
            pairs,
            f"{key_prefix}VerifiedAccessTrustProvider",
        )
    if "verified_access_instance" in value:
        import capo_ec2.types.verified_access_instance

        capo_ec2.types.verified_access_instance.serialize_ec2_query(
            value["verified_access_instance"],
            pairs,
            f"{key_prefix}VerifiedAccessInstance",
        )


def deserialize_ec2_query(el: Element) -> AttachVerifiedAccessTrustProviderResult:
    out: AttachVerifiedAccessTrustProviderResult = {}  # type: ignore[typeddict-item]
    child_verified_access_trust_provider = el.find("verifiedAccessTrustProvider")
    if child_verified_access_trust_provider is not None:
        import capo_ec2.types.verified_access_trust_provider

        out["verified_access_trust_provider"] = (
            capo_ec2.types.verified_access_trust_provider.deserialize_ec2_query(
                child_verified_access_trust_provider
            )
        )
    child_verified_access_instance = el.find("verifiedAccessInstance")
    if child_verified_access_instance is not None:
        import capo_ec2.types.verified_access_instance

        out["verified_access_instance"] = (
            capo_ec2.types.verified_access_instance.deserialize_ec2_query(
                child_verified_access_instance
            )
        )
    return out


def redact_sensitive(value: AttachVerifiedAccessTrustProviderResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "verified_access_trust_provider" in value:
        import capo_ec2.types.verified_access_trust_provider

        out["verified_access_trust_provider"] = (
            capo_ec2.types.verified_access_trust_provider.redact_sensitive(
                value["verified_access_trust_provider"]
            )
        )
    return out
