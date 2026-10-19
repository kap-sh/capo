"""Generated from Smithy shape ``com.amazonaws.ssm#Runbook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.target_locations
    import capo_ssm.types.target_maps
    import capo_ssm.types.targets


class Runbook(TypedDict, closed=True):
    document_name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the Automation runbook used in a runbook workflow.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the Automation runbook used in a runbook workflow.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The key-value map of execution parameters, which were supplied when calling <code>StartChangeRequestExecution</code>.</p>"""
    target_parameter_name: NotRequired[
        "capo_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The name of the parameter used as the target resource for the rate-controlled runbook workflow. Required if you specify <code>Targets</code>. </p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>A key-value mapping to target resources that the runbook operation performs tasks on. Required if you specify <code>TargetParameterName</code>.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of runbook parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The <code>MaxConcurrency</code> value specified by the user when the operation started, indicating the maximum number of resources that the runbook operation can run on at the same time.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The <code>MaxErrors</code> value specified by the user when the execution started, indicating the maximum number of errors that can occur during the operation before the updates are stopped or rolled back.</p>"""
    target_locations: NotRequired["capo_ssm.types.target_locations.TargetLocations"]
    """<p>Information about the Amazon Web Services Regions and Amazon Web Services accounts targeted by the current Runbook operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Runbook) -> dict:
    out: dict = {}
    out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "parameters" in value:
        import capo_ssm.types.automation_parameter_map

        out["Parameters"] = (
            capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "target_locations" in value:
        import capo_ssm.types.target_locations

        out["TargetLocations"] = capo_ssm.types.target_locations.serialize_aws_json_1_1(
            value["target_locations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Runbook:
    out: Runbook = {}  # type: ignore[typeddict-item]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    else:
        out["document_name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.automation_parameter_map

        out["parameters"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("TargetParameterName") is not None:
        out["target_parameter_name"] = data["TargetParameterName"]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TargetMaps") is not None:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("TargetLocations") is not None:
        import capo_ssm.types.target_locations

        out["target_locations"] = (
            capo_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    return out
