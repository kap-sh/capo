"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_id
    import capo_ec2.types.image_usage_report_id
    import capo_ec2.types.image_usage_resource_type_name
    import capo_ec2.types.long
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class ImageUsageReportEntry(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_ec2.types.image_usage_resource_type_name.ImageUsageResourceTypeName"
    ]
    """<p>The type of resource (<code>ec2:Instance</code> | <code>ec2:LaunchTemplate</code> | <code>imagebuilder:ImageRecipe</code> | <code>imagebuilder:ContainerRecipe</code>).</p>"""
    report_id: NotRequired["capo_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""
    usage_count: NotRequired["capo_ec2.types.long.Long"]
    """<p>The number of times resources of this type reference this image in the account.</p>"""
    account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the account that uses the image.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the image.</p>"""
    report_creation_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the report creation was initiated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageReportEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "report_id" in value:
        pairs.append((f"{key_prefix}ReportId", str(value["report_id"])))
    if "usage_count" in value:
        pairs.append((f"{key_prefix}UsageCount", str(value["usage_count"])))
    if "account_id" in value:
        pairs.append((f"{key_prefix}AccountId", str(value["account_id"])))
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "report_creation_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["report_creation_time"], pairs, f"{key_prefix}ReportCreationTime"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageReportEntry:
    out: ImageUsageReportEntry = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_report_id = el.find("reportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    child_usage_count = el.find("usageCount")
    if child_usage_count is not None:
        out["usage_count"] = int(child_usage_count.text or "")
    child_account_id = el.find("accountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_report_creation_time = el.find("reportCreationTime")
    if child_report_creation_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["report_creation_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_report_creation_time
            )
        )
    return out
