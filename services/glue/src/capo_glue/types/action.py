"""Generated from Smithy shape ``com.amazonaws.glue#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_map
    import capo_glue.types.name_string
    import capo_glue.types.notification_property
    import capo_glue.types.timeout


class Action(TypedDict, closed=True):
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of a job to be run.</p>"""
    arguments: NotRequired["capo_glue.types.generic_map.GenericMap"]
    """<p>The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.</p> <p>You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.</p> <p>For information about how to specify and consume your own Job arguments, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling Glue APIs in Python</a> topic in the developer guide.</p> <p>For information about the key-value pairs that Glue consumes to set up your job, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html">Special Parameters Used by Glue</a> topic in the developer guide.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The <code>JobRun</code> timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. This overrides the timeout value set in the parent job.</p> <p>Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.</p> <p>When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.</p> <p>Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.</p> <p>For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.</p>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used with this action.</p>"""
    notification_property: NotRequired[
        "capo_glue.types.notification_property.NotificationProperty"
    ]
    """<p>Specifies configuration properties of a job run notification.</p>"""
    crawler_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the crawler to be used with this action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Action) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "arguments" in value:
        import capo_glue.types.generic_map

        out["Arguments"] = capo_glue.types.generic_map.serialize_aws_json_1_1(
            value["arguments"]
        )
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "notification_property" in value:
        import capo_glue.types.notification_property

        out["NotificationProperty"] = (
            capo_glue.types.notification_property.serialize_aws_json_1_1(
                value["notification_property"]
            )
        )
    if "crawler_name" in value:
        out["CrawlerName"] = value["crawler_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("Arguments") is not None:
        import capo_glue.types.generic_map

        out["arguments"] = capo_glue.types.generic_map.deserialize_aws_json_1_1(
            data["Arguments"]
        )
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("NotificationProperty") is not None:
        import capo_glue.types.notification_property

        out["notification_property"] = (
            capo_glue.types.notification_property.deserialize_aws_json_1_1(
                data["NotificationProperty"]
            )
        )
    if data.get("CrawlerName") is not None:
        out["crawler_name"] = data["CrawlerName"]
    return out
