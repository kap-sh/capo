"""Generated from Smithy shape ``com.amazonaws.s3tables#ReportOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.checksum_crc64_nvme
    import capo_s3tables.types.finding_category_counts
    import capo_s3tables.types.migration_report_prefix
    import capo_s3tables.types.report_object_key


class ReportOverview(TypedDict, closed=True):
    prefix: NotRequired[
        "capo_s3tables.types.migration_report_prefix.MigrationReportPrefix"
    ]
    """<p>The key prefix that the report is written under.</p>"""
    key: NotRequired["capo_s3tables.types.report_object_key.ReportObjectKey"]
    """<p>The key of the report object in the bucket. For the object compatibility and object migration reports, this is the report's manifest; for the table compatibility report, it is the report itself. This value is returned after the migration writes the report. A migration doesn't always write every report. For example, a migration that fails during planning doesn't write the object migration report.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3tables.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>The Base64-encoded CRC64NVME checksum of the object that <code>key</code> names. For a report that has a manifest, the manifest lists the checksum of each report file. This value is returned after the migration writes the report.</p>"""
    invalid_findings: NotRequired[
        "capo_s3tables.types.finding_category_counts.FindingCategoryCounts"
    ]
    """<p>For the compatibility reports, the number of blocking findings in each category. The object compatibility report counts each blocked object once, under its most severe finding. Categories with no blocking findings are left out.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportOverview) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    if "key" in value:
        out["key"] = value["key"]
    if "checksum_crc64_nvme" in value:
        out["checksumCRC64NVME"] = value["checksum_crc64_nvme"]
    if "invalid_findings" in value:
        import capo_s3tables.types.finding_category_counts

        out["invalidFindings"] = (
            capo_s3tables.types.finding_category_counts.serialize_json(
                value["invalid_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReportOverview:
    out: ReportOverview = {}  # type: ignore[typeddict-item]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("checksumCRC64NVME") is not None:
        out["checksum_crc64_nvme"] = data["checksumCRC64NVME"]
    if data.get("invalidFindings") is not None:
        import capo_s3tables.types.finding_category_counts

        out["invalid_findings"] = (
            capo_s3tables.types.finding_category_counts.deserialize_json(
                data["invalidFindings"]
            )
        )
    return out
