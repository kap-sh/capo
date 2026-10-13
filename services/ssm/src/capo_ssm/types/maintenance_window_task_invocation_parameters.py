"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskInvocationParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_automation_parameters
    import capo_ssm.types.maintenance_window_lambda_parameters
    import capo_ssm.types.maintenance_window_run_command_parameters
    import capo_ssm.types.maintenance_window_step_functions_parameters

MaintenanceWindowTaskInvocationParameters = TypedDict(
    "MaintenanceWindowTaskInvocationParameters",
    {
        "run_command": NotRequired[
            "capo_ssm.types.maintenance_window_run_command_parameters.MaintenanceWindowRunCommandParameters"
        ],
        "automation": NotRequired[
            "capo_ssm.types.maintenance_window_automation_parameters.MaintenanceWindowAutomationParameters"
        ],
        "step_functions": NotRequired[
            "capo_ssm.types.maintenance_window_step_functions_parameters.MaintenanceWindowStepFunctionsParameters"
        ],
        "lambda": NotRequired[
            "capo_ssm.types.maintenance_window_lambda_parameters.MaintenanceWindowLambdaParameters"
        ],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskInvocationParameters) -> dict:
    out: dict = {}
    if "run_command" in value:
        import capo_ssm.types.maintenance_window_run_command_parameters

        out["RunCommand"] = (
            capo_ssm.types.maintenance_window_run_command_parameters.serialize_aws_json_1_1(
                value["run_command"]
            )
        )
    if "automation" in value:
        import capo_ssm.types.maintenance_window_automation_parameters

        out["Automation"] = (
            capo_ssm.types.maintenance_window_automation_parameters.serialize_aws_json_1_1(
                value["automation"]
            )
        )
    if "step_functions" in value:
        import capo_ssm.types.maintenance_window_step_functions_parameters

        out["StepFunctions"] = (
            capo_ssm.types.maintenance_window_step_functions_parameters.serialize_aws_json_1_1(
                value["step_functions"]
            )
        )
    if "lambda" in value:
        import capo_ssm.types.maintenance_window_lambda_parameters

        out["Lambda"] = (
            capo_ssm.types.maintenance_window_lambda_parameters.serialize_aws_json_1_1(
                value["lambda"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowTaskInvocationParameters:
    out: MaintenanceWindowTaskInvocationParameters = {}  # type: ignore[typeddict-item]
    if data.get("RunCommand") is not None:
        import capo_ssm.types.maintenance_window_run_command_parameters

        out["run_command"] = (
            capo_ssm.types.maintenance_window_run_command_parameters.deserialize_aws_json_1_1(
                data["RunCommand"]
            )
        )
    if data.get("Automation") is not None:
        import capo_ssm.types.maintenance_window_automation_parameters

        out["automation"] = (
            capo_ssm.types.maintenance_window_automation_parameters.deserialize_aws_json_1_1(
                data["Automation"]
            )
        )
    if data.get("StepFunctions") is not None:
        import capo_ssm.types.maintenance_window_step_functions_parameters

        out["step_functions"] = (
            capo_ssm.types.maintenance_window_step_functions_parameters.deserialize_aws_json_1_1(
                data["StepFunctions"]
            )
        )
    if data.get("Lambda") is not None:
        import capo_ssm.types.maintenance_window_lambda_parameters

        out["lambda"] = (
            capo_ssm.types.maintenance_window_lambda_parameters.deserialize_aws_json_1_1(
                data["Lambda"]
            )
        )
    return out


def redact_sensitive(
    value: MaintenanceWindowTaskInvocationParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "run_command" in value:
        import capo_ssm.types.maintenance_window_run_command_parameters

        out["run_command"] = (
            capo_ssm.types.maintenance_window_run_command_parameters.redact_sensitive(
                value["run_command"]
            )
        )
    if "step_functions" in value:
        import capo_ssm.types.maintenance_window_step_functions_parameters

        out["step_functions"] = (
            capo_ssm.types.maintenance_window_step_functions_parameters.redact_sensitive(
                value["step_functions"]
            )
        )
    if "lambda" in value:
        import capo_ssm.types.maintenance_window_lambda_parameters

        out["lambda"] = (
            capo_ssm.types.maintenance_window_lambda_parameters.redact_sensitive(
                value["lambda"]
            )
        )
    return out
