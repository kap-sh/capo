"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.client_token
    import capo_fis.types.create_experiment_template_action_input_map
    import capo_fis.types.create_experiment_template_experiment_options_input
    import capo_fis.types.create_experiment_template_log_configuration_input
    import capo_fis.types.create_experiment_template_report_configuration_input
    import capo_fis.types.create_experiment_template_stop_condition_input_list
    import capo_fis.types.create_experiment_template_target_input_map
    import capo_fis.types.experiment_template_description
    import capo_fis.types.role_arn
    import capo_fis.types.tag_map


class CreateExperimentTemplateRequest(TypedDict, closed=True):
    client_token: "capo_fis.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    description: (
        "capo_fis.types.experiment_template_description.ExperimentTemplateDescription"
    )
    """<p>A description for the experiment template.</p>"""
    stop_conditions: "capo_fis.types.create_experiment_template_stop_condition_input_list.CreateExperimentTemplateStopConditionInputList"
    """<p>The stop conditions.</p>"""
    targets: NotRequired[
        "capo_fis.types.create_experiment_template_target_input_map.CreateExperimentTemplateTargetInputMap"
    ]
    """<p>The targets for the experiment.</p>"""
    actions: "capo_fis.types.create_experiment_template_action_input_map.CreateExperimentTemplateActionInputMap"
    """<p>The actions for the experiment.</p>"""
    role_arn: "capo_fis.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.</p>"""
    tags: NotRequired["capo_fis.types.tag_map.TagMap"]
    """<p>The tags to apply to the experiment template.</p>"""
    log_configuration: NotRequired[
        "capo_fis.types.create_experiment_template_log_configuration_input.CreateExperimentTemplateLogConfigurationInput"
    ]
    """<p>The configuration for experiment logging.</p>"""
    experiment_options: NotRequired[
        "capo_fis.types.create_experiment_template_experiment_options_input.CreateExperimentTemplateExperimentOptionsInput"
    ]
    """<p>The experiment options for the experiment template.</p>"""
    experiment_report_configuration: NotRequired[
        "capo_fis.types.create_experiment_template_report_configuration_input.CreateExperimentTemplateReportConfigurationInput"
    ]
    """<p>The experiment report configuration for the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["description"] = value["description"]
    import capo_fis.types.create_experiment_template_stop_condition_input_list

    out["stopConditions"] = (
        capo_fis.types.create_experiment_template_stop_condition_input_list.serialize_json(
            value["stop_conditions"]
        )
    )
    if "targets" in value:
        import capo_fis.types.create_experiment_template_target_input_map

        out["targets"] = (
            capo_fis.types.create_experiment_template_target_input_map.serialize_json(
                value["targets"]
            )
        )
    import capo_fis.types.create_experiment_template_action_input_map

    out["actions"] = (
        capo_fis.types.create_experiment_template_action_input_map.serialize_json(
            value["actions"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.serialize_json(value["tags"])
    if "log_configuration" in value:
        import capo_fis.types.create_experiment_template_log_configuration_input

        out["logConfiguration"] = (
            capo_fis.types.create_experiment_template_log_configuration_input.serialize_json(
                value["log_configuration"]
            )
        )
    if "experiment_options" in value:
        import capo_fis.types.create_experiment_template_experiment_options_input

        out["experimentOptions"] = (
            capo_fis.types.create_experiment_template_experiment_options_input.serialize_json(
                value["experiment_options"]
            )
        )
    if "experiment_report_configuration" in value:
        import capo_fis.types.create_experiment_template_report_configuration_input

        out["experimentReportConfiguration"] = (
            capo_fis.types.create_experiment_template_report_configuration_input.serialize_json(
                value["experiment_report_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateRequest:
    out: CreateExperimentTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("stopConditions") is not None:
        import capo_fis.types.create_experiment_template_stop_condition_input_list

        out["stop_conditions"] = (
            capo_fis.types.create_experiment_template_stop_condition_input_list.deserialize_json(
                data["stopConditions"]
            )
        )
    else:
        out["stop_conditions"] = []
    if data.get("targets") is not None:
        import capo_fis.types.create_experiment_template_target_input_map

        out["targets"] = (
            capo_fis.types.create_experiment_template_target_input_map.deserialize_json(
                data["targets"]
            )
        )
    if data.get("actions") is not None:
        import capo_fis.types.create_experiment_template_action_input_map

        out["actions"] = (
            capo_fis.types.create_experiment_template_action_input_map.deserialize_json(
                data["actions"]
            )
        )
    else:
        out["actions"] = {}
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("tags") is not None:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.deserialize_json(data["tags"])
    if data.get("logConfiguration") is not None:
        import capo_fis.types.create_experiment_template_log_configuration_input

        out["log_configuration"] = (
            capo_fis.types.create_experiment_template_log_configuration_input.deserialize_json(
                data["logConfiguration"]
            )
        )
    if data.get("experimentOptions") is not None:
        import capo_fis.types.create_experiment_template_experiment_options_input

        out["experiment_options"] = (
            capo_fis.types.create_experiment_template_experiment_options_input.deserialize_json(
                data["experimentOptions"]
            )
        )
    if data.get("experimentReportConfiguration") is not None:
        import capo_fis.types.create_experiment_template_report_configuration_input

        out["experiment_report_configuration"] = (
            capo_fis.types.create_experiment_template_report_configuration_input.deserialize_json(
                data["experimentReportConfiguration"]
            )
        )
    return out
