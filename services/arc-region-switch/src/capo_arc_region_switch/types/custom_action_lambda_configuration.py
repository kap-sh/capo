"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CustomActionLambdaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.lambda_list
    import capo_arc_region_switch.types.lambda_ungraceful
    import capo_arc_region_switch.types.region_to_run_in


class CustomActionLambdaConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    lambdas: "capo_arc_region_switch.types.lambda_list.LambdaList"
    """<p>The Amazon Web Services Lambda functions for the execution block.</p>"""
    retry_interval_minutes: "float"
    """<p>The retry interval specified.</p>"""
    region_to_run: "capo_arc_region_switch.types.region_to_run_in.RegionToRunIn"
    """<p>The Amazon Web Services Region for the function to run in. For recovery workflows use <code>activatingRegion</code> or <code>deactivatingRegion</code>. For post-recovery workflows, use <code>activeRegion</code> (the Region with customer traffic) or <code>inactiveRegion</code> (the Region with no customer traffic).</p>"""
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.lambda_ungraceful.LambdaUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomActionLambdaConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import capo_arc_region_switch.types.lambda_list

    out["lambdas"] = capo_arc_region_switch.types.lambda_list.serialize_aws_json_1_0(
        value["lambdas"]
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
    import capo_arc_region_switch.types.region_to_run_in

    out["regionToRun"] = (
        capo_arc_region_switch.types.region_to_run_in.serialize_aws_json_1_0(
            value["region_to_run"]
        )
    )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.lambda_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.lambda_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomActionLambdaConfiguration:
    out: CustomActionLambdaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("lambdas") is not None:
        import capo_arc_region_switch.types.lambda_list

        out["lambdas"] = (
            capo_arc_region_switch.types.lambda_list.deserialize_aws_json_1_0(
                data["lambdas"]
            )
        )
    else:
        raise DeserializationError("CustomActionLambdaConfiguration.lambdas required")
    if data.get("retryIntervalMinutes") is not None:
        out["retry_interval_minutes"] = float(data["retryIntervalMinutes"])
    else:
        raise DeserializationError(
            "CustomActionLambdaConfiguration.retry_interval_minutes required"
        )
    if data.get("regionToRun") is not None:
        import capo_arc_region_switch.types.region_to_run_in

        out["region_to_run"] = (
            capo_arc_region_switch.types.region_to_run_in.deserialize_aws_json_1_0(
                data["regionToRun"]
            )
        )
    else:
        raise DeserializationError(
            "CustomActionLambdaConfiguration.region_to_run required"
        )
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.lambda_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.lambda_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out
