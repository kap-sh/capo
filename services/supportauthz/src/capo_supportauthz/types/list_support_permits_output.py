"""Generated from Smithy shape ``com.amazonaws.supportauthz#ListSupportPermitsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.next_token
    import capo_supportauthz.types.support_permit_summaries


class ListSupportPermitsOutput(TypedDict, closed=True):
    support_permits: (
        "capo_supportauthz.types.support_permit_summaries.SupportPermitSummaries"
    )
    """<p>The list of support permits.</p>"""
    next_token: NotRequired["capo_supportauthz.types.next_token.NextToken"]
    """<p>The token for the next page of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportPermitsOutput) -> dict:
    out: dict = {}
    import capo_supportauthz.types.support_permit_summaries

    out["supportPermits"] = (
        capo_supportauthz.types.support_permit_summaries.serialize_json(
            value["support_permits"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSupportPermitsOutput:
    out: ListSupportPermitsOutput = {}  # type: ignore[typeddict-item]
    if data.get("supportPermits") is not None:
        import capo_supportauthz.types.support_permit_summaries

        out["support_permits"] = (
            capo_supportauthz.types.support_permit_summaries.deserialize_json(
                data["supportPermits"]
            )
        )
    else:
        raise DeserializationError("ListSupportPermitsOutput.support_permits required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
