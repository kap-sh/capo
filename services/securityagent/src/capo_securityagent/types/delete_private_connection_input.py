"""Generated from Smithy shape ``com.amazonaws.securityagent#DeletePrivateConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.private_connection_name


class DeletePrivateConnectionInput(TypedDict, closed=True):
    private_connection_name: (
        "capo_securityagent.types.private_connection_name.PrivateConnectionName"
    )
    """<p>The name of the private connection to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateConnectionInput) -> dict:
    out: dict = {}
    out["privateConnectionName"] = value["private_connection_name"]
    return out


def deserialize_json(data: dict) -> DeletePrivateConnectionInput:
    out: DeletePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    else:
        out["private_connection_name"] = ""
    return out
