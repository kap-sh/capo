"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseHostReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.currency_code_values
    import capo_ec2.types.offering_id
    import capo_ec2.types.request_host_id_set
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class PurchaseHostReservationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    currency_code: NotRequired["capo_ec2.types.currency_code_values.CurrencyCodeValues"]
    """<p>The currency in which the <code>totalUpfrontPrice</code>, <code>LimitPrice</code>, and <code>totalHourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    host_id_set: NotRequired["capo_ec2.types.request_host_id_set.RequestHostIdSet"]
    """<p>The IDs of the Dedicated Hosts with which the reservation will be associated.</p>"""
    limit_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request fails. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is <code>USD</code>. For example, to indicate a limit price of USD 100, specify 100.00.</p>"""
    offering_id: NotRequired["capo_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the offering.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Dedicated Host Reservation during purchase.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseHostReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "currency_code" in value:
        import capo_ec2.types.currency_code_values

        capo_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{key_prefix}CurrencyCode"
        )
    if "host_id_set" in value:
        import capo_ec2.types.request_host_id_set

        capo_ec2.types.request_host_id_set.serialize_ec2_query(
            value["host_id_set"], pairs, f"{key_prefix}HostIdSet"
        )
    if "limit_price" in value:
        pairs.append((f"{key_prefix}LimitPrice", str(value["limit_price"])))
    if "offering_id" in value:
        pairs.append((f"{key_prefix}OfferingId", str(value["offering_id"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> PurchaseHostReservationRequest:
    out: PurchaseHostReservationRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import capo_ec2.types.currency_code_values

        out["currency_code"] = (
            capo_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_host_id_set = el.find("HostIdSet")
    if child_host_id_set is not None:
        import capo_ec2.types.request_host_id_set

        out["host_id_set"] = capo_ec2.types.request_host_id_set.deserialize_ec2_query(
            child_host_id_set
        )
    child_limit_price = el.find("LimitPrice")
    if child_limit_price is not None:
        out["limit_price"] = str(child_limit_price.text or "")
    child_offering_id = el.find("OfferingId")
    if child_offering_id is not None:
        out["offering_id"] = str(child_offering_id.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
