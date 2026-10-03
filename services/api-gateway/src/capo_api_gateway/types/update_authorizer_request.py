"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_patch_operation
    import capo_api_gateway.types.string


class UpdateAuthorizerRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    authorizer_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the Authorizer resource.</p>"""
    patch_operations: NotRequired[
        "capo_api_gateway.types.list_of_patch_operation.ListOfPatchOperation"
    ]
    """<p>For more information about supported patch operations, see <a href="https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html">Patch Operations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAuthorizerRequest) -> dict:
    out: dict = {}
    if "patch_operations" in value:
        import capo_api_gateway.types.list_of_patch_operation

        out["patchOperations"] = (
            capo_api_gateway.types.list_of_patch_operation.serialize_json(
                value["patch_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAuthorizerRequest:
    out: UpdateAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if data.get("patchOperations") is not None:
        import capo_api_gateway.types.list_of_patch_operation

        out["patch_operations"] = (
            capo_api_gateway.types.list_of_patch_operation.deserialize_json(
                data["patchOperations"]
            )
        )
    return out
