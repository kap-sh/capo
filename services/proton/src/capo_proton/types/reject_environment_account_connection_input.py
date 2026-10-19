"""Generated from Smithy shape ``com.amazonaws.proton#RejectEnvironmentAccountConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection_id


class RejectEnvironmentAccountConnectionInput(TypedDict, closed=True):
    id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection to reject.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectEnvironmentAccountConnectionInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectEnvironmentAccountConnectionInput:
    out: RejectEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
