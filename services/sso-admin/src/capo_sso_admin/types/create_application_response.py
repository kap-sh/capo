"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.identity_store_arn
    import capo_sso_admin.types.instance_arn


class CreateApplicationResponse(TypedDict, closed=True):
    application_arn: NotRequired["capo_sso_admin.types.application_arn.ApplicationArn"]
    """<p>Specifies the ARN of the application.</p>"""
    instance_arn: NotRequired["capo_sso_admin.types.instance_arn.InstanceArn"]
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    identity_store_arn: NotRequired[
        "capo_sso_admin.types.identity_store_arn.IdentityStoreArn"
    ]
    """<p>The ARN of the identity store that is connected to the instance of IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "identity_store_arn" in value:
        out["IdentityStoreArn"] = value["identity_store_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("IdentityStoreArn") is not None:
        out["identity_store_arn"] = data["IdentityStoreArn"]
    return out
