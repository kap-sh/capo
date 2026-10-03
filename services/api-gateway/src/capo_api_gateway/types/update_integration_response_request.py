"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateIntegrationResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_patch_operation
    import capo_api_gateway.types.status_code
    import capo_api_gateway.types.string


class UpdateIntegrationResponseRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>Specifies an update integration response request's resource identifier.</p>"""
    http_method: "capo_api_gateway.types.string.String"
    """<p>Specifies an update integration response request's HTTP method.</p>"""
    status_code: "capo_api_gateway.types.status_code.StatusCode"
    """<p>Specifies an update integration response request's status code.</p>"""
    patch_operations: NotRequired[
        "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
    ]
    """<p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationResponseRequest) -> dict:
    out: dict = {}
    if "patch_operations" in value:
        import capo_api_gateway.types.list_of_patch_operation

        out["patchOperations"] = (
            capo_api_gateway.types.list_of_patch_operation.serialize_json(
                value["patch_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIntegrationResponseRequest:
    out: UpdateIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
    if data.get("patchOperations") is not None:
        import capo_api_gateway.types.list_of_patch_operation

        out["patch_operations"] = (
            capo_api_gateway.types.list_of_patch_operation.deserialize_json(
                data["patchOperations"]
            )
        )
    return out
