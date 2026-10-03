"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CreateResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.client_token
    import capo_cloudcontrol.types.properties
    import capo_cloudcontrol.types.role_arn
    import capo_cloudcontrol.types.type_name
    import capo_cloudcontrol.types.type_version_id


class CreateResourceInput(TypedDict, closed=True):
    type_name: "capo_cloudcontrol.types.type_name.TypeName"
    """<p>The name of the resource type.</p>"""
    type_version_id: NotRequired[
        "capo_cloudcontrol.types.type_version_id.TypeVersionId"
    ]
    """<p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>"""
    role_arn: NotRequired["capo_cloudcontrol.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>"""
    client_token: NotRequired["capo_cloudcontrol.types.client_token.ClientToken"]
    """<p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>"""
    desired_state: "capo_cloudcontrol.types.properties.Properties"
    """<p>Structured data format representing the desired state of the resource, consisting of that resource's properties and their desired values.</p> <note> <p>Cloud Control API currently supports JSON as a structured data format.</p> </note> <p>Specify the desired state as one of the following:</p> <ul> <li> <p>A JSON blob</p> </li> <li> <p>A local path containing the desired state in JSON data format</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html#resource-operations-create-desiredstate">Composing the desired state of the resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>For more information about the properties of a specific resource, refer to the related topic for the resource in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Resource and property types reference</a> in the <i>CloudFormation Users Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceInput) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    if "type_version_id" in value:
        out["TypeVersionId"] = value["type_version_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["DesiredState"] = value["desired_state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceInput:
    out: CreateResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        raise DeserializationError("CreateResourceInput.type_name required")
    if data.get("TypeVersionId") is not None:
        out["type_version_id"] = data["TypeVersionId"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("DesiredState") is not None:
        out["desired_state"] = data["DesiredState"]
    else:
        raise DeserializationError("CreateResourceInput.desired_state required")
    return out
