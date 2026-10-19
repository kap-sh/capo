"""Generated from Smithy shape ``com.amazonaws.odb#AssociateIamRoleToResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.arn
    import capo_odb.types.role_arn
    import capo_odb.types.supported_aws_integration


class AssociateIamRoleToResourceInput(TypedDict, closed=True):
    iam_role_arn: "capo_odb.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role to associate with the resource.</p>"""
    aws_integration: "capo_odb.types.supported_aws_integration.SupportedAwsIntegration"
    """<p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role association.</p>"""
    resource_arn: "capo_odb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the target resource to associate with the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateIamRoleToResourceInput) -> dict:
    out: dict = {}
    out["iamRoleArn"] = value["iam_role_arn"]
    import capo_odb.types.supported_aws_integration

    out["awsIntegration"] = (
        capo_odb.types.supported_aws_integration.serialize_aws_json_1_0(
            value["aws_integration"]
        )
    )
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateIamRoleToResourceInput:
    out: AssociateIamRoleToResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("iamRoleArn") is not None:
        out["iam_role_arn"] = data["iamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("awsIntegration") is not None:
        import capo_odb.types.supported_aws_integration

        out["aws_integration"] = (
            capo_odb.types.supported_aws_integration.deserialize_aws_json_1_0(
                data["awsIntegration"]
            )
        )
    else:
        import typing

        out["aws_integration"] = typing.cast(
            "capo_odb.types.supported_aws_integration.SupportedAwsIntegration", ""
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
