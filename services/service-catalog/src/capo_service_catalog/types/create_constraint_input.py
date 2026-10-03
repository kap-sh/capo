"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateConstraintInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.constraint_description
    import capo_service_catalog.types.constraint_parameters
    import capo_service_catalog.types.constraint_type
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token


class CreateConstraintInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    parameters: "capo_service_catalog.types.constraint_parameters.ConstraintParameters"
    """<p>The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:</p> <dl> <dt>LAUNCH</dt> <dd> <p>You are required to specify either the <code>RoleArn</code> or the <code>LocalRoleName</code> but can't use both.</p> <p>Specify the <code>RoleArn</code> property as follows:</p> <p> <code>{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}</code> </p> <p>Specify the <code>LocalRoleName</code> property as follows:</p> <p> <code>{"LocalRoleName": "SCBasicLaunchRole"}</code> </p> <p>If you specify the <code>LocalRoleName</code> property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.</p> <note> <p>The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.</p> </note> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>LAUNCH</code> constraint on a product and portfolio.</p> </dd> <dt>NOTIFICATION</dt> <dd> <p>Specify the <code>NotificationArns</code> property as follows:</p> <p> <code>{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}</code> </p> </dd> <dt>RESOURCE_UPDATE</dt> <dd> <p>Specify the <code>TagUpdatesOnProvisionedProduct</code> property as follows:</p> <p> <code>{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}</code> </p> <p>The <code>TagUpdatesOnProvisionedProduct</code> property accepts a string value of <code>ALLOWED</code> or <code>NOT_ALLOWED</code>.</p> </dd> <dt>STACKSET</dt> <dd> <p>Specify the <code>Parameters</code> property as follows:</p> <p> <code>{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}</code> </p> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>STACKSET</code> constraint on a product and portfolio.</p> <p>Products with a <code>STACKSET</code> constraint will launch an CloudFormation stack set.</p> </dd> <dt>TEMPLATE</dt> <dd> <p>Specify the <code>Rules</code> property. For more information, see <a href="http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html">Template Constraint Rules</a>.</p> </dd> </dl>"""
    type: "capo_service_catalog.types.constraint_type.ConstraintType"
    """<p>The type of constraint.</p> <ul> <li> <p> <code>LAUNCH</code> </p> </li> <li> <p> <code>NOTIFICATION</code> </p> </li> <li> <p> <code>RESOURCE_UPDATE</code> </p> </li> <li> <p> <code>STACKSET</code> </p> </li> <li> <p> <code>TEMPLATE</code> </p> </li> </ul>"""
    description: NotRequired[
        "capo_service_catalog.types.constraint_description.ConstraintDescription"
    ]
    """<p>The description of the constraint.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConstraintInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    out["ProductId"] = value["product_id"]
    out["Parameters"] = value["parameters"]
    out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConstraintInput:
    out: CreateConstraintInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("CreateConstraintInput.portfolio_id required")
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError("CreateConstraintInput.product_id required")
    if data.get("Parameters") is not None:
        out["parameters"] = data["Parameters"]
    else:
        raise DeserializationError("CreateConstraintInput.parameters required")
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("CreateConstraintInput.type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError("CreateConstraintInput.idempotency_token required")
    return out
