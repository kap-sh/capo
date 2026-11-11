"""Generated from Smithy shape ``com.amazonaws.glue#UserDefinedFunctionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.function_type
    import capo_glue.types.governance_mode
    import capo_glue.types.name_string
    import capo_glue.types.principal_type
    import capo_glue.types.resource_uri_list
    import capo_glue.types.uri


class UserDefinedFunctionInput(TypedDict, closed=True):
    function_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the function.</p>"""
    class_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The Java class that contains the function code.</p>"""
    owner_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The owner of the function.</p>"""
    function_type: NotRequired["capo_glue.types.function_type.FunctionType"]
    """<p>The type of the function.</p>"""
    owner_type: NotRequired["capo_glue.types.principal_type.PrincipalType"]
    """<p>The owner type.</p>"""
    resource_uris: NotRequired["capo_glue.types.resource_uri_list.ResourceUriList"]
    """<p>The resource URIs for the function.</p>"""
    artifact_location: NotRequired["capo_glue.types.uri.URI"]
    """<p>The Amazon S3 location that contains the function's artifacts. Required when <code>GovernanceMode</code> is <code>LAKE_FORMATION</code>. You must register the location with Lake Formation, and every resource URI must be under this location.</p>"""
    governance_mode: NotRequired["capo_glue.types.governance_mode.GovernanceMode"]
    """<p>How access to the function is governed. Specify <code>LAKE_FORMATION</code> to manage access to the function with Lake Formation permissions. If you don't specify a value, the default is <code>IAM_ONLY</code>. You can't change the governance mode after the function is created.</p> <p>When <code>GovernanceMode</code> is <code>LAKE_FORMATION</code>:</p> <ul> <li> <p>You must be a data lake administrator or have all permissions on the Data Catalog with the grant option.</p> </li> <li> <p>You must have the <code>DATA_LOCATION_ACCESS</code> permission on the <code>ArtifactLocation</code>, unless you're a data lake administrator.</p> </li> <li> <p>You must specify from 1 to 10 resource URIs, each under the <code>ArtifactLocation</code>.</p> </li> <li> <p>You can't rename the function.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDefinedFunctionInput) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "class_name" in value:
        out["ClassName"] = value["class_name"]
    if "owner_name" in value:
        out["OwnerName"] = value["owner_name"]
    if "function_type" in value:
        import capo_glue.types.function_type

        out["FunctionType"] = capo_glue.types.function_type.serialize_aws_json_1_1(
            value["function_type"]
        )
    if "owner_type" in value:
        import capo_glue.types.principal_type

        out["OwnerType"] = capo_glue.types.principal_type.serialize_aws_json_1_1(
            value["owner_type"]
        )
    if "resource_uris" in value:
        import capo_glue.types.resource_uri_list

        out["ResourceUris"] = capo_glue.types.resource_uri_list.serialize_aws_json_1_1(
            value["resource_uris"]
        )
    if "artifact_location" in value:
        out["ArtifactLocation"] = value["artifact_location"]
    if "governance_mode" in value:
        import capo_glue.types.governance_mode

        out["GovernanceMode"] = capo_glue.types.governance_mode.serialize_aws_json_1_1(
            value["governance_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDefinedFunctionInput:
    out: UserDefinedFunctionInput = {}  # type: ignore[typeddict-item]
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    if data.get("ClassName") is not None:
        out["class_name"] = data["ClassName"]
    if data.get("OwnerName") is not None:
        out["owner_name"] = data["OwnerName"]
    if data.get("FunctionType") is not None:
        import capo_glue.types.function_type

        out["function_type"] = capo_glue.types.function_type.deserialize_aws_json_1_1(
            data["FunctionType"]
        )
    if data.get("OwnerType") is not None:
        import capo_glue.types.principal_type

        out["owner_type"] = capo_glue.types.principal_type.deserialize_aws_json_1_1(
            data["OwnerType"]
        )
    if data.get("ResourceUris") is not None:
        import capo_glue.types.resource_uri_list

        out["resource_uris"] = (
            capo_glue.types.resource_uri_list.deserialize_aws_json_1_1(
                data["ResourceUris"]
            )
        )
    if data.get("ArtifactLocation") is not None:
        out["artifact_location"] = data["ArtifactLocation"]
    if data.get("GovernanceMode") is not None:
        import capo_glue.types.governance_mode

        out["governance_mode"] = (
            capo_glue.types.governance_mode.deserialize_aws_json_1_1(
                data["GovernanceMode"]
            )
        )
    return out
