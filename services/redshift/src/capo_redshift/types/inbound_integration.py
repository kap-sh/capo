"""Generated from Smithy shape ``com.amazonaws.redshift#InboundIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.inbound_integration_arn
    import capo_redshift.types.integration_error_list
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.target_arn
    import capo_redshift.types.zero_etl_integration_status


class InboundIntegration(TypedDict, closed=True):
    integration_arn: NotRequired[
        "capo_redshift.types.inbound_integration_arn.InboundIntegrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an inbound integration.</p>"""
    source_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the source of an inbound integration.</p>"""
    target_arn: NotRequired["capo_redshift.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Name (ARN) of the target of an inbound integration.</p>"""
    status: NotRequired[
        "capo_redshift.types.zero_etl_integration_status.ZeroETLIntegrationStatus"
    ]
    """<p>The status of an inbound integration.</p>"""
    errors: NotRequired[
        "capo_redshift.types.integration_error_list.IntegrationErrorList"
    ]
    """<p>The outstanding errors of an inbound integration. Each item is an "IntegrationError". This is null if there is no error.</p>"""
    create_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The creation time of an inbound integration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InboundIntegration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "integration_arn" in value:
        pairs.append((f"{key_prefix}IntegrationArn", str(value["integration_arn"])))
    if "source_arn" in value:
        pairs.append((f"{key_prefix}SourceArn", str(value["source_arn"])))
    if "target_arn" in value:
        pairs.append((f"{key_prefix}TargetArn", str(value["target_arn"])))
    if "status" in value:
        import capo_redshift.types.zero_etl_integration_status

        capo_redshift.types.zero_etl_integration_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "errors" in value:
        import capo_redshift.types.integration_error_list

        capo_redshift.types.integration_error_list.serialize_query(
            value["errors"], pairs, f"{key_prefix}Errors"
        )
    if "create_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )


def deserialize_query(el: Element) -> InboundIntegration:
    out: InboundIntegration = {}  # type: ignore[typeddict-item]
    child_integration_arn = el.find("IntegrationArn")
    if child_integration_arn is not None:
        out["integration_arn"] = str(child_integration_arn.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_target_arn = el.find("TargetArn")
    if child_target_arn is not None:
        out["target_arn"] = str(child_target_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.zero_etl_integration_status

        out["status"] = (
            capo_redshift.types.zero_etl_integration_status.deserialize_query(
                child_status
            )
        )
    child_errors = el.find("Errors")
    if child_errors is not None:
        import capo_redshift.types.integration_error_list

        out["errors"] = capo_redshift.types.integration_error_list.deserialize_query(
            child_errors
        )
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import capo_redshift.types.t_stamp

        out["create_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_create_time
        )
    return out
