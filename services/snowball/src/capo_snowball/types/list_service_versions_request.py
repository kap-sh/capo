"""Generated from Smithy shape ``com.amazonaws.snowball#ListServiceVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.dependent_service_list
    import capo_snowball.types.list_limit
    import capo_snowball.types.service_name
    import capo_snowball.types.string


class ListServiceVersionsRequest(TypedDict, closed=True):
    service_name: "capo_snowball.types.service_name.ServiceName"
    """<p>The name of the service for which you're requesting supported versions.</p>"""
    dependent_services: NotRequired[
        "capo_snowball.types.dependent_service_list.DependentServiceList"
    ]
    """<p>A list of names and versions of dependant services of the requested service.</p>"""
    max_results: NotRequired["capo_snowball.types.list_limit.ListLimit"]
    """<p>The maximum number of <code>ListServiceVersions</code> objects to return.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for the next list of returned <code>ListServiceVersionsRequest</code> versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceVersionsRequest) -> dict:
    out: dict = {}
    import capo_snowball.types.service_name

    out["ServiceName"] = capo_snowball.types.service_name.serialize_aws_json_1_1(
        value["service_name"]
    )
    if "dependent_services" in value:
        import capo_snowball.types.dependent_service_list

        out["DependentServices"] = (
            capo_snowball.types.dependent_service_list.serialize_aws_json_1_1(
                value["dependent_services"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceVersionsRequest:
    out: ListServiceVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceName") is not None:
        import capo_snowball.types.service_name

        out["service_name"] = capo_snowball.types.service_name.deserialize_aws_json_1_1(
            data["ServiceName"]
        )
    else:
        import typing

        out["service_name"] = typing.cast(
            "capo_snowball.types.service_name.ServiceName", ""
        )
    if data.get("DependentServices") is not None:
        import capo_snowball.types.dependent_service_list

        out["dependent_services"] = (
            capo_snowball.types.dependent_service_list.deserialize_aws_json_1_1(
                data["DependentServices"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
