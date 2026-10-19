"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name


class DeleteServiceSyncConfigInput(TypedDict, closed=True):
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want to delete the service sync configuration for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceSyncConfigInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceSyncConfigInput:
    out: DeleteServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    return out
