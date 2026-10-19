"""Generated from Smithy shape ``com.amazonaws.appflow#MarketoConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.instance_url


class MarketoConnectorProfileProperties(TypedDict, closed=True):
    instance_url: "capo_appflow.types.instance_url.InstanceUrl"
    """<p> The location of the Marketo resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketoConnectorProfileProperties) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> MarketoConnectorProfileProperties:
    out: MarketoConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if data.get("instanceUrl") is not None:
        out["instance_url"] = data["instanceUrl"]
    else:
        out["instance_url"] = ""
    return out
