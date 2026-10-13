"""Generated from Smithy shape ``com.amazonaws.repostspace#SupportedEmailDomainsStatus``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.allowed_domains_list
    import capo_repostspace.types.feature_enable_status


class SupportedEmailDomainsStatus(TypedDict, closed=True):
    enabled: NotRequired[
        "capo_repostspace.types.feature_enable_status.FeatureEnableStatus"
    ]
    """<p/>"""
    allowed_domains: NotRequired[
        "capo_repostspace.types.allowed_domains_list.AllowedDomainsList"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportedEmailDomainsStatus) -> dict:
    out: dict = {}
    if "enabled" in value:
        import capo_repostspace.types.feature_enable_status

        out["enabled"] = capo_repostspace.types.feature_enable_status.serialize_json(
            value["enabled"]
        )
    if "allowed_domains" in value:
        import capo_repostspace.types.allowed_domains_list

        out["allowedDomains"] = (
            capo_repostspace.types.allowed_domains_list.serialize_json(
                value["allowed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> SupportedEmailDomainsStatus:
    out: SupportedEmailDomainsStatus = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        import capo_repostspace.types.feature_enable_status

        out["enabled"] = capo_repostspace.types.feature_enable_status.deserialize_json(
            data["enabled"]
        )
    if data.get("allowedDomains") is not None:
        import capo_repostspace.types.allowed_domains_list

        out["allowed_domains"] = (
            capo_repostspace.types.allowed_domains_list.deserialize_json(
                data["allowedDomains"]
            )
        )
    return out


def redact_sensitive(value: SupportedEmailDomainsStatus) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "allowed_domains" in value:
        import capo_repostspace.types.allowed_domains_list

        out["allowed_domains"] = (
            capo_repostspace.types.allowed_domains_list.redact_sensitive(
                value["allowed_domains"]
            )
        )
    return out
