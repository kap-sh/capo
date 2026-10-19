"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListAssertionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.assertion_list
    import capo_resiliencehubv2.types.next_token


class ListAssertionsResponse(TypedDict, closed=True):
    assertions: "capo_resiliencehubv2.types.assertion_list.AssertionList"
    """<p>The list of assertions.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssertionsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.assertion_list

    out["assertions"] = capo_resiliencehubv2.types.assertion_list.serialize_json(
        value["assertions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssertionsResponse:
    out: ListAssertionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assertions") is not None:
        import capo_resiliencehubv2.types.assertion_list

        out["assertions"] = capo_resiliencehubv2.types.assertion_list.deserialize_json(
            data["assertions"]
        )
    else:
        out["assertions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
