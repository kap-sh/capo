"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListSharedDNSViewsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.shared_dns_views


class ListSharedDNSViewsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    dns_views: "capo_route53globalresolver.types.shared_dns_views.SharedDNSViews"
    """<p>An array of information about the DNS views shared with your Amazon Web Services account, including the Amazon Web Services account that owns each DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSharedDNSViewsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.shared_dns_views

    out["dnsViews"] = capo_route53globalresolver.types.shared_dns_views.serialize_json(
        value["dns_views"]
    )
    return out


def deserialize_json(data: dict) -> ListSharedDNSViewsOutput:
    out: ListSharedDNSViewsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("dnsViews") is not None:
        import capo_route53globalresolver.types.shared_dns_views

        out["dns_views"] = (
            capo_route53globalresolver.types.shared_dns_views.deserialize_json(
                data["dnsViews"]
            )
        )
    else:
        out["dns_views"] = []
    return out
