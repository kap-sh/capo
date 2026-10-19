"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzedResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.resource_arn
    import capo_accessanalyzer.types.resource_type


class AnalyzedResourceSummary(TypedDict, closed=True):
    resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the analyzed resource.</p>"""
    resource_owner_account: "str"
    """<p>The Amazon Web Services account ID that owns the resource.</p>"""
    resource_type: "capo_accessanalyzer.types.resource_type.ResourceType"
    """<p>The type of resource that was analyzed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzedResourceSummary) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["resourceOwnerAccount"] = value["resource_owner_account"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> AnalyzedResourceSummary:
    out: AnalyzedResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("resourceOwnerAccount") is not None:
        out["resource_owner_account"] = data["resourceOwnerAccount"]
    else:
        out["resource_owner_account"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    return out
