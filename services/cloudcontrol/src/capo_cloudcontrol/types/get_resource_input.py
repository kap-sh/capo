"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.identifier
    import capo_cloudcontrol.types.role_arn
    import capo_cloudcontrol.types.type_name
    import capo_cloudcontrol.types.type_version_id


class GetResourceInput(TypedDict, closed=True):
    type_name: "capo_cloudcontrol.types.type_name.TypeName"
    """<p>The name of the resource type.</p>"""
    type_version_id: NotRequired[
        "capo_cloudcontrol.types.type_version_id.TypeVersionId"
    ]
    """<p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>"""
    role_arn: NotRequired["capo_cloudcontrol.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>"""
    identifier: "capo_cloudcontrol.types.identifier.Identifier"
    """<p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceInput) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    if "type_version_id" in value:
        out["TypeVersionId"] = value["type_version_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceInput:
    out: GetResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        raise DeserializationError("GetResourceInput.type_name required")
    if data.get("TypeVersionId") is not None:
        out["type_version_id"] = data["TypeVersionId"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetResourceInput.identifier required")
    return out
