"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.boolean
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.timestamp


class DomainSummary(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of the domain that the summary information applies to.</p>"""
    auto_renew: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Indicates whether the domain is automatically renewed upon expiration.</p>"""
    transfer_lock: NotRequired["capo_route_53_domains.types.boolean.Boolean"]
    """<p>Indicates whether a domain is locked from unauthorized transfer to another party.</p>"""
    expiry: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>Expiration date of the domain in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSummary) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "auto_renew" in value:
        out["AutoRenew"] = value["auto_renew"]
    if "transfer_lock" in value:
        out["TransferLock"] = value["transfer_lock"]
    if "expiry" in value:
        import capo_route_53_domains.types.timestamp

        out["Expiry"] = capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
            value["expiry"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("AutoRenew") is not None:
        out["auto_renew"] = data["AutoRenew"]
    if data.get("TransferLock") is not None:
        out["transfer_lock"] = data["TransferLock"]
    if data.get("Expiry") is not None:
        import capo_route_53_domains.types.timestamp

        out["expiry"] = capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
            data["Expiry"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainSummary) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "auto_renew" in value:
        out["AutoRenew"] = value["auto_renew"]
    if "transfer_lock" in value:
        out["TransferLock"] = value["transfer_lock"]
    if "expiry" in value:
        import capo_route_53_domains.types.timestamp

        out["Expiry"] = capo_route_53_domains.types.timestamp.serialize_cbor(
            value["expiry"]
        )
    return out


def deserialize_cbor(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("AutoRenew") is not None:
        out["auto_renew"] = data["AutoRenew"]
    if data.get("TransferLock") is not None:
        out["transfer_lock"] = data["TransferLock"]
    if data.get("Expiry") is not None:
        import capo_route_53_domains.types.timestamp

        out["expiry"] = capo_route_53_domains.types.timestamp.deserialize_cbor(
            data["Expiry"]
        )
    return out
