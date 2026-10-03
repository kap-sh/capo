"""Generated from Smithy shape ``com.amazonaws.securityhub#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cloud_provider_name
    import capo_securityhub.types.data_classification_details
    import capo_securityhub.types.field_map
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.partition
    import capo_securityhub.types.resource_details
    import capo_securityhub.types.resource_owner


class Resource(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the resource that details are provided for. If possible, set <code>Type</code> to one of the supported resource types. For example, if the resource is an EC2 instance, then set <code>Type</code> to <code>AwsEc2Instance</code>.</p> <p>If the resource does not match any of the provided types, then set <code>Type</code> to <code>Other</code>. </p> <p>Length Constraints: Minimum length of 1. Maximum length of 256.</p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical identifier for the given resource type.</p>"""
    partition: NotRequired["capo_securityhub.types.partition.Partition"]
    """<p>The canonical Amazon Web Services partition name that the Region is assigned to.</p>"""
    region: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical Amazon Web Services external Region name where this resource is located.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 16.</p>"""
    provider: NotRequired[
        "capo_securityhub.types.cloud_provider_name.CloudProviderName"
    ]
    """<p>The cloud provider that the resource belongs to. Valid values are <code>AWS</code> and <code>Azure</code>.</p>"""
    owner: NotRequired["capo_securityhub.types.resource_owner.ResourceOwner"]
    """<p>Information about the account and organization that own the resource.</p>"""
    resource_role: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Identifies the role of the resource in the finding. A resource is either the actor or target of the finding activity,</p>"""
    tags: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>A list of Amazon Web Services tags associated with a resource at the time the finding was processed. Tags must follow <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions">Amazon Web Services tag naming limits and requirements</a>.</p>"""
    data_classification: NotRequired[
        "capo_securityhub.types.data_classification_details.DataClassificationDetails"
    ]
    """<p>Contains information about sensitive data that was detected on the resource.</p>"""
    details: NotRequired["capo_securityhub.types.resource_details.ResourceDetails"]
    """<p>Additional details about the resource related to a finding.</p>"""
    application_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the application that is related to a finding. </p>"""
    application_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the application that is related to a finding. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "partition" in value:
        import capo_securityhub.types.partition

        out["Partition"] = capo_securityhub.types.partition.serialize_json(
            value["partition"]
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "provider" in value:
        import capo_securityhub.types.cloud_provider_name

        out["Provider"] = capo_securityhub.types.cloud_provider_name.serialize_json(
            value["provider"]
        )
    if "owner" in value:
        import capo_securityhub.types.resource_owner

        out["Owner"] = capo_securityhub.types.resource_owner.serialize_json(
            value["owner"]
        )
    if "resource_role" in value:
        out["ResourceRole"] = value["resource_role"]
    if "tags" in value:
        import capo_securityhub.types.field_map

        out["Tags"] = capo_securityhub.types.field_map.serialize_json(value["tags"])
    if "data_classification" in value:
        import capo_securityhub.types.data_classification_details

        out["DataClassification"] = (
            capo_securityhub.types.data_classification_details.serialize_json(
                value["data_classification"]
            )
        )
    if "details" in value:
        import capo_securityhub.types.resource_details

        out["Details"] = capo_securityhub.types.resource_details.serialize_json(
            value["details"]
        )
    if "application_name" in value:
        out["ApplicationName"] = value["application_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Partition") is not None:
        import capo_securityhub.types.partition

        out["partition"] = capo_securityhub.types.partition.deserialize_json(
            data["Partition"]
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("Provider") is not None:
        import capo_securityhub.types.cloud_provider_name

        out["provider"] = capo_securityhub.types.cloud_provider_name.deserialize_json(
            data["Provider"]
        )
    if data.get("Owner") is not None:
        import capo_securityhub.types.resource_owner

        out["owner"] = capo_securityhub.types.resource_owner.deserialize_json(
            data["Owner"]
        )
    if data.get("ResourceRole") is not None:
        out["resource_role"] = data["ResourceRole"]
    if data.get("Tags") is not None:
        import capo_securityhub.types.field_map

        out["tags"] = capo_securityhub.types.field_map.deserialize_json(data["Tags"])
    if data.get("DataClassification") is not None:
        import capo_securityhub.types.data_classification_details

        out["data_classification"] = (
            capo_securityhub.types.data_classification_details.deserialize_json(
                data["DataClassification"]
            )
        )
    if data.get("Details") is not None:
        import capo_securityhub.types.resource_details

        out["details"] = capo_securityhub.types.resource_details.deserialize_json(
            data["Details"]
        )
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out
