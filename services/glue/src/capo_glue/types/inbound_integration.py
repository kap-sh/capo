"""Generated from Smithy shape ``com.amazonaws.glue#InboundIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_config
    import capo_glue.types.integration_error_list
    import capo_glue.types.integration_status
    import capo_glue.types.integration_timestamp
    import capo_glue.types.string128
    import capo_glue.types.string512


class InboundIntegration(TypedDict, closed=True):
    source_arn: "capo_glue.types.string512.String512"
    """<p>The ARN of the source resource for the integration.</p>"""
    target_arn: "capo_glue.types.string512.String512"
    """<p>The ARN of the target resource for the integration.</p>"""
    integration_arn: "capo_glue.types.string128.String128"
    """<p>The ARN of the zero-ETL integration.</p>"""
    status: "capo_glue.types.integration_status.IntegrationStatus"
    """<p>The possible statuses are:</p> <ul> <li> <p>CREATING: The integration is being created.</p> </li> <li> <p>ACTIVE: The integration creation succeeds.</p> </li> <li> <p>MODIFYING: The integration is being modified.</p> </li> <li> <p>FAILED: The integration creation fails. </p> </li> <li> <p>DELETING: The integration is deleted.</p> </li> <li> <p>SYNCING: The integration is synchronizing.</p> </li> <li> <p>NEEDS_ATTENTION: The integration needs attention, such as synchronization.</p> </li> </ul>"""
    create_time: "capo_glue.types.integration_timestamp.IntegrationTimestamp"
    """<p>The time that the integration was created, in UTC.</p>"""
    integration_config: NotRequired[
        "capo_glue.types.integration_config.IntegrationConfig"
    ]
    """<p>Properties associated with the integration.</p>"""
    errors: NotRequired["capo_glue.types.integration_error_list.IntegrationErrorList"]
    """<p>A list of errors associated with the integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InboundIntegration) -> dict:
    out: dict = {}
    out["SourceArn"] = value["source_arn"]
    out["TargetArn"] = value["target_arn"]
    out["IntegrationArn"] = value["integration_arn"]
    import capo_glue.types.integration_status

    out["Status"] = capo_glue.types.integration_status.serialize_aws_json_1_1(
        value["status"]
    )
    import capo_glue.types.integration_timestamp

    out["CreateTime"] = capo_glue.types.integration_timestamp.serialize_aws_json_1_1(
        value["create_time"]
    )
    if "integration_config" in value:
        import capo_glue.types.integration_config

        out["IntegrationConfig"] = (
            capo_glue.types.integration_config.serialize_aws_json_1_1(
                value["integration_config"]
            )
        )
    if "errors" in value:
        import capo_glue.types.integration_error_list

        out["Errors"] = capo_glue.types.integration_error_list.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InboundIntegration:
    out: InboundIntegration = {}  # type: ignore[typeddict-item]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    if data.get("IntegrationArn") is not None:
        out["integration_arn"] = data["IntegrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("Status") is not None:
        import capo_glue.types.integration_status

        out["status"] = capo_glue.types.integration_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_glue.types.integration_status.IntegrationStatus", ""
        )
    if data.get("CreateTime") is not None:
        import capo_glue.types.integration_timestamp

        out["create_time"] = (
            capo_glue.types.integration_timestamp.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("IntegrationConfig") is not None:
        import capo_glue.types.integration_config

        out["integration_config"] = (
            capo_glue.types.integration_config.deserialize_aws_json_1_1(
                data["IntegrationConfig"]
            )
        )
    if data.get("Errors") is not None:
        import capo_glue.types.integration_error_list

        out["errors"] = capo_glue.types.integration_error_list.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
