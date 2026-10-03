"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateConstraintInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.constraint_description
    import capo_service_catalog.types.constraint_parameters
    import capo_service_catalog.types.id


class UpdateConstraintInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the constraint.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.constraint_description.ConstraintDescription"
    ]
    """<p>The updated description of the constraint.</p>"""
    parameters: NotRequired[
        "capo_service_catalog.types.constraint_parameters.ConstraintParameters"
    ]
    """<p>The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:</p> <dl> <dt>LAUNCH</dt> <dd> <p>You are required to specify either the <code>RoleArn</code> or the <code>LocalRoleName</code> but can't use both.</p> <p>Specify the <code>RoleArn</code> property as follows:</p> <p> <code>{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}</code> </p> <p>Specify the <code>LocalRoleName</code> property as follows:</p> <p> <code>{"LocalRoleName": "SCBasicLaunchRole"}</code> </p> <p>If you specify the <code>LocalRoleName</code> property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.</p> <note> <p>The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.</p> </note> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>LAUNCH</code> constraint on a product and portfolio.</p> </dd> <dt>NOTIFICATION</dt> <dd> <p>Specify the <code>NotificationArns</code> property as follows:</p> <p> <code>{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}</code> </p> </dd> <dt>RESOURCE_UPDATE</dt> <dd> <p>Specify the <code>TagUpdatesOnProvisionedProduct</code> property as follows:</p> <p> <code>{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}</code> </p> <p>The <code>TagUpdatesOnProvisionedProduct</code> property accepts a string value of <code>ALLOWED</code> or <code>NOT_ALLOWED</code>.</p> </dd> <dt>STACKSET</dt> <dd> <p>Specify the <code>Parameters</code> property as follows:</p> <p> <code>{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}</code> </p> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>STACKSET</code> constraint on a product and portfolio.</p> <p>Products with a <code>STACKSET</code> constraint will launch an CloudFormation stack set.</p> </dd> <dt>TEMPLATE</dt> <dd> <p>Specify the <code>Rules</code> property. For more information, see <a href="http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html">Template Constraint Rules</a>.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConstraintInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConstraintInput:
    out: UpdateConstraintInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateConstraintInput.id required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        out["parameters"] = data["Parameters"]
    return out
