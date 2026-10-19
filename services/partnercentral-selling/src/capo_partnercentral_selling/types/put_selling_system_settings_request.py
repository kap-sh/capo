"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PutSellingSystemSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_role_identifier


class PutSellingSystemSettingsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the settings will be updated. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>"""
    resource_snapshot_job_role_identifier: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_role_identifier.ResourceSnapshotJobRoleIdentifier"
    ]
    """<p>Specifies the ARN of the IAM Role used for resource snapshot job executions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutSellingSystemSettingsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "resource_snapshot_job_role_identifier" in value:
        out["ResourceSnapshotJobRoleIdentifier"] = value[
            "resource_snapshot_job_role_identifier"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutSellingSystemSettingsRequest:
    out: PutSellingSystemSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ResourceSnapshotJobRoleIdentifier") is not None:
        out["resource_snapshot_job_role_identifier"] = data[
            "ResourceSnapshotJobRoleIdentifier"
        ]
    return out
