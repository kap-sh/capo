"""Generated from Smithy shape ``com.amazonaws.proton#AcceptEnvironmentAccountConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection_id


class AcceptEnvironmentAccountConnectionInput(TypedDict, closed=True):
    id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptEnvironmentAccountConnectionInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptEnvironmentAccountConnectionInput:
    out: AcceptEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
