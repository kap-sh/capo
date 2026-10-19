"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedRepository``."""

from typing_extensions import NotRequired, TypedDict


class IntegratedRepository(TypedDict, closed=True):
    integration_id: "str"
    """<p>The unique identifier of the integration that provides access to the repository.</p>"""
    provider_resource_id: "str"
    """<p>The provider-specific resource identifier for the repository.</p>"""
    branch: NotRequired["str"]
    """<p>An optional override for the repository branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedRepository) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["providerResourceId"] = value["provider_resource_id"]
    if "branch" in value:
        out["branch"] = value["branch"]
    return out


def deserialize_json(data: dict) -> IntegratedRepository:
    out: IntegratedRepository = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        out["provider_resource_id"] = ""
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    return out
