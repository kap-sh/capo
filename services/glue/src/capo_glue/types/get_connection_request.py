"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.catalog_id_string
    import capo_glue.types.compute_environment
    import capo_glue.types.name_string


class GetConnectionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the connection definition to retrieve.</p>"""
    hide_password: NotRequired["capo_glue.types.boolean.Boolean"]
    """<p>Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.</p>"""
    apply_override_for_compute_environment: NotRequired[
        "capo_glue.types.compute_environment.ComputeEnvironment"
    ]
    """<p>For connections that may be used in multiple services, specifies returning properties for the specified compute environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    if "hide_password" in value:
        out["HidePassword"] = value["hide_password"]
    if "apply_override_for_compute_environment" in value:
        import capo_glue.types.compute_environment

        out["ApplyOverrideForComputeEnvironment"] = (
            capo_glue.types.compute_environment.serialize_aws_json_1_1(
                value["apply_override_for_compute_environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionRequest:
    out: GetConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("HidePassword") is not None:
        out["hide_password"] = data["HidePassword"]
    if data.get("ApplyOverrideForComputeEnvironment") is not None:
        import capo_glue.types.compute_environment

        out["apply_override_for_compute_environment"] = (
            capo_glue.types.compute_environment.deserialize_aws_json_1_1(
                data["ApplyOverrideForComputeEnvironment"]
            )
        )
    return out
