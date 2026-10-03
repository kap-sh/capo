"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.apply_only_at_cron_interval
    import capo_ssm.types.association_compliance_severity
    import capo_ssm.types.association_dispatch_assume_role_arn
    import capo_ssm.types.association_id
    import capo_ssm.types.association_name
    import capo_ssm.types.association_sync_compliance
    import capo_ssm.types.association_version
    import capo_ssm.types.calendar_name_or_arn_list
    import capo_ssm.types.date_time
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.duration
    import capo_ssm.types.instance_association_output_location
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.parameters
    import capo_ssm.types.schedule_expression
    import capo_ssm.types.schedule_offset
    import capo_ssm.types.target_locations
    import capo_ssm.types.target_maps
    import capo_ssm.types.targets


class AssociationVersionInfo(TypedDict, closed=True):
    association_id: NotRequired["capo_ssm.types.association_id.AssociationId"]
    """<p>The ID created by the system when the association was created.</p>"""
    association_version: NotRequired[
        "capo_ssm.types.association_version.AssociationVersion"
    ]
    """<p>The association version.</p>"""
    created_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the association version was created.</p>"""
    name: NotRequired["capo_ssm.types.document_arn.DocumentARN"]
    """<p>The name specified when the association was created.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of an Amazon Web Services Systems Manager document (SSM document) used when the association version was created.</p>"""
    parameters: NotRequired["capo_ssm.types.parameters.Parameters"]
    """<p>Parameters specified when the association version was created.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The targets specified for the association when the association version was created. </p>"""
    schedule_expression: NotRequired[
        "capo_ssm.types.schedule_expression.ScheduleExpression"
    ]
    """<p>The cron or rate schedule specified for the association when the association version was created.</p>"""
    output_location: NotRequired[
        "capo_ssm.types.instance_association_output_location.InstanceAssociationOutputLocation"
    ]
    """<p>The location in Amazon S3 specified for the association when the association version was created.</p>"""
    association_name: NotRequired["capo_ssm.types.association_name.AssociationName"]
    """<p>The name specified for the association version when the association version was created.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set <code>MaxError</code> to 10%, then the system stops sending the request when the sixth error is received.</p> <p>Executions that are already running an association when <code>MaxErrors</code> is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set <code>MaxConcurrency</code> to 1 so that executions proceed one at a time.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.</p> <p>If a new managed node starts and attempts to run an association while Systems Manager is running <code>MaxConcurrency</code> associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for <code>MaxConcurrency</code>.</p>"""
    compliance_severity: NotRequired[
        "capo_ssm.types.association_compliance_severity.AssociationComplianceSeverity"
    ]
    """<p>The severity level that is assigned to the association.</p>"""
    sync_compliance: NotRequired[
        "capo_ssm.types.association_sync_compliance.AssociationSyncCompliance"
    ]
    """<p>The mode for generating association compliance. You can specify <code>AUTO</code> or <code>MANUAL</code>. In <code>AUTO</code> mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is <code>COMPLIANT</code>. If the association execution doesn't run successfully, the association is <code>NON-COMPLIANT</code>.</p> <p>In <code>MANUAL</code> mode, you must specify the <code>AssociationId</code> as a parameter for the <a>PutComplianceItems</a> API operation. In this case, compliance data isn't managed by State Manager, a tool in Amazon Web Services Systems Manager. It is managed by your direct call to the <a>PutComplianceItems</a> API operation.</p> <p>By default, all associations use <code>AUTO</code> mode.</p>"""
    apply_only_at_cron_interval: (
        "capo_ssm.types.apply_only_at_cron_interval.ApplyOnlyAtCronInterval"
    )
    """<p>By default, when you create new associations, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter isn't supported for rate expressions.</p>"""
    calendar_names: NotRequired[
        "capo_ssm.types.calendar_name_or_arn_list.CalendarNameOrARNList"
    ]
    """<p>The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations for this version only run when that Change Calendar is open. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar">Amazon Web Services Systems Manager Change Calendar</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    target_locations: NotRequired["capo_ssm.types.target_locations.TargetLocations"]
    """<p>The combination of Amazon Web Services Regions and Amazon Web Services accounts where you wanted to run the association when this association version was created.</p>"""
    schedule_offset: NotRequired["capo_ssm.types.schedule_offset.ScheduleOffset"]
    """<p>Number of days to wait after the scheduled day to run an association.</p>"""
    duration: NotRequired["capo_ssm.types.duration.Duration"]
    """<p>The number of hours that an association can run on specified targets. After the resulting cutoff time passes, associations that are currently running are cancelled, and no pending executions are started on remaining targets.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    association_dispatch_assume_role: NotRequired[
        "capo_ssm.types.association_dispatch_assume_role_arn.AssociationDispatchAssumeRoleArn"
    ]
    """<p>A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html"> service-linked role for Systems Manager</a> will be used by default. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationVersionInfo) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_version" in value:
        out["AssociationVersion"] = value["association_version"]
    if "created_date" in value:
        import capo_ssm.types.date_time

        out["CreatedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "parameters" in value:
        import capo_ssm.types.parameters

        out["Parameters"] = capo_ssm.types.parameters.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "output_location" in value:
        import capo_ssm.types.instance_association_output_location

        out["OutputLocation"] = (
            capo_ssm.types.instance_association_output_location.serialize_aws_json_1_1(
                value["output_location"]
            )
        )
    if "association_name" in value:
        out["AssociationName"] = value["association_name"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "compliance_severity" in value:
        import capo_ssm.types.association_compliance_severity

        out["ComplianceSeverity"] = (
            capo_ssm.types.association_compliance_severity.serialize_aws_json_1_1(
                value["compliance_severity"]
            )
        )
    if "sync_compliance" in value:
        import capo_ssm.types.association_sync_compliance

        out["SyncCompliance"] = (
            capo_ssm.types.association_sync_compliance.serialize_aws_json_1_1(
                value["sync_compliance"]
            )
        )
    out["ApplyOnlyAtCronInterval"] = value.get("apply_only_at_cron_interval", False)
    if "calendar_names" in value:
        import capo_ssm.types.calendar_name_or_arn_list

        out["CalendarNames"] = (
            capo_ssm.types.calendar_name_or_arn_list.serialize_aws_json_1_1(
                value["calendar_names"]
            )
        )
    if "target_locations" in value:
        import capo_ssm.types.target_locations

        out["TargetLocations"] = capo_ssm.types.target_locations.serialize_aws_json_1_1(
            value["target_locations"]
        )
    if "schedule_offset" in value:
        out["ScheduleOffset"] = value["schedule_offset"]
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "association_dispatch_assume_role" in value:
        out["AssociationDispatchAssumeRole"] = value["association_dispatch_assume_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationVersionInfo:
    out: AssociationVersionInfo = {}  # type: ignore[typeddict-item]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("AssociationVersion") is not None:
        out["association_version"] = data["AssociationVersion"]
    if data.get("CreatedDate") is not None:
        import capo_ssm.types.date_time

        out["created_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.parameters

        out["parameters"] = capo_ssm.types.parameters.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("OutputLocation") is not None:
        import capo_ssm.types.instance_association_output_location

        out["output_location"] = (
            capo_ssm.types.instance_association_output_location.deserialize_aws_json_1_1(
                data["OutputLocation"]
            )
        )
    if data.get("AssociationName") is not None:
        out["association_name"] = data["AssociationName"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("ComplianceSeverity") is not None:
        import capo_ssm.types.association_compliance_severity

        out["compliance_severity"] = (
            capo_ssm.types.association_compliance_severity.deserialize_aws_json_1_1(
                data["ComplianceSeverity"]
            )
        )
    if data.get("SyncCompliance") is not None:
        import capo_ssm.types.association_sync_compliance

        out["sync_compliance"] = (
            capo_ssm.types.association_sync_compliance.deserialize_aws_json_1_1(
                data["SyncCompliance"]
            )
        )
    if data.get("ApplyOnlyAtCronInterval") is not None:
        out["apply_only_at_cron_interval"] = data["ApplyOnlyAtCronInterval"]
    else:
        out["apply_only_at_cron_interval"] = False
    if data.get("CalendarNames") is not None:
        import capo_ssm.types.calendar_name_or_arn_list

        out["calendar_names"] = (
            capo_ssm.types.calendar_name_or_arn_list.deserialize_aws_json_1_1(
                data["CalendarNames"]
            )
        )
    if data.get("TargetLocations") is not None:
        import capo_ssm.types.target_locations

        out["target_locations"] = (
            capo_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if data.get("ScheduleOffset") is not None:
        out["schedule_offset"] = data["ScheduleOffset"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("TargetMaps") is not None:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if data.get("AssociationDispatchAssumeRole") is not None:
        out["association_dispatch_assume_role"] = data["AssociationDispatchAssumeRole"]
    return out
