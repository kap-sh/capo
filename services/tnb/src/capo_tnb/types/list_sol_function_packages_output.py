"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionPackagesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_function_package_resources
    import capo_tnb.types.pagination_token


class ListSolFunctionPackagesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_tnb.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    function_packages: "capo_tnb.types.list_sol_function_package_resources.ListSolFunctionPackageResources"
    """<p>Function packages. A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionPackagesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_tnb.types.list_sol_function_package_resources

    out["functionPackages"] = (
        capo_tnb.types.list_sol_function_package_resources.serialize_json(
            value["function_packages"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSolFunctionPackagesOutput:
    out: ListSolFunctionPackagesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("functionPackages") is not None:
        import capo_tnb.types.list_sol_function_package_resources

        out["function_packages"] = (
            capo_tnb.types.list_sol_function_package_resources.deserialize_json(
                data["functionPackages"]
            )
        )
    else:
        out["function_packages"] = []
    return out
