"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListReservationOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.reservation_offerings_list


class ListReservationOfferingsResponse(TypedDict, closed=True):
    reservation_offerings_list: "capo_redshift_serverless.types.reservation_offerings_list.ReservationOfferingsList"
    """<p>The returned list of reservation offerings.</p>"""
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReservationOfferingsResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.reservation_offerings_list

    out["reservationOfferingsList"] = (
        capo_redshift_serverless.types.reservation_offerings_list.serialize_aws_json_1_1(
            value["reservation_offerings_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReservationOfferingsResponse:
    out: ListReservationOfferingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("reservationOfferingsList") is not None:
        import capo_redshift_serverless.types.reservation_offerings_list

        out["reservation_offerings_list"] = (
            capo_redshift_serverless.types.reservation_offerings_list.deserialize_aws_json_1_1(
                data["reservationOfferingsList"]
            )
        )
    else:
        out["reservation_offerings_list"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
