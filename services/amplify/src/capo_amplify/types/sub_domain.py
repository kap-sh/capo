"""Generated from Smithy shape ``com.amazonaws.amplify#SubDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.dns_record
    import capo_amplify.types.sub_domain_setting
    import capo_amplify.types.verified


class SubDomain(TypedDict, closed=True):
    sub_domain_setting: "capo_amplify.types.sub_domain_setting.SubDomainSetting"
    """<p> Describes the settings for the subdomain. </p>"""
    verified: "capo_amplify.types.verified.Verified"
    """<p> The verified status of the subdomain </p>"""
    dns_record: "capo_amplify.types.dns_record.DNSRecord"
    """<p> The DNS record for the subdomain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubDomain) -> dict:
    out: dict = {}
    import capo_amplify.types.sub_domain_setting

    out["subDomainSetting"] = capo_amplify.types.sub_domain_setting.serialize_json(
        value["sub_domain_setting"]
    )
    out["verified"] = value["verified"]
    out["dnsRecord"] = value["dns_record"]
    return out


def deserialize_json(data: dict) -> SubDomain:
    out: SubDomain = {}  # type: ignore[typeddict-item]
    if data.get("subDomainSetting") is not None:
        import capo_amplify.types.sub_domain_setting

        out["sub_domain_setting"] = (
            capo_amplify.types.sub_domain_setting.deserialize_json(
                data["subDomainSetting"]
            )
        )
    else:
        raise DeserializationError("SubDomain.sub_domain_setting required")
    if data.get("verified") is not None:
        out["verified"] = data["verified"]
    else:
        out["verified"] = False
    if data.get("dnsRecord") is not None:
        out["dns_record"] = data["dnsRecord"]
    else:
        out["dns_record"] = ""
    return out
