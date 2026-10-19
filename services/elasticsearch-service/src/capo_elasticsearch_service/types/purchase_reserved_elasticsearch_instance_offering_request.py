"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PurchaseReservedElasticsearchInstanceOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.instance_count
    import capo_elasticsearch_service.types.reservation_token


class PurchaseReservedElasticsearchInstanceOfferingRequest(TypedDict, closed=True):
    reserved_elasticsearch_instance_offering_id: (
        "capo_elasticsearch_service.types.guid.GUID"
    )
    """<p>The ID of the reserved Elasticsearch instance offering to purchase.</p>"""
    reservation_name: (
        "capo_elasticsearch_service.types.reservation_token.ReservationToken"
    )
    """<p>A customer-specified identifier to track this reservation.</p>"""
    instance_count: NotRequired[
        "capo_elasticsearch_service.types.instance_count.InstanceCount"
    ]
    """<p>The number of Elasticsearch instances to reserve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseReservedElasticsearchInstanceOfferingRequest) -> dict:
    out: dict = {}
    out["ReservedElasticsearchInstanceOfferingId"] = value[
        "reserved_elasticsearch_instance_offering_id"
    ]
    out["ReservationName"] = value["reservation_name"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_json(
    data: dict,
) -> PurchaseReservedElasticsearchInstanceOfferingRequest:
    out: PurchaseReservedElasticsearchInstanceOfferingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReservedElasticsearchInstanceOfferingId") is not None:
        out["reserved_elasticsearch_instance_offering_id"] = data[
            "ReservedElasticsearchInstanceOfferingId"
        ]
    else:
        out["reserved_elasticsearch_instance_offering_id"] = ""
    if data.get("ReservationName") is not None:
        out["reservation_name"] = data["ReservationName"]
    else:
        out["reservation_name"] = ""
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    return out
