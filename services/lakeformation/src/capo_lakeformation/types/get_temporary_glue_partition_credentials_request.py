"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTemporaryGluePartitionCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.audit_context
    import capo_lakeformation.types.credential_timeout_duration_second_integer
    import capo_lakeformation.types.partition_value_list
    import capo_lakeformation.types.permission_list
    import capo_lakeformation.types.permission_type_list
    import capo_lakeformation.types.resource_arn_string


class GetTemporaryGluePartitionCredentialsRequest(TypedDict, closed=True):
    table_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The ARN of the partitions' table.</p>"""
    partition: "capo_lakeformation.types.partition_value_list.PartitionValueList"
    """<p>A list of partition values identifying a single partition.</p>"""
    permissions: NotRequired["capo_lakeformation.types.permission_list.PermissionList"]
    """<p>Filters the request based on the user having been granted a list of specified permissions on the requested resource(s).</p>"""
    duration_seconds: NotRequired[
        "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
    ]
    """<p>The time period, between 900 and 21,600 seconds, for the timeout of the temporary credentials.</p>"""
    audit_context: NotRequired["capo_lakeformation.types.audit_context.AuditContext"]
    """<p>A structure representing context to access a resource (column names, query ID, etc).</p>"""
    supported_permission_types: NotRequired[
        "capo_lakeformation.types.permission_type_list.PermissionTypeList"
    ]
    """<p>A list of supported permission types for the partition. Valid values are <code>COLUMN_PERMISSION</code> and <code>CELL_FILTER_PERMISSION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemporaryGluePartitionCredentialsRequest) -> dict:
    out: dict = {}
    out["TableArn"] = value["table_arn"]
    import capo_lakeformation.types.partition_value_list

    out["Partition"] = capo_lakeformation.types.partition_value_list.serialize_json(
        value["partition"]
    )
    if "permissions" in value:
        import capo_lakeformation.types.permission_list

        out["Permissions"] = capo_lakeformation.types.permission_list.serialize_json(
            value["permissions"]
        )
    if "duration_seconds" in value:
        out["DurationSeconds"] = value["duration_seconds"]
    if "audit_context" in value:
        import capo_lakeformation.types.audit_context

        out["AuditContext"] = capo_lakeformation.types.audit_context.serialize_json(
            value["audit_context"]
        )
    if "supported_permission_types" in value:
        import capo_lakeformation.types.permission_type_list

        out["SupportedPermissionTypes"] = (
            capo_lakeformation.types.permission_type_list.serialize_json(
                value["supported_permission_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemporaryGluePartitionCredentialsRequest:
    out: GetTemporaryGluePartitionCredentialsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TableArn") is not None:
        out["table_arn"] = data["TableArn"]
    else:
        out["table_arn"] = ""
    if data.get("Partition") is not None:
        import capo_lakeformation.types.partition_value_list

        out["partition"] = (
            capo_lakeformation.types.partition_value_list.deserialize_json(
                data["Partition"]
            )
        )
    else:
        raise DeserializationError(
            "GetTemporaryGluePartitionCredentialsRequest.partition required"
        )
    if data.get("Permissions") is not None:
        import capo_lakeformation.types.permission_list

        out["permissions"] = capo_lakeformation.types.permission_list.deserialize_json(
            data["Permissions"]
        )
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = data["DurationSeconds"]
    if data.get("AuditContext") is not None:
        import capo_lakeformation.types.audit_context

        out["audit_context"] = capo_lakeformation.types.audit_context.deserialize_json(
            data["AuditContext"]
        )
    if data.get("SupportedPermissionTypes") is not None:
        import capo_lakeformation.types.permission_type_list

        out["supported_permission_types"] = (
            capo_lakeformation.types.permission_type_list.deserialize_json(
                data["SupportedPermissionTypes"]
            )
        )
    return out
