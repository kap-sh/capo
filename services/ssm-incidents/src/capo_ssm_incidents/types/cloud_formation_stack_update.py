"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CloudFormationStackUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn


class CloudFormationStackUpdate(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The timestamp for when the CloudFormation stack creation or update began.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the CloudFormation stack creation or update ended. Not reported for deployments that are still in progress.</p>"""
    stack_arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CloudFormation stack involved in the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationStackUpdate) -> dict:
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
    out["stackArn"] = value["stack_arn"]
    return out


def deserialize_json(data: dict) -> CloudFormationStackUpdate:
    out: CloudFormationStackUpdate = {}  # type: ignore[typeddict-item]
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
    if data.get("stackArn") is not None:
        out["stack_arn"] = data["stackArn"]
    else:
        out["stack_arn"] = ""
    return out
