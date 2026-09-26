"""Generated from Smithy shape ``com.amazonaws.supportauthz#ListSupportPermitRequestsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.next_token
    import capo_supportauthz.types.support_permit_requests


class ListSupportPermitRequestsOutput(TypedDict, closed=True):
    support_permit_requests: (
        "capo_supportauthz.types.support_permit_requests.SupportPermitRequests"
    )
    """<p>The list of permit requests.</p>"""
    next_token: NotRequired["capo_supportauthz.types.next_token.NextToken"]
    """<p>The token for the next page of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportPermitRequestsOutput) -> dict:
    out: dict = {}
    import capo_supportauthz.types.support_permit_requests

    out["supportPermitRequests"] = (
        capo_supportauthz.types.support_permit_requests.serialize_json(
            value["support_permit_requests"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSupportPermitRequestsOutput:
    out: ListSupportPermitRequestsOutput = {}  # type: ignore[typeddict-item]
    if data.get("supportPermitRequests") is not None:
        import capo_supportauthz.types.support_permit_requests

        out["support_permit_requests"] = (
            capo_supportauthz.types.support_permit_requests.deserialize_json(
                data["supportPermitRequests"]
            )
        )
    else:
        raise DeserializationError(
            "ListSupportPermitRequestsOutput.support_permit_requests required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
