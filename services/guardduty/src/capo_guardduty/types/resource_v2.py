"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceV2``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_resource_type
    import capo_guardduty.types.resource_data
    import capo_guardduty.types.string
    import capo_guardduty.types.tags


class ResourceV2(TypedDict, closed=True):
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the resource.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the resource.</p>"""
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID to which the resource belongs.</p>"""
    resource_type: NotRequired[
        "capo_guardduty.types.finding_resource_type.FindingResourceType"
    ]
    """<p>The type of the Amazon Web Services resource.</p>"""
    region: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services Region where the resource belongs.</p>"""
    service: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services service of the resource.</p>"""
    cloud_partition: NotRequired["capo_guardduty.types.string.String"]
    """<p>The cloud partition within the Amazon Web Services Region to which the resource belongs.</p>"""
    tags: NotRequired["capo_guardduty.types.tags.Tags"]
    """<p>Contains information about the tags associated with the resource.</p>"""
    data: NotRequired["capo_guardduty.types.resource_data.ResourceData"]
    """<p>Contains information about the Amazon Web Services resource associated with the activity that prompted GuardDuty to generate a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceV2) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "name" in value:
        out["name"] = value["name"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "resource_type" in value:
        import capo_guardduty.types.finding_resource_type

        out["resourceType"] = capo_guardduty.types.finding_resource_type.serialize_json(
            value["resource_type"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "service" in value:
        out["service"] = value["service"]
    if "cloud_partition" in value:
        out["cloudPartition"] = value["cloud_partition"]
    if "tags" in value:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.serialize_json(value["tags"])
    if "data" in value:
        import capo_guardduty.types.resource_data

        out["data"] = capo_guardduty.types.resource_data.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> ResourceV2:
    out: ResourceV2 = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("resourceType") is not None:
        import capo_guardduty.types.finding_resource_type

        out["resource_type"] = (
            capo_guardduty.types.finding_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("cloudPartition") is not None:
        out["cloud_partition"] = data["cloudPartition"]
    if data.get("tags") is not None:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.deserialize_json(data["tags"])
    if data.get("data") is not None:
        import capo_guardduty.types.resource_data

        out["data"] = capo_guardduty.types.resource_data.deserialize_json(data["data"])
    return out


def redact_sensitive(value: ResourceV2) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_guardduty.types.resource_data

        out["data"] = capo_guardduty.types.resource_data.redact_sensitive(value["data"])
    return out
