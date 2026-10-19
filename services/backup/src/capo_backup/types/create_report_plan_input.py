"""Generated from Smithy shape ``com.amazonaws.backup#CreateReportPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.report_delivery_channel
    import capo_backup.types.report_plan_description
    import capo_backup.types.report_plan_name
    import capo_backup.types.report_setting
    import capo_backup.types.string
    import capo_backup.types.string_map


class CreateReportPlanInput(TypedDict, closed=True):
    report_plan_name: "capo_backup.types.report_plan_name.ReportPlanName"
    """<p>The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    report_plan_description: NotRequired[
        "capo_backup.types.report_plan_description.ReportPlanDescription"
    ]
    """<p>An optional description of the report plan with a maximum of 1,024 characters.</p>"""
    report_delivery_channel: (
        "capo_backup.types.report_delivery_channel.ReportDeliveryChannel"
    )
    """<p>A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</p>"""
    report_setting: "capo_backup.types.report_setting.ReportSetting"
    """<p>Identifies the report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT </code> </p> <p>If the report template is <code>RESOURCE_COMPLIANCE_REPORT</code> or <code>CONTROL_COMPLIANCE_REPORT</code>, this API resource also describes the report coverage by Amazon Web Services Regions and frameworks.</p>"""
    report_plan_tags: NotRequired["capo_backup.types.string_map.stringMap"]
    """<p>The tags to assign to the report plan.</p>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>CreateReportPlanInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReportPlanInput) -> dict:
    out: dict = {}
    out["ReportPlanName"] = value["report_plan_name"]
    if "report_plan_description" in value:
        out["ReportPlanDescription"] = value["report_plan_description"]
    import capo_backup.types.report_delivery_channel

    out["ReportDeliveryChannel"] = (
        capo_backup.types.report_delivery_channel.serialize_json(
            value["report_delivery_channel"]
        )
    )
    import capo_backup.types.report_setting

    out["ReportSetting"] = capo_backup.types.report_setting.serialize_json(
        value["report_setting"]
    )
    if "report_plan_tags" in value:
        import capo_backup.types.string_map

        out["ReportPlanTags"] = capo_backup.types.string_map.serialize_json(
            value["report_plan_tags"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_json(data: dict) -> CreateReportPlanInput:
    out: CreateReportPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("ReportPlanName") is not None:
        out["report_plan_name"] = data["ReportPlanName"]
    else:
        out["report_plan_name"] = ""
    if data.get("ReportPlanDescription") is not None:
        out["report_plan_description"] = data["ReportPlanDescription"]
    if data.get("ReportDeliveryChannel") is not None:
        import capo_backup.types.report_delivery_channel

        out["report_delivery_channel"] = (
            capo_backup.types.report_delivery_channel.deserialize_json(
                data["ReportDeliveryChannel"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReportPlanInput.report_delivery_channel required"
        )
    if data.get("ReportSetting") is not None:
        import capo_backup.types.report_setting

        out["report_setting"] = capo_backup.types.report_setting.deserialize_json(
            data["ReportSetting"]
        )
    else:
        raise DeserializationError("CreateReportPlanInput.report_setting required")
    if data.get("ReportPlanTags") is not None:
        import capo_backup.types.string_map

        out["report_plan_tags"] = capo_backup.types.string_map.deserialize_json(
            data["ReportPlanTags"]
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
