"""Generated from Smithy shape ``com.amazonaws.s3#InventoryConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.inventory_destination
    import capo_s3.types.inventory_filter
    import capo_s3.types.inventory_id
    import capo_s3.types.inventory_included_object_versions
    import capo_s3.types.inventory_optional_fields
    import capo_s3.types.inventory_schedule
    import capo_s3.types.is_enabled


class InventoryConfiguration(TypedDict, closed=True):
    destination: "capo_s3.types.inventory_destination.InventoryDestination"
    """<p>Contains information about where to publish the inventory results.</p>"""
    is_enabled: "capo_s3.types.is_enabled.IsEnabled"
    """<p>Specifies whether the inventory is enabled or disabled. If set to <code>True</code>, an inventory list is generated. If set to <code>False</code>, no inventory list is generated.</p>"""
    filter: NotRequired["capo_s3.types.inventory_filter.InventoryFilter"]
    """<p>Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.</p>"""
    id: "capo_s3.types.inventory_id.InventoryId"
    """<p>The ID used to identify the inventory configuration.</p>"""
    included_object_versions: "capo_s3.types.inventory_included_object_versions.InventoryIncludedObjectVersions"
    """<p>Object versions to include in the inventory list. If set to <code>All</code>, the list includes all the object versions, which adds the version-related fields <code>VersionId</code>, <code>IsLatest</code>, and <code>DeleteMarker</code> to the list. If set to <code>Current</code>, the list does not contain these version-related fields.</p>"""
    optional_fields: NotRequired[
        "capo_s3.types.inventory_optional_fields.InventoryOptionalFields"
    ]
    """<p>Contains the optional fields that are included in the inventory results.</p> <note> <p>The following optional fields are supported for directory buckets <code>Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | EncryptionStatus | BucketKeyStatus | ChecksumAlgorithm | LifecycleExpirationDate.</code> Throws MalformedXML error if unsupported optional field is provided. </p> </note>"""
    schedule: "capo_s3.types.inventory_schedule.InventorySchedule"
    """<p>Specifies the schedule for generating inventory results.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventoryConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.inventory_destination

    capo_s3.types.inventory_destination.serialize_xml(
        value["destination"], el, "Destination"
    )
    SubElement(el, "IsEnabled").text = "true" if value["is_enabled"] else "false"
    if "filter" in value:
        import capo_s3.types.inventory_filter

        capo_s3.types.inventory_filter.serialize_xml(value["filter"], el, "Filter")
    SubElement(el, "Id").text = str(value["id"])
    import capo_s3.types.inventory_included_object_versions

    capo_s3.types.inventory_included_object_versions.serialize_xml(
        value["included_object_versions"], el, "IncludedObjectVersions"
    )
    if "optional_fields" in value:
        import capo_s3.types.inventory_optional_fields

        capo_s3.types.inventory_optional_fields.serialize_xml(
            value["optional_fields"], el, "OptionalFields"
        )
    import capo_s3.types.inventory_schedule

    capo_s3.types.inventory_schedule.serialize_xml(value["schedule"], el, "Schedule")


def deserialize_xml(el: Element) -> InventoryConfiguration:
    out: InventoryConfiguration = {}  # type: ignore[typeddict-item]
    child_destination = el.find("Destination")
    if child_destination is not None:
        import capo_s3.types.inventory_destination

        out["destination"] = capo_s3.types.inventory_destination.deserialize_xml(
            child_destination
        )
    else:
        raise DeserializationError("InventoryConfiguration.destination required")
    child_is_enabled = el.find("IsEnabled")
    if child_is_enabled is not None:
        out["is_enabled"] = (child_is_enabled.text or "").lower() == "true"
    else:
        out["is_enabled"] = False
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.inventory_filter

        out["filter"] = capo_s3.types.inventory_filter.deserialize_xml(child_filter)
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_included_object_versions = el.find("IncludedObjectVersions")
    if child_included_object_versions is not None:
        import capo_s3.types.inventory_included_object_versions

        out["included_object_versions"] = (
            capo_s3.types.inventory_included_object_versions.deserialize_xml(
                child_included_object_versions
            )
        )
    else:
        import typing

        out["included_object_versions"] = typing.cast(
            "capo_s3.types.inventory_included_object_versions.InventoryIncludedObjectVersions",
            "",
        )
    child_optional_fields = el.find("OptionalFields")
    if child_optional_fields is not None:
        import capo_s3.types.inventory_optional_fields

        out["optional_fields"] = (
            capo_s3.types.inventory_optional_fields.deserialize_xml(
                child_optional_fields
            )
        )
    child_schedule = el.find("Schedule")
    if child_schedule is not None:
        import capo_s3.types.inventory_schedule

        out["schedule"] = capo_s3.types.inventory_schedule.deserialize_xml(
            child_schedule
        )
    else:
        raise DeserializationError("InventoryConfiguration.schedule required")
    return out


def redact_sensitive(value: InventoryConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination" in value:
        import capo_s3.types.inventory_destination

        out["destination"] = capo_s3.types.inventory_destination.redact_sensitive(
            value["destination"]
        )
    return out
