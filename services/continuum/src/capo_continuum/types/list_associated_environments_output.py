"""Generated from Smithy shape ``com.amazonaws.continuum#ListAssociatedEnvironmentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.associated_environments
    import capo_continuum.types.next_token


class ListAssociatedEnvironmentsOutput(TypedDict, closed=True):
    associated_environments: (
        "capo_continuum.types.associated_environments.AssociatedEnvironments"
    )
    """Summaries of the Environments associated with this Collector, ordered by environmentArn lexicographically ascending. Each summary has the same fields as a ListEnvironments item but uses an independent model shape. Empty when the Collector has no associations."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """Pagination token for the next page, if present."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedEnvironmentsOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.associated_environments

    out["associatedEnvironments"] = (
        capo_continuum.types.associated_environments.serialize_json(
            value["associated_environments"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedEnvironmentsOutput:
    out: ListAssociatedEnvironmentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("associatedEnvironments") is not None:
        import capo_continuum.types.associated_environments

        out["associated_environments"] = (
            capo_continuum.types.associated_environments.deserialize_json(
                data["associatedEnvironments"]
            )
        )
    else:
        out["associated_environments"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
