"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.attempt
    import capo_databrew.types.data_catalog_output_list
    import capo_databrew.types.database_output_list
    import capo_databrew.types.dataset_name
    import capo_databrew.types.date
    import capo_databrew.types.execution_time
    import capo_databrew.types.job_name
    import capo_databrew.types.job_run_error_message
    import capo_databrew.types.job_run_id
    import capo_databrew.types.job_run_state
    import capo_databrew.types.job_sample
    import capo_databrew.types.log_group_name
    import capo_databrew.types.log_subscription
    import capo_databrew.types.output_list
    import capo_databrew.types.profile_configuration
    import capo_databrew.types.recipe_reference
    import capo_databrew.types.started_by
    import capo_databrew.types.validation_configuration_list


class DescribeJobRunResponse(TypedDict, closed=True):
    attempt: "capo_databrew.types.attempt.Attempt"
    """<p>The number of times that DataBrew has attempted to run the job.</p>"""
    completed_on: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time when the job completed processing.</p>"""
    dataset_name: NotRequired["capo_databrew.types.dataset_name.DatasetName"]
    """<p>The name of the dataset for the job to process.</p>"""
    error_message: NotRequired[
        "capo_databrew.types.job_run_error_message.JobRunErrorMessage"
    ]
    """<p>A message indicating an error (if any) that was encountered when the job ran.</p>"""
    execution_time: "capo_databrew.types.execution_time.ExecutionTime"
    """<p>The amount of time, in seconds, during which the job run consumed resources.</p>"""
    job_name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job being processed during this run.</p>"""
    profile_configuration: NotRequired[
        "capo_databrew.types.profile_configuration.ProfileConfiguration"
    ]
    """<p>Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.</p>"""
    validation_configurations: NotRequired[
        "capo_databrew.types.validation_configuration_list.ValidationConfigurationList"
    ]
    """<p>List of validation configurations that are applied to the profile job.</p>"""
    run_id: NotRequired["capo_databrew.types.job_run_id.JobRunId"]
    """<p>The unique identifier of the job run.</p>"""
    state: NotRequired["capo_databrew.types.job_run_state.JobRunState"]
    """<p>The current state of the job run entity itself.</p>"""
    log_subscription: NotRequired[
        "capo_databrew.types.log_subscription.LogSubscription"
    ]
    """<p>The current status of Amazon CloudWatch logging for the job run.</p>"""
    log_group_name: NotRequired["capo_databrew.types.log_group_name.LogGroupName"]
    """<p>The name of an Amazon CloudWatch log group, where the job writes diagnostic messages when it runs.</p>"""
    outputs: NotRequired["capo_databrew.types.output_list.OutputList"]
    """<p>One or more output artifacts from a job run.</p>"""
    data_catalog_outputs: NotRequired[
        "capo_databrew.types.data_catalog_output_list.DataCatalogOutputList"
    ]
    """<p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>"""
    database_outputs: NotRequired[
        "capo_databrew.types.database_output_list.DatabaseOutputList"
    ]
    """<p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.</p>"""
    recipe_reference: NotRequired[
        "capo_databrew.types.recipe_reference.RecipeReference"
    ]
    started_by: NotRequired["capo_databrew.types.started_by.StartedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who started the job run.</p>"""
    started_on: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time when the job run began.</p>"""
    job_sample: NotRequired["capo_databrew.types.job_sample.JobSample"]
    """<p>Sample configuration for profile jobs only. Determines the number of rows on which the profile job will be executed. If a JobSample value is not provided, the default value will be used. The default value is CUSTOM_ROWS for the mode parameter and 20000 for the size parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRunResponse) -> dict:
    out: dict = {}
    out["Attempt"] = value.get("attempt", 0)
    if "completed_on" in value:
        import capo_databrew.types.date

        out["CompletedOn"] = capo_databrew.types.date.serialize_json(
            value["completed_on"]
        )
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    out["ExecutionTime"] = value.get("execution_time", 0)
    out["JobName"] = value["job_name"]
    if "profile_configuration" in value:
        import capo_databrew.types.profile_configuration

        out["ProfileConfiguration"] = (
            capo_databrew.types.profile_configuration.serialize_json(
                value["profile_configuration"]
            )
        )
    if "validation_configurations" in value:
        import capo_databrew.types.validation_configuration_list

        out["ValidationConfigurations"] = (
            capo_databrew.types.validation_configuration_list.serialize_json(
                value["validation_configurations"]
            )
        )
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "state" in value:
        import capo_databrew.types.job_run_state

        out["State"] = capo_databrew.types.job_run_state.serialize_json(value["state"])
    if "log_subscription" in value:
        import capo_databrew.types.log_subscription

        out["LogSubscription"] = capo_databrew.types.log_subscription.serialize_json(
            value["log_subscription"]
        )
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "outputs" in value:
        import capo_databrew.types.output_list

        out["Outputs"] = capo_databrew.types.output_list.serialize_json(
            value["outputs"]
        )
    if "data_catalog_outputs" in value:
        import capo_databrew.types.data_catalog_output_list

        out["DataCatalogOutputs"] = (
            capo_databrew.types.data_catalog_output_list.serialize_json(
                value["data_catalog_outputs"]
            )
        )
    if "database_outputs" in value:
        import capo_databrew.types.database_output_list

        out["DatabaseOutputs"] = (
            capo_databrew.types.database_output_list.serialize_json(
                value["database_outputs"]
            )
        )
    if "recipe_reference" in value:
        import capo_databrew.types.recipe_reference

        out["RecipeReference"] = capo_databrew.types.recipe_reference.serialize_json(
            value["recipe_reference"]
        )
    if "started_by" in value:
        out["StartedBy"] = value["started_by"]
    if "started_on" in value:
        import capo_databrew.types.date

        out["StartedOn"] = capo_databrew.types.date.serialize_json(value["started_on"])
    if "job_sample" in value:
        import capo_databrew.types.job_sample

        out["JobSample"] = capo_databrew.types.job_sample.serialize_json(
            value["job_sample"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobRunResponse:
    out: DescribeJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("Attempt") is not None:
        out["attempt"] = data["Attempt"]
    else:
        out["attempt"] = 0
    if data.get("CompletedOn") is not None:
        import capo_databrew.types.date

        out["completed_on"] = capo_databrew.types.date.deserialize_json(
            data["CompletedOn"]
        )
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ExecutionTime") is not None:
        out["execution_time"] = data["ExecutionTime"]
    else:
        out["execution_time"] = 0
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("ProfileConfiguration") is not None:
        import capo_databrew.types.profile_configuration

        out["profile_configuration"] = (
            capo_databrew.types.profile_configuration.deserialize_json(
                data["ProfileConfiguration"]
            )
        )
    if data.get("ValidationConfigurations") is not None:
        import capo_databrew.types.validation_configuration_list

        out["validation_configurations"] = (
            capo_databrew.types.validation_configuration_list.deserialize_json(
                data["ValidationConfigurations"]
            )
        )
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    if data.get("State") is not None:
        import capo_databrew.types.job_run_state

        out["state"] = capo_databrew.types.job_run_state.deserialize_json(data["State"])
    if data.get("LogSubscription") is not None:
        import capo_databrew.types.log_subscription

        out["log_subscription"] = capo_databrew.types.log_subscription.deserialize_json(
            data["LogSubscription"]
        )
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    if data.get("Outputs") is not None:
        import capo_databrew.types.output_list

        out["outputs"] = capo_databrew.types.output_list.deserialize_json(
            data["Outputs"]
        )
    if data.get("DataCatalogOutputs") is not None:
        import capo_databrew.types.data_catalog_output_list

        out["data_catalog_outputs"] = (
            capo_databrew.types.data_catalog_output_list.deserialize_json(
                data["DataCatalogOutputs"]
            )
        )
    if data.get("DatabaseOutputs") is not None:
        import capo_databrew.types.database_output_list

        out["database_outputs"] = (
            capo_databrew.types.database_output_list.deserialize_json(
                data["DatabaseOutputs"]
            )
        )
    if data.get("RecipeReference") is not None:
        import capo_databrew.types.recipe_reference

        out["recipe_reference"] = capo_databrew.types.recipe_reference.deserialize_json(
            data["RecipeReference"]
        )
    if data.get("StartedBy") is not None:
        out["started_by"] = data["StartedBy"]
    if data.get("StartedOn") is not None:
        import capo_databrew.types.date

        out["started_on"] = capo_databrew.types.date.deserialize_json(data["StartedOn"])
    if data.get("JobSample") is not None:
        import capo_databrew.types.job_sample

        out["job_sample"] = capo_databrew.types.job_sample.deserialize_json(
            data["JobSample"]
        )
    return out
