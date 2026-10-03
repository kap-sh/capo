"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateBasePathMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_patch_operation
    import capo_api_gateway.types.string


class UpdateBasePathMappingRequest(TypedDict, closed=True):
    domain_name: "capo_api_gateway.types.string.String"
    """<p>The domain name of the BasePathMapping resource to change.</p>"""
    domain_name_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p> The identifier for the domain name resource. Supported only for private custom domain names. </p>"""
    base_path: "capo_api_gateway.types.string.String"
    """<p>The base path of the BasePathMapping resource to change.</p> <p>To specify an empty base path, set this parameter to <code>'(none)'</code>.</p>"""
    patch_operations: NotRequired[
        "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
    ]
    """<p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBasePathMappingRequest) -> dict:
    out: dict = {}
    if "patch_operations" in value:
        import capo_api_gateway.types.list_of_patch_operation

        out["patchOperations"] = (
            capo_api_gateway.types.list_of_patch_operation.serialize_json(
                value["patch_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBasePathMappingRequest:
    out: UpdateBasePathMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("patchOperations") is not None:
        import capo_api_gateway.types.list_of_patch_operation

        out["patch_operations"] = (
            capo_api_gateway.types.list_of_patch_operation.deserialize_json(
                data["patchOperations"]
            )
        )
    return out
