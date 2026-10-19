"""Generated from Smithy shape ``com.amazonaws.appflow#DeleteConnectorProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.connector_profile_name


class DeleteConnectorProfileRequest(TypedDict, closed=True):
    connector_profile_name: (
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    )
    """<p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in your account. </p>"""
    force_delete: NotRequired["capo_appflow.types.boolean.Boolean"]
    """<p> Indicates whether Amazon AppFlow should delete the profile, even if it is currently in use in one or more flows. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorProfileRequest) -> dict:
    out: dict = {}
    out["connectorProfileName"] = value["connector_profile_name"]
    if "force_delete" in value:
        out["forceDelete"] = value["force_delete"]
    return out


def deserialize_json(data: dict) -> DeleteConnectorProfileRequest:
    out: DeleteConnectorProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorProfileName") is not None:
        out["connector_profile_name"] = data["connectorProfileName"]
    else:
        out["connector_profile_name"] = ""
    if data.get("forceDelete") is not None:
        out["force_delete"] = data["forceDelete"]
    return out
