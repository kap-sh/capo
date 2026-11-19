"""Generated from Smithy shape ``com.amazonaws.route53domains#ViewBillingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.page_marker
    import capo_route_53_domains.types.page_max_items
    import capo_route_53_domains.types.timestamp


class ViewBillingRequest(TypedDict, closed=True):
    start: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The beginning date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>"""
    end: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The end date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>"""
    marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current Amazon Web Services account during the specified period is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional billing records. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element. </p> <p>Constraints: The marker must match the value of <code>NextPageMarker</code> that was returned in the previous response.</p>"""
    max_items: NotRequired["capo_route_53_domains.types.page_max_items.PageMaxItems"]
    """<p>The number of billing records to be returned.</p> <p>Default: 20</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewBillingRequest) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_route_53_domains.types.timestamp

        out["Start"] = capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
            value["start"]
        )
    if "end" in value:
        import capo_route_53_domains.types.timestamp

        out["End"] = capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
            value["end"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewBillingRequest:
    out: ViewBillingRequest = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        import capo_route_53_domains.types.timestamp

        out["start"] = capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
            data["Start"]
        )
    if data.get("End") is not None:
        import capo_route_53_domains.types.timestamp

        out["end"] = capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
            data["End"]
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ViewBillingRequest) -> dict:
    out: dict = {}
    if "start" in value:
        import capo_route_53_domains.types.timestamp

        out["Start"] = capo_route_53_domains.types.timestamp.serialize_cbor(
            value["start"]
        )
    if "end" in value:
        import capo_route_53_domains.types.timestamp

        out["End"] = capo_route_53_domains.types.timestamp.serialize_cbor(value["end"])
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_cbor(data: dict) -> ViewBillingRequest:
    out: ViewBillingRequest = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        import capo_route_53_domains.types.timestamp

        out["start"] = capo_route_53_domains.types.timestamp.deserialize_cbor(
            data["Start"]
        )
    if data.get("End") is not None:
        import capo_route_53_domains.types.timestamp

        out["end"] = capo_route_53_domains.types.timestamp.deserialize_cbor(data["End"])
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out
