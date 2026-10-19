"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListDomainVerificationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.domain_verification_list
    import capo_vpc_lattice.types.next_token


class ListDomainVerificationsResponse(TypedDict, closed=True):
    items: "capo_vpc_lattice.types.domain_verification_list.DomainVerificationList"
    """<p> Information about the domain verifications. </p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p> A pagination token for the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainVerificationsResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.domain_verification_list

    out["items"] = capo_vpc_lattice.types.domain_verification_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainVerificationsResponse:
    out: ListDomainVerificationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_vpc_lattice.types.domain_verification_list

        out["items"] = capo_vpc_lattice.types.domain_verification_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
