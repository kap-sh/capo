"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.enable_cross_account_visibility


class DeploymentConfiguration(TypedDict, closed=True):
    enable_cross_account_visibility: "capo_network_security_manager.types.enable_cross_account_visibility.EnableCrossAccountVisibility"
    """<p>Specifies whether aggregate synchronization status details for the resources covered by this deployment are visible across accounts. Default: <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentConfiguration) -> dict:
    out: dict = {}
    out["enableCrossAccountVisibility"] = value.get(
        "enable_cross_account_visibility", False
    )
    return out


def deserialize_json(data: dict) -> DeploymentConfiguration:
    out: DeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enableCrossAccountVisibility") is not None:
        out["enable_cross_account_visibility"] = data["enableCrossAccountVisibility"]
    else:
        out["enable_cross_account_visibility"] = False
    return out
