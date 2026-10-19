"""Generated from Smithy shape ``com.amazonaws.interconnect#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.environment_list


class ListEnvironmentsResponse(TypedDict, closed=True):
    environments: "capo_interconnect.types.environment_list.EnvironmentList"
    """<p>The list of matching <a>Environment</a> objects.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token for use in subsequent calls to fetch the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    import capo_interconnect.types.environment_list

    out["environments"] = (
        capo_interconnect.types.environment_list.serialize_aws_json_1_0(
            value["environments"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("environments") is not None:
        import capo_interconnect.types.environment_list

        out["environments"] = (
            capo_interconnect.types.environment_list.deserialize_aws_json_1_0(
                data["environments"]
            )
        )
    else:
        out["environments"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
