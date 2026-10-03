"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesListing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_count_list
    import capo_ec2.types.listing_status
    import capo_ec2.types.price_schedule_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ReservedInstancesListing(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    create_date: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time the listing was created.</p>"""
    instance_counts: NotRequired["capo_ec2.types.instance_count_list.InstanceCountList"]
    """<p>The number of instances in this state.</p>"""
    price_schedules: NotRequired["capo_ec2.types.price_schedule_list.PriceScheduleList"]
    """<p>The price of the Reserved Instance listing.</p>"""
    reserved_instances_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
    reserved_instances_listing_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance listing.</p>"""
    status: NotRequired["capo_ec2.types.listing_status.ListingStatus"]
    """<p>The status of the Reserved Instance listing.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current status of the Reserved Instance listing. The response can be blank.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    update_date: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The last modified timestamp of the listing.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesListing, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "create_date" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "instance_counts" in value:
        import capo_ec2.types.instance_count_list

        capo_ec2.types.instance_count_list.serialize_ec2_query(
            value["instance_counts"], pairs, f"{key_prefix}InstanceCounts"
        )
    if "price_schedules" in value:
        import capo_ec2.types.price_schedule_list

        capo_ec2.types.price_schedule_list.serialize_ec2_query(
            value["price_schedules"], pairs, f"{key_prefix}PriceSchedules"
        )
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "reserved_instances_listing_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedInstancesListingId",
                str(value["reserved_instances_listing_id"]),
            )
        )
    if "status" in value:
        import capo_ec2.types.listing_status

        capo_ec2.types.listing_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "update_date" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["update_date"], pairs, f"{key_prefix}UpdateDate"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesListing:
    out: ReservedInstancesListing = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_create_date = el.find("createDate")
    if child_create_date is not None:
        import capo_ec2.types.date_time

        out["create_date"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_date
        )
    child_instance_counts = el.find("instanceCounts")
    if child_instance_counts is not None:
        import capo_ec2.types.instance_count_list

        out["instance_counts"] = (
            capo_ec2.types.instance_count_list.deserialize_ec2_query(
                child_instance_counts
            )
        )
    child_price_schedules = el.find("priceSchedules")
    if child_price_schedules is not None:
        import capo_ec2.types.price_schedule_list

        out["price_schedules"] = (
            capo_ec2.types.price_schedule_list.deserialize_ec2_query(
                child_price_schedules
            )
        )
    child_reserved_instances_id = el.find("reservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_reserved_instances_listing_id = el.find("reservedInstancesListingId")
    if child_reserved_instances_listing_id is not None:
        out["reserved_instances_listing_id"] = str(
            child_reserved_instances_listing_id.text or ""
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.listing_status

        out["status"] = capo_ec2.types.listing_status.deserialize_ec2_query(
            child_status
        )
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_update_date = el.find("updateDate")
    if child_update_date is not None:
        import capo_ec2.types.date_time

        out["update_date"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_update_date
        )
    return out
