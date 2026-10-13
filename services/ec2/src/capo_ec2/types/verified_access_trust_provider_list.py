"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProviderList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_trust_provider

VerifiedAccessTrustProviderList: TypeAlias = list[
    "capo_ec2.types.verified_access_trust_provider.VerifiedAccessTrustProvider"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessTrustProviderList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.verified_access_trust_provider

        capo_ec2.types.verified_access_trust_provider.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessTrustProviderList:
    import capo_ec2.types.verified_access_trust_provider

    out: VerifiedAccessTrustProviderList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.verified_access_trust_provider.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> VerifiedAccessTrustProviderList:
    import capo_ec2.types.verified_access_trust_provider

    out: VerifiedAccessTrustProviderList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.verified_access_trust_provider.deserialize_ec2_query(child)
        )
    return out


def redact_sensitive(value: VerifiedAccessTrustProviderList) -> list[Any]:
    import capo_ec2.types.verified_access_trust_provider

    return [
        capo_ec2.types.verified_access_trust_provider.redact_sensitive(item)
        for item in value
    ]
