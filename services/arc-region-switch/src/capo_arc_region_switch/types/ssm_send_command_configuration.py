"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmSendCommandConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region_ssm_document_map
    import capo_arc_region_switch.types.ssm_send_command_ungraceful


class SsmSendCommandConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    region_documents: (
        "capo_arc_region_switch.types.region_ssm_document_map.RegionSsmDocumentMap"
    )
    """<p>The Systems Manager document and target configuration for each Amazon Web Services Region in the plan. Provide an entry for each Amazon Web Services Region that you want the command to run in.</p>"""
    retry_interval_minutes: "float"
    """<p>How often, in minutes, Region switch retries the command if it returns a failure.</p>"""
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.ssm_send_command_ungraceful.SsmSendCommandUngraceful"
    ]
    """<p>Specifies the settings that determine how the execution block behaves when the plan runs ungracefully, such as whether to skip the command.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmSendCommandConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import capo_arc_region_switch.types.region_ssm_document_map

    out["regionDocuments"] = (
        capo_arc_region_switch.types.region_ssm_document_map.serialize_aws_json_1_0(
            value["region_documents"]
        )
    )
    out["retryIntervalMinutes"] = (
        "NaN"
        if value["retry_interval_minutes"] != value["retry_interval_minutes"]
        else "Infinity"
        if value["retry_interval_minutes"] == float("inf")
        else "-Infinity"
        if value["retry_interval_minutes"] == float("-inf")
        else value["retry_interval_minutes"]
    )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.ssm_send_command_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.ssm_send_command_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SsmSendCommandConfiguration:
    out: SsmSendCommandConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("regionDocuments") is not None:
        import capo_arc_region_switch.types.region_ssm_document_map

        out["region_documents"] = (
            capo_arc_region_switch.types.region_ssm_document_map.deserialize_aws_json_1_0(
                data["regionDocuments"]
            )
        )
    else:
        out["region_documents"] = {}
    if data.get("retryIntervalMinutes") is not None:
        out["retry_interval_minutes"] = float(data["retryIntervalMinutes"])
    else:
        out["retry_interval_minutes"] = 0.0
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.ssm_send_command_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.ssm_send_command_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out
