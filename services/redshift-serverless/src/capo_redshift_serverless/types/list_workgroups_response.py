"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListWorkgroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.workgroup_list


class ListWorkgroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p> If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.</p>"""
    workgroups: "capo_redshift_serverless.types.workgroup_list.WorkgroupList"
    """<p>The returned array of workgroups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkgroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_redshift_serverless.types.workgroup_list

    out["workgroups"] = (
        capo_redshift_serverless.types.workgroup_list.serialize_aws_json_1_1(
            value["workgroups"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkgroupsResponse:
    out: ListWorkgroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("workgroups") is not None:
        import capo_redshift_serverless.types.workgroup_list

        out["workgroups"] = (
            capo_redshift_serverless.types.workgroup_list.deserialize_aws_json_1_1(
                data["workgroups"]
            )
        )
    else:
        out["workgroups"] = []
    return out
