"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssociationsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.associations_list
    import capo_devops_agent.types.next_token


class ListAssociationsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token to retrieve the next page of results, if there are more results.</p>"""
    associations: "capo_devops_agent.types.associations_list.AssociationsList"
    """<p>The list of associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_devops_agent.types.associations_list

    out["associations"] = capo_devops_agent.types.associations_list.serialize_json(
        value["associations"]
    )
    return out


def deserialize_json(data: dict) -> ListAssociationsOutput:
    out: ListAssociationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("associations") is not None:
        import capo_devops_agent.types.associations_list

        out["associations"] = (
            capo_devops_agent.types.associations_list.deserialize_json(
                data["associations"]
            )
        )
    else:
        out["associations"] = []
    return out


def redact_sensitive(value: ListAssociationsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "associations" in value:
        import capo_devops_agent.types.associations_list

        out["associations"] = (
            capo_devops_agent.types.associations_list.redact_sensitive(
                value["associations"]
            )
        )
    return out
