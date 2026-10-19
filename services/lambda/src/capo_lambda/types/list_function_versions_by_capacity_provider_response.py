"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionVersionsByCapacityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_arn
    import capo_lambda.types.function_versions_by_capacity_provider_list
    import capo_lambda.types.string


class ListFunctionVersionsByCapacityProviderResponse(TypedDict, closed=True):
    capacity_provider_arn: "capo_lambda.types.capacity_provider_arn.CapacityProviderArn"
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    function_versions: "capo_lambda.types.function_versions_by_capacity_provider_list.FunctionVersionsByCapacityProviderList"
    """<p>A list of function versions that use the specified capacity provider.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionVersionsByCapacityProviderResponse) -> dict:
    out: dict = {}
    out["CapacityProviderArn"] = value["capacity_provider_arn"]
    import capo_lambda.types.function_versions_by_capacity_provider_list

    out["FunctionVersions"] = (
        capo_lambda.types.function_versions_by_capacity_provider_list.serialize_json(
            value["function_versions"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListFunctionVersionsByCapacityProviderResponse:
    out: ListFunctionVersionsByCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["CapacityProviderArn"]
    else:
        out["capacity_provider_arn"] = ""
    if data.get("FunctionVersions") is not None:
        import capo_lambda.types.function_versions_by_capacity_provider_list

        out["function_versions"] = (
            capo_lambda.types.function_versions_by_capacity_provider_list.deserialize_json(
                data["FunctionVersions"]
            )
        )
    else:
        out["function_versions"] = []
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
