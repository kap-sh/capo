"""Generated from Smithy shape ``com.amazonaws.devopsagent#IdcAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class IdcAuthConfiguration(TypedDict, closed=True):
    operator_app_role_arn: "str"
    """<p>The IAM role end users assume to access AIDevOps APIs</p>"""
    idc_instance_arn: "str"
    """<p>The IdC instance Arn used to create an IdC auth application</p>"""
    idc_application_arn: NotRequired["str"]
    """<p>The IdC application Arn created for IdC auth</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Operator App IdC auth flow was enabled.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the Operator App IdC auth flow was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdcAuthConfiguration) -> dict:
    out: dict = {}
    out["operatorAppRoleArn"] = value["operator_app_role_arn"]
    out["idcInstanceArn"] = value["idc_instance_arn"]
    if "idc_application_arn" in value:
        out["idcApplicationArn"] = value["idc_application_arn"]
    import capo_devops_agent._protocol.serialize

    out["createdAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_devops_agent._protocol.serialize

        out["updatedAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> IdcAuthConfiguration:
    out: IdcAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("operatorAppRoleArn") is not None:
        out["operator_app_role_arn"] = data["operatorAppRoleArn"]
    else:
        out["operator_app_role_arn"] = ""
    if data.get("idcInstanceArn") is not None:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    else:
        out["idc_instance_arn"] = ""
    if data.get("idcApplicationArn") is not None:
        out["idc_application_arn"] = data["idcApplicationArn"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
