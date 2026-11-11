"""Generated from Smithy shape ``com.amazonaws.glue#UserDefinedFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.function_type
    import capo_glue.types.governance_mode
    import capo_glue.types.name_string
    import capo_glue.types.principal_type
    import capo_glue.types.resource_uri_list
    import capo_glue.types.timestamp
    import capo_glue.types.uri


class UserDefinedFunction(TypedDict, closed=True):
    function_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the function.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the catalog database that contains the function.</p>"""
    class_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The Java class that contains the function code.</p>"""
    owner_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The owner of the function.</p>"""
    function_type: NotRequired["capo_glue.types.function_type.FunctionType"]
    """<p>The type of the function.</p>"""
    owner_type: NotRequired["capo_glue.types.principal_type.PrincipalType"]
    """<p>The owner type.</p>"""
    create_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the function was created.</p>"""
    resource_uris: NotRequired["capo_glue.types.resource_uri_list.ResourceUriList"]
    """<p>The resource URIs for the function.</p>"""
    artifact_location: NotRequired["capo_glue.types.uri.URI"]
    """<p>The Amazon S3 location that contains the function's artifacts. This location must be registered with Lake Formation. Glue returns this field only for functions whose <code>GovernanceMode</code> is <code>LAKE_FORMATION</code>.</p>"""
    governance_mode: NotRequired["capo_glue.types.governance_mode.GovernanceMode"]
    """<p>How access to the function is governed. <code>IAM_ONLY</code> means access is controlled by IAM permissions only. <code>LAKE_FORMATION</code> means Lake Formation permissions (<code>EXECUTE</code>, <code>DESCRIBE</code>, <code>ALTER</code>, and <code>DROP</code>) also control who can run, describe, update, and delete the function.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the function resides.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDefinedFunction) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
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
    if "create_time" in value:
        import capo_glue.types.timestamp

        out["CreateTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
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
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDefinedFunction:
    out: UserDefinedFunction = {}  # type: ignore[typeddict-item]
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
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
    if data.get("CreateTime") is not None:
        import capo_glue.types.timestamp

        out["create_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
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
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    return out
