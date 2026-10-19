"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListServicesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.registered_services_list


class ListServicesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token to retrieve the next page of results, if there are more results.</p>"""
    services: "capo_devops_agent.types.registered_services_list.RegisteredServicesList"


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_devops_agent.types.registered_services_list

    out["services"] = capo_devops_agent.types.registered_services_list.serialize_json(
        value["services"]
    )
    return out


def deserialize_json(data: dict) -> ListServicesOutput:
    out: ListServicesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("services") is not None:
        import capo_devops_agent.types.registered_services_list

        out["services"] = (
            capo_devops_agent.types.registered_services_list.deserialize_json(
                data["services"]
            )
        )
    else:
        out["services"] = []
    return out


def redact_sensitive(value: ListServicesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "services" in value:
        import capo_devops_agent.types.registered_services_list

        out["services"] = (
            capo_devops_agent.types.registered_services_list.redact_sensitive(
                value["services"]
            )
        )
    return out
