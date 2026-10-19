"""Generated from Smithy shape ``com.amazonaws.snowball#ListServiceVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.dependent_service_list
    import capo_snowball.types.service_name
    import capo_snowball.types.service_version_list
    import capo_snowball.types.string


class ListServiceVersionsResult(TypedDict, closed=True):
    service_versions: "capo_snowball.types.service_version_list.ServiceVersionList"
    """<p>A list of supported versions.</p>"""
    service_name: "capo_snowball.types.service_name.ServiceName"
    """<p>The name of the service for which the system provided supported versions.</p>"""
    dependent_services: NotRequired[
        "capo_snowball.types.dependent_service_list.DependentServiceList"
    ]
    """<p>A list of names and versions of dependant services of the service for which the system provided supported versions.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point of the next list of returned <code>ListServiceVersionsResult</code> results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceVersionsResult) -> dict:
    out: dict = {}
    import capo_snowball.types.service_version_list

    out["ServiceVersions"] = (
        capo_snowball.types.service_version_list.serialize_aws_json_1_1(
            value["service_versions"]
        )
    )
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
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceVersionsResult:
    out: ListServiceVersionsResult = {}  # type: ignore[typeddict-item]
    if data.get("ServiceVersions") is not None:
        import capo_snowball.types.service_version_list

        out["service_versions"] = (
            capo_snowball.types.service_version_list.deserialize_aws_json_1_1(
                data["ServiceVersions"]
            )
        )
    else:
        out["service_versions"] = []
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
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
