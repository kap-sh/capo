"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPrivateConnectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.private_connection_summary_list


class ListPrivateConnectionsOutput(TypedDict, closed=True):
    private_connections: "capo_devops_agent.types.private_connection_summary_list.PrivateConnectionSummaryList"
    """<p>The list of Private Connections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateConnectionsOutput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.private_connection_summary_list

    out["privateConnections"] = (
        capo_devops_agent.types.private_connection_summary_list.serialize_json(
            value["private_connections"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListPrivateConnectionsOutput:
    out: ListPrivateConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("privateConnections") is not None:
        import capo_devops_agent.types.private_connection_summary_list

        out["private_connections"] = (
            capo_devops_agent.types.private_connection_summary_list.deserialize_json(
                data["privateConnections"]
            )
        )
    else:
        out["private_connections"] = []
    return out
