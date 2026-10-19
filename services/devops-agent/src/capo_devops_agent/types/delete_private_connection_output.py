"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeletePrivateConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.private_connection_status


class DeletePrivateConnectionOutput(TypedDict, closed=True):
    name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""
    status: "capo_devops_agent.types.private_connection_status.PrivateConnectionStatus"
    """<p>The status of the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateConnectionOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_devops_agent.types.private_connection_status

    out["status"] = capo_devops_agent.types.private_connection_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeletePrivateConnectionOutput:
    out: DeletePrivateConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_devops_agent.types.private_connection_status

        out["status"] = (
            capo_devops_agent.types.private_connection_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_devops_agent.types.private_connection_status.PrivateConnectionStatus",
            "",
        )
    return out
