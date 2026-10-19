"""Generated from Smithy shape ``com.amazonaws.workmail#CreateIdentityCenterApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.identity_center_application_name
    import capo_workmail.types.instance_arn


class CreateIdentityCenterApplicationRequest(TypedDict, closed=True):
    name: "capo_workmail.types.identity_center_application_name.IdentityCenterApplicationName"
    """<p> The name of the IAM Identity Center application. </p>"""
    instance_arn: "capo_workmail.types.instance_arn.InstanceArn"
    """<p> The Amazon Resource Name (ARN) of the instance. </p>"""
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p> The idempotency token associated with the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIdentityCenterApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["InstanceArn"] = value["instance_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIdentityCenterApplicationRequest:
    out: CreateIdentityCenterApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
