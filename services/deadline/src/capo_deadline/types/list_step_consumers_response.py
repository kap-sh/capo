"""Generated from Smithy shape ``com.amazonaws.deadline#ListStepConsumersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.step_consumers


class ListStepConsumersResponse(TypedDict, closed=True):
    consumers: "capo_deadline.types.step_consumers.StepConsumers"
    """The consumers on the list."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: ListStepConsumersResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.step_consumers

    out["consumers"] = capo_deadline.types.step_consumers.serialize_json(
        value["consumers"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStepConsumersResponse:
    out: ListStepConsumersResponse = {}  # type: ignore[typeddict-item]
    if data.get("consumers") is not None:
        import capo_deadline.types.step_consumers

        out["consumers"] = capo_deadline.types.step_consumers.deserialize_json(
            data["consumers"]
        )
    else:
        out["consumers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
