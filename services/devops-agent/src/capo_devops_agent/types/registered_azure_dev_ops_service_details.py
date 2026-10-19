"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredAzureDevOpsServiceDetails``."""

from typing_extensions import TypedDict


class RegisteredAzureDevOpsServiceDetails(TypedDict, closed=True):
    organization_name: "str"
    """<p>The Azure DevOps Organization name associated with the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredAzureDevOpsServiceDetails) -> dict:
    out: dict = {}
    out["organizationName"] = value["organization_name"]
    return out


def deserialize_json(data: dict) -> RegisteredAzureDevOpsServiceDetails:
    out: RegisteredAzureDevOpsServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    else:
        out["organization_name"] = ""
    return out
