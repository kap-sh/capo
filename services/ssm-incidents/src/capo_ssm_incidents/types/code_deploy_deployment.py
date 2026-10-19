"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CodeDeployDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn


class CodeDeployDeployment(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The timestamp for when the CodeDeploy deployment began.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the CodeDeploy deployment ended. Not reported for deployments that are still in progress.</p>"""
    deployment_group_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CodeDeploy deployment group associated with the deployment.</p>"""
    deployment_id: "str"
    """<p>The ID of the CodeDeploy deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeDeployDeployment) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types._prelude.timestamp

    out["startTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        out["endTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["deploymentGroupArn"] = value["deployment_group_arn"]
    out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> CodeDeployDeployment:
    out: CodeDeployDeployment = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["start_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["end_time"] = capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("deploymentGroupArn") is not None:
        out["deployment_group_arn"] = data["deploymentGroupArn"]
    else:
        out["deployment_group_arn"] = ""
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    return out
