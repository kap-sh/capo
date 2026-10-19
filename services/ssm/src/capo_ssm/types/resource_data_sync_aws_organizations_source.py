"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncAwsOrganizationsSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_organization_source_type
    import capo_ssm.types.resource_data_sync_organizational_unit_list


class ResourceDataSyncAwsOrganizationsSource(TypedDict, closed=True):
    organization_source_type: "capo_ssm.types.resource_data_sync_organization_source_type.ResourceDataSyncOrganizationSourceType"
    """<p>If an Amazon Web Services organization is present, this is either <code>OrganizationalUnits</code> or <code>EntireOrganization</code>. For <code>OrganizationalUnits</code>, the data is aggregated from a set of organization units. For <code>EntireOrganization</code>, the data is aggregated from the entire Amazon Web Services organization.</p>"""
    organizational_units: NotRequired[
        "capo_ssm.types.resource_data_sync_organizational_unit_list.ResourceDataSyncOrganizationalUnitList"
    ]
    """<p>The Organizations organization units included in the sync.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncAwsOrganizationsSource) -> dict:
    out: dict = {}
    out["OrganizationSourceType"] = value["organization_source_type"]
    if "organizational_units" in value:
        import capo_ssm.types.resource_data_sync_organizational_unit_list

        out["OrganizationalUnits"] = (
            capo_ssm.types.resource_data_sync_organizational_unit_list.serialize_aws_json_1_1(
                value["organizational_units"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncAwsOrganizationsSource:
    out: ResourceDataSyncAwsOrganizationsSource = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationSourceType") is not None:
        out["organization_source_type"] = data["OrganizationSourceType"]
    else:
        out["organization_source_type"] = ""
    if data.get("OrganizationalUnits") is not None:
        import capo_ssm.types.resource_data_sync_organizational_unit_list

        out["organizational_units"] = (
            capo_ssm.types.resource_data_sync_organizational_unit_list.deserialize_aws_json_1_1(
                data["OrganizationalUnits"]
            )
        )
    return out
