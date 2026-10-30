"""Generated from Smithy shape ``com.amazonaws.continuum#ListEnvironmentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_list_entries
    import capo_continuum.types.next_token


class ListEnvironmentsOutput(TypedDict, closed=True):
    items: "capo_continuum.types.environment_list_entries.EnvironmentListEntries"
    """Common metadata for the environments in the account, ordered by environmentId descending."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """A pagination token to retrieve the next page of results. Absent when there are no more results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.environment_list_entries

    out["items"] = capo_continuum.types.environment_list_entries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsOutput:
    out: ListEnvironmentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_continuum.types.environment_list_entries

        out["items"] = capo_continuum.types.environment_list_entries.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
