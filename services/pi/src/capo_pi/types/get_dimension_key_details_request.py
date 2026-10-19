"""Generated from Smithy shape ``com.amazonaws.pi#GetDimensionKeyDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.identifier_string
    import capo_pi.types.request_string
    import capo_pi.types.requested_dimension_list
    import capo_pi.types.service_type


class GetDimensionKeyDetailsRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns data. The only valid value is <code>RDS</code>.</p>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>The ID for a data source from which to gather dimension data. This ID must be immutable and unique within an Amazon Web Services Region. When a DB instance is the data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>. </p>"""
    group: "capo_pi.types.request_string.RequestString"
    """<p>The name of the dimension group. Performance Insights searches the specified group for the dimension group ID. The following group name values are valid:</p> <ul> <li> <p> <code>db.execution_plan</code> (Amazon RDS and Aurora only)</p> </li> <li> <p> <code>db.lock_snapshot</code> (Aurora only)</p> </li> <li> <p> <code>db.query</code> (Amazon DocumentDB only)</p> </li> <li> <p> <code>db.sql</code> (Amazon RDS and Aurora only)</p> </li> </ul>"""
    group_identifier: "capo_pi.types.request_string.RequestString"
    """<p>The ID of the dimension group from which to retrieve dimension details. For dimension group <code>db.sql</code>, the group ID is <code>db.sql.id</code>. The following group ID values are valid:</p> <ul> <li> <p> <code>db.execution_plan.id</code> for dimension group <code>db.execution_plan</code> (Aurora and RDS only)</p> </li> <li> <p> <code>db.sql.id</code> for dimension group <code>db.sql</code> (Aurora and RDS only)</p> </li> <li> <p> <code>db.query.id</code> for dimension group <code>db.query</code> (DocumentDB only)</p> </li> <li> <p>For the dimension group <code>db.lock_snapshot</code>, the <code>GroupIdentifier</code> is the epoch timestamp when Performance Insights captured the snapshot, in seconds. You can retrieve this value with the <code>GetResourceMetrics</code> operation for a 1 second period.</p> </li> </ul>"""
    requested_dimensions: NotRequired[
        "capo_pi.types.requested_dimension_list.RequestedDimensionList"
    ]
    """<p>A list of dimensions to retrieve the detail data for within the given dimension group. If you don't specify this parameter, Performance Insights returns all dimension data within the specified dimension group. Specify dimension names for the following dimension groups:</p> <ul> <li> <p> <code>db.execution_plan</code> - Specify the dimension name <code>db.execution_plan.raw_plan</code> or the short dimension name <code>raw_plan</code> (Amazon RDS and Aurora only)</p> </li> <li> <p> <code>db.lock_snapshot</code> - Specify the dimension name <code>db.lock_snapshot.lock_trees</code> or the short dimension name <code>lock_trees</code>. (Aurora only)</p> </li> <li> <p> <code>db.sql</code> - Specify either the full dimension name <code>db.sql.statement</code> or the short dimension name <code>statement</code> (Aurora and RDS only).</p> </li> <li> <p> <code>db.query</code> - Specify either the full dimension name <code>db.query.statement</code> or the short dimension name <code>statement</code> (DocumentDB only).</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDimensionKeyDetailsRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    out["Group"] = value["group"]
    out["GroupIdentifier"] = value["group_identifier"]
    if "requested_dimensions" in value:
        import capo_pi.types.requested_dimension_list

        out["RequestedDimensions"] = (
            capo_pi.types.requested_dimension_list.serialize_aws_json_1_1(
                value["requested_dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDimensionKeyDetailsRequest:
    out: GetDimensionKeyDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        import typing

        out["service_type"] = typing.cast("capo_pi.types.service_type.ServiceType", "")
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    else:
        out["group"] = ""
    if data.get("GroupIdentifier") is not None:
        out["group_identifier"] = data["GroupIdentifier"]
    else:
        out["group_identifier"] = ""
    if data.get("RequestedDimensions") is not None:
        import capo_pi.types.requested_dimension_list

        out["requested_dimensions"] = (
            capo_pi.types.requested_dimension_list.deserialize_aws_json_1_1(
                data["RequestedDimensions"]
            )
        )
    return out
