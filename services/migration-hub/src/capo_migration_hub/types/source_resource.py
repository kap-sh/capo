"""Generated from Smithy shape ``com.amazonaws.migrationhub#SourceResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.source_resource_description
    import capo_migration_hub.types.source_resource_name
    import capo_migration_hub.types.status_detail


class SourceResource(TypedDict, closed=True):
    name: "capo_migration_hub.types.source_resource_name.SourceResourceName"
    """<p>This is the name that you want to use to identify the resource. If the resource is an AWS resource, we recommend that you set this parameter to the ARN of the resource.</p>"""
    description: NotRequired[
        "capo_migration_hub.types.source_resource_description.SourceResourceDescription"
    ]
    """<p>A description that can be free-form text to record additional detail about the resource for clarity or later reference.</p>"""
    status_detail: NotRequired["capo_migration_hub.types.status_detail.StatusDetail"]
    """<p>A free-form description of the status of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceResource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceResource:
    out: SourceResource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("StatusDetail") is not None:
        out["status_detail"] = data["StatusDetail"]
    return out
